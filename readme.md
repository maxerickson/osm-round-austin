Scripts to mechanically edit poorly formatted building heights from the [Austin, TX/Buildings Import](http://wiki.openstreetmap.org/wiki/Austin,_TX/Buildings_Import).

fetch.sh pulls data from Overpass-Api using this query: http://overpass-turbo.eu/s/ksJ and stores it in buildings.osm.

round.py reads buildings.osm and rounds the height values to 2 digits, saving the modified data in rounded_buildings.osm.