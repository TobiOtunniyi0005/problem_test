from geopy.geocoders import Nominatim
from geopy.distance import geodesic
#from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
# Create geolocator with user agent
geolocator = Nominatim(user_agent="distance_calculator")

# Enter two locations
#place1 = input("Enter the first location: ")
#place2 = input("Enter the second location: ")


def calcdistpoints(place1: str, place2: str) -> float:
    try:
        # Get latitude and longitude
        location1 = geolocator.geocode(place1,timeout=7)
        location2 = geolocator.geocode(place2,timeout=7)

        # Check if both locations were found
        if location1 and location2:
            coords_1 = (location1.latitude, location1.longitude)
            coords_2 = (location2.latitude, location2.longitude)

            # Calculate distance
            one_way = geodesic(coords_1, coords_2).km
            round_trip = one_way * 2

            print(f"Geopy says that round trip distance: {round_trip:.2f} km")
            return round_trip
        else:
            print("Sorry, one or both locations could not be found. Geopy tapped out.")
            return -1
    except Exception as e:
        print(f"Error occurred while calculating distance: {e}")
        return -1

def coordinates(s1:str):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(s1)
    thelist = [location.latitude, location.longitude]
    return thelist



def place_exists(place_name):
    geolocator = Nominatim(user_agent="geo_checker")
    try:
        location = geolocator.geocode(place_name)
        return location is not None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding error: {e}")
        return False

from geopy.geocoders import Nominatim 
import math

def get_xyz_coordinates(place_name):
    # Step 1: Get latitude and longitude in degrees
    geolocator = Nominatim(user_agent="geo_xyz_locator")
    location = geolocator.geocode(place_name)
    
    if not location:
        return None  # or return an empty list []

    lat_deg = location.latitude
    lon_deg = location.longitude

    # Step 2: Convert degrees to radians
    lat_rad = math.radians(lat_deg)
    lon_rad = math.radians(lon_deg)

    # Step 3: Convert to Cartesian (x, y, z) coordinates in km
    R = 6371  # Approximate radius of Earth in km

    x = R * math.cos(lat_rad) * math.cos(lon_rad)
    y = R * math.cos(lat_rad) * math.sin(lon_rad)
    z = R * math.sin(lat_rad)

    return [
        x,                 # x in km
        y,                 # y in km
        z                  # z in km
    ]

