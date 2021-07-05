Scripts to mechanically edit poorly formatted building heights from the 
[Austin, TX/Buildings Import](http://wiki.openstreetmap.org/wiki/Austin,_TX/Buildings_Import).

fetch pulls data from Overpass-Api using a provided query file (following 
this query: http://overpass-turbo.eu/s/ksJ for heights) and stores it in a
.osm with the same base name as the query file.

round.py reads an input .osm file and rounds the height values to 2 digits, 
saving the modified data in a file with the same base name and a .rounded.osm 
extension.

The changes in the rounded.osm file can be commited to OSM by opening the file
in JOSM and uploading.