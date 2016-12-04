#! /bin/python3
import xml.etree.ElementTree as ElementTree

infile="buildings.osm"
outfile="rounded_buildings.osm"
rounds=open("rounding.txt", "w")

tree=ElementTree.parse(infile)
osm=tree.getroot()
osm.set('generator', 'round.py')
for child in osm:
    if child.tag in {"way","relation"}:
        try:
            # round the height.
            t=child.findall("./tag[@k='height']")[0]
            h=t.get('v')
            newh='%.2f' % float(h)
            rounds.write(h+' '+newh+'\n')
            t.set('v', newh)
            # mark element as modified.
            child.set('action', 'modify')
        except: # should only be child ways of relations
            print(child.get('id'))
tree.write(outfile)