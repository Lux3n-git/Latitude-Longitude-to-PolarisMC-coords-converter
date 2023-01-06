#Credits: TripleLuxen 

from pyproj import Transformer

scaleratio = 326 #1:326 scale of polarisMC map
round_to_dec = 0 #round the coordinates by how many decimals

latitude = input("Latitude?: ")
longitude = input("Longitude?: ")
#asks for both latitude and longitude

transform = Transformer.from_crs("EPSG:4326", 'EPSG:4087') 
#transformer object that will convert long/lat to polarisMC's map projection: "equidistant cylindrical projection (EPSG:4087)"

mapcoords = transform.transform(latitude, longitude)
#converts to xy coordinates of equidistant cylindrical projection on a graph. Think of the origin of the graph (0,0) is where the Equator and Prime Meridian intercept.

x_mc_coord = round(mapcoords[0]/scaleratio,round_to_dec)
z_mc_coord = round(mapcoords[1]/scaleratio,round_to_dec)
#scales coords to the scale of the PolarisMC map compared to real life scale (1:326)

print("PolarisMC Map coords: X: {}, Z: {}".format(x_mc_coord,z_mc_coord))

