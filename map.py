import folium

m = folium.Map(location=(30, 10), zoom_start=4, tiles="cartodb positron")
m.save("footprint.html")
