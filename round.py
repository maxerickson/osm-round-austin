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
            # increment version, delete attributes of previous version.
            v=int(child.get('version'))
            child.set('version', str(v+1))
            child.attrib.pop('user')
            child.attrib.pop('uid')
            child.attrib.pop('changeset')
            child.attrib.pop('timestamp')
        except:
            pass
tree.write(outfile)