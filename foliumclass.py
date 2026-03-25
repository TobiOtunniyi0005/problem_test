import folium
import webbrowser

# Create map centered on a location
def gpshtml(lcoord:list):
    m = folium.Map(location=lcoord[0], zoom_start=13)

    # List of locations (lat, lon)
    locations = lcoord#Instead of hardcoding

    # Add markers
    for loc in locations:
        folium.Marker(location=loc).add_to(m)

    # Draw path
    folium.PolyLine(locations, color="blue", weight=2.5, opacity=1).add_to(m)

    # Save map
    m.save("map_with_path.html")
    webbrowser.open("map_with_path.html")  # or any other file