#! /bin/python3
import xml.etree.ElementTree as ElementTree

infile="buildings.osm"
outfile="rounded_buildings.osm"
rounds=open("rounding.txt", "w")

tree=ElementTree.parse(infile)
elem=tree.getroot()
for child in elem:
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
        except:
            print(child.get('id'))
tree.write(outfile)