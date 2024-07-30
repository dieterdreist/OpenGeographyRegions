#!/usr/bin/env python3
# this script formats a given geojson output to a compromise of compactness and readability
import json
import argparse
from io import StringIO
from collections import OrderedDict

def main():
    parser = argparse.ArgumentParser(description='Reformat a GeoJSON file.')
    parser.add_argument('geofile', type=str, help='path to the GeoJSON input file')

    properties = ["name", "featureclass", "scalerank", "region", "subregion", "wikidata"] # this is the order
    args = parser.parse_args()
    
    geofile_path = args.geofile

    try:
        # Open and read the GeoJSON file
        with open(geofile_path, "r") as geofile:
            jsonfromfile = geofile.read()
            # Parse the JSON content
            pythobject = json.loads(jsonfromfile)
           
            # Define the sorting key function to handle null values
            def sort_key(feature):
                region = feature['properties'].get('region')
                name = feature['properties'].get('name')
                # Replace None with a special value that ensures it sorts before any string
                return ('' if region is None else region, '' if name is None else name)
        
            # Sort the features by properties.region and then by properties.name
            pythobject['features'].sort(key=sort_key)

            generalobject = pythobject.copy()
            generalobject.pop("features")
            j = json.dumps(generalobject, indent=2)
            j = j[:j.rfind('\n')] # remove last line
            featuresdict = { k : pythobject[k] for k in set(pythobject) - set(generalobject) }
            j = j + ',\n  "features": ['
            f = ''
            for feature in featuresdict["features"]:
                otherkeys = feature.copy()
                otherkeys.pop("geometry")
                fproperties = OrderedDict()
                fproperties.update(otherkeys["properties"])
                if "wikidata" not in fproperties:
                    fproperties["wikidata"] = ""
                for prop in properties:
                    if prop in fproperties:
                        if fproperties[prop] is None:
                            fproperties.pop(prop)
                        else:
                            fproperties.move_to_end(prop)

                # reassign the OrderedDict
                otherkeys["properties"]=fproperties

                # format the output string so that the geometry property is in a single line:
                f = json.dumps(otherkeys, indent=2, sort_keys=False)
                f = f[:f.rfind('\n')] # remove last line
                f = f + (',\n  "geometry": ')
                f = f + json.dumps(feature["geometry"]) + "\n},"
                j = j + "\n" + f

            # remove comma from last line
            j = j[:j.rfind('\n')] # remove last line
            j = j + "\n}"


            j = j + "\n  ]\n}"
            print(j)

    except FileNotFoundError:
        print(f"Error: The file '{geofile_path}' does not exist.")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

