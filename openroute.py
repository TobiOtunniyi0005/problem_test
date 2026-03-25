import openrouteservice
from geopy.geocoders import Nominatim
from openrouteservice.exceptions import ApiError, HTTPError
import random

# === 1. SETUP ===
# Replace with your actual API key
list_api = ['5b3ce3597851110001cf62481fc838a6b1754afe8313b795ffb529d0', '5b3ce3597851110001cf624800db0748415048deb44fae0a6ba54ecf','5b3ce3597851110001cf62488422d6a751b544e08a1e7ece24096263','5b3ce3597851110001cf624835312da062fb41229eab9234dc551cff','5b3ce3597851110001cf6248976e0d255d0a4b6cb12b6a12c5929dee','5b3ce3597851110001cf6248cab175c8a6274a6793556208cb3af460']
ORS_API_KEY = list_api[random.randint(0,len(list_api)-1)]#'your-api-key-here'

# Create clients
ors_client = openrouteservice.Client(key=ORS_API_KEY)
geolocator = Nominatim(user_agent="distance_by_name")

# === 2. USER INPUT ===
#place1 = input("Enter the first location: ")
#place2 = input("Enter the second location: ")

def calcdistpoints(place1: str, place2: str) -> float:
    try:
        location1 = geolocator.geocode(place1)
        location2 = geolocator.geocode(place2)

        if location1 and location2:
            coords1 = (location1.longitude, location1.latitude)
            coords2 = (location2.longitude, location2.latitude)

            try:
                route = ors_client.directions(
                    coordinates=[coords1, coords2],
                    profile='driving-car',
                    format='geojson'
                )

                distance_km = route['features'][0]['properties']['segments'][0]['distance'] / 1000
                print(f'Openroute said the distance was: {2*distance_km}Km')
                return 2*distance_km#Should Returns two way distance
            except:
                print('Openroute tapped out.')
                return -1  # ORS failed silently
        else:
            print('Openroute did not find both of these places.')
            return -1  # Location not found
    except:
        print('Openroute found some API way to tap out.')
        return -1  # Geocoding or any other error