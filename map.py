# # import folium

# # # Create a map centered around India
# # india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4)

# # # Add a marker for a specific location in India
# # marker_location = [28.6139, 77.2090]  # Delhi, India
# # folium.Marker(marker_location, popup='Delhi, India').add_to(india_map)

# # # Add a popup with embedded Street View
# # popup_content = f'<iframe width="400" height="300" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/streetview?key=YOUR_API_KEY&location={marker_location[0]},{marker_location[1]}" allowfullscreen></iframe>'
# # popup = folium.Popup(popup_content, max_width=600)
# # popup.add_to(folium.Marker(marker_location))

# # # Display the map
# # india_map.save('india_street_view.html')


# import folium

# # Create a map centered around India
# india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4)

# # Add a marker for a specific location in India
# marker_location = [28.6139, 77.2090]  # Delhi, India
# folium.Marker(marker_location, popup="Delhi, India").add_to(india_map)

# # Customize popup content with Street View iframe and additional styling
# popup_content = f"""
# <div style="width: 400px; height: 300px;">
#     <iframe width="100%" height="100%" frameborder="0" style="border:0"
#             src="https://www.google.com/maps/embed/v1/streetview?key=YOUR_API_KEY&location={marker_location[0]},{marker_location[1]}"
#             allowfullscreen>
#     </iframe>
# </div>
# """
# popup = folium.Popup(popup_content, max_width=600)

# # Add popup to marker
# folium.Marker(marker_location, popup=popup).add_to(india_map)

# # Save map as HTML file
# india_map.save("india_street_view.html")




import folium

# Create a map centered at a specific location
m = folium.Map(location=[28.6139, 77.2090], zoom_start=12)  # Delhi, India coordinates

# Define marker coordinates and popup messages

marker_data = [
    {
        "location": [28.5907, 77.2315],
        "popup": "You are here",
        "color": "red",
    },  # Delhi marker
    {
        "location": [28.5849, 77.2214],
        "popup": "SDMC Dump Zone",
        "color": "green",
        "icon " : "A",
    },  # Near Delhi marker 2
    {"location": [28.572, 77.2011], "popup": "MCD Dump Zone", "color": "green"},
    {"location": [28.5586, 77.2775], "popup": "Garbage Zone 1", "color": "green"},
    {
        "location": [28.5812, 77.2631],
        "popup": "Garbage Zone 2",
        "color": "green",
    },  # Near Delhi marker 3
]

# Add markers to the map
for data in marker_data:
    folium.Marker(
        location=data["location"],
        popup=data["popup"],
        icon=folium.Icon(color=data["color"], icon="info-sign"),
    ).add_to(m)

# Display the map
m.save("map.html")
