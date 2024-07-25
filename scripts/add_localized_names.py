#!/usr/bin/env python3
import json
import argparse
import urllib.parse
import urllib.request

def fetch_wikidata_labels(wikidata, languages):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbgetentities",
        "ids": wikidata,
        "format": "json",
        "props": "labels"
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{url}?{query_string}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    labels = {}
    if "entities" in data and wikidata in data["entities"]:
        entity = data["entities"][wikidata]
        for lang in languages:
            if lang in entity["labels"]:
                labels[lang] = entity["labels"][lang]["value"]
            else:
                labels[lang] = None

    return labels

def add_labels_to_geojson(input_geojson, output_geojson, languages):
    with open(input_geojson, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for feature in data['features']:
        if 'wikidata' in feature['properties']:
            wikidata = feature['properties']['wikidata']
            labels = fetch_wikidata_labels(wikidata, languages)
            for lang, label in labels.items():
                feature['properties'][f'name_{lang}'] = label

    with open(output_geojson, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=True, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Add names in multiple languages from Wikidata to a GeoJSON file.")
    parser.add_argument("input_geojson", type=str, help="Input GeoJSON file")
    parser.add_argument("output_geojson", type=str, help="Output GeoJSON file")
    parser.add_argument("languages", type=str, nargs="+", help="List of language codes")

    args = parser.parse_args()
    add_labels_to_geojson(args.input_geojson, args.output_geojson, args.languages)

if __name__ == "__main__":
    main()
