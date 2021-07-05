#! /bin/python3
import os.path
import argparse
import xml.etree.ElementTree as ElementTree

def round(infile, outfile, rounds):
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

if "__main__"==__name__:
    parser = argparse.ArgumentParser(description='Trim excess digits from height values (uses Python float rounding rules).')
    parser.add_argument('infile',
                        help='Source data')
    args = parser.parse_args()
    fbase=os.path.splitext(os.path.basename(args.infile))[0]
    outfile=fbase+'.rounded.osm'
    rounds=open(fbase+'.rounds.txt', 'w')
    round(args.infile, outfile, rounds)