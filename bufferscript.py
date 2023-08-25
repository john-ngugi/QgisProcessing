from qgis.core import *
from qgis.utils import *
import processing 
import os

path ='/Users/User/Documents/internal attachment/week 1/day 2/Data (1)/Data/counties.shp'
#addLayer(path_to _data(string),layerName(string),"provider"))
vlayer= iface.addVectorLayer(path,"counties","ogr")
layer = iface.activeLayer()
print(layer)   
layer.selectByExpression("\"COUNTY\"='Nueces'")   
new_layer = layer.materialize(QgsFeatureRequest().setFilterFids(layer.selectedFeatureIds()))
airports=iface.addVectorLayer('/Users/User/Documents/internal attachment/week 1/day 2/Data (1)/Data/airports.shp','airports','ogr')
QgsProject.instance().addMapLayer(new_layer)
roadsPath='/Users/User/Documents/internal attachment/week 1/day 2/Data (1)/Data/Roads.shp'
roadsLayer = iface.addVectorLayer(roadsPath,"roads","ogr")
bufferpath='/Users/User/Desktop/desktop folders/programming/Qgiscodes/buffer/airportsBuff5.shp'

processing.run('native:buffer',{"INPUT":airports,"DISTANCE":5000,"DISOLVE":False,"EXPLODE_COLLECTIONS":True,"OUTPUT":bufferpath})
buffLayer=iface.addVectorLayer(bufferpath,"","ogr")

# perform clip 

#add the overlay polygon path 
polyPath= new_layer
#add the point or clip feature path 
pointPath=bufferpath
# add the output feature path
clipPath= 'C:/Users/User/Documents/pyclips/clippedbufferAirports.shp'
# run the clip 
processing.run('native:clip',{'INPUT': pointPath,'OVERLAY':polyPath,'OUTPUT':clipPath})
#add the clipped feature to the map canvas 
iface.addVectorLayer(clipPath,"",'ogr')
