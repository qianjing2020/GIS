import geopandas
import numpy
import matplotlib.pyplot as plt
import webbrowser

# read
path_to_data = geopandas.datasets.get_path("nybb")
gdf = geopandas.read_file(path_to_data)
# write
gdf = gdf.set_index("BoroName")
gdf['area'] =  gdf.area

print(type(gdf))
print(gdf.tail())

gdf['boundary'] = gdf.boundary
gdf['centroid'] = gdf.centroid

# measure distance from selected point
first_point = gdf['centroid'].iloc[0]
gdf['distance'] = gdf['centroid'].distance(first_point)

gdf.plot('area', legend=True)
plt.show()

# to include an interactive map, use explore()
# it is a folium map, can be saved as html
map = gdf.explore("area", legend=False)
savefile = "c:/data/map.html"
map.save(savefile)
webbrowser.open(savefile)