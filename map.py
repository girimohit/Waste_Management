import folium

m = folium.Map(location=[28.6139, 77.2090], zoom_start=12)  # Delhi, India coordinates

marker_data = [
    {
        "location": [28.5907, 77.2315],
        "popup": "You are here",
        "color": "red",
    },
    {
        "location": [28.5849, 77.2214],
        "popup": "SDMC Dump Zone",
        "color": "green",
        "icon ": "A",
    },
    {"location": [28.572, 77.2011], "popup": "MCD Dump Zone", "color": "green"},
    {"location": [28.5586, 77.2775], "popup": "Garbage Zone 1", "color": "green"},
    {
        "location": [28.5812, 77.2631],
        "popup": "Garbage Zone 2",
        "color": "green",
    },
]

# Add markers to the map
for data in marker_data:
    folium.Marker(
        location=data["location"],
        popup=data["popup"],
        icon=folium.Icon(color=data["color"], icon="info-sign"),
    ).add_to(m)

m.save("map.html")
