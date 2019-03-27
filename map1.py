import folium
import pandas

df1=pandas.read_csv("Hotels.csv")
lat=list(df1["Latitude"])
lon=list(df1["Longitude"])
elev=list(df1["Company Name"])


map=folium.Map(location=[40,-70],zoom_start=10,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="my map",overlay=False)


type(elev)
for lt,ln in zip(lat,lon) :
    fg.add_child(folium.Marker(location=[lt,ln],popup="quotes n' hai ",icon=folium.Icon(color='red')))
map.add_child(fg)
map.save("map1.html")
