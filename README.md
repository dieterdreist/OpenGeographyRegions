# OpenGeographyRegions
A project to create a free, global, crowdsourced, multilingual dataset of geographic regions

## Simple polygons, appropriate for different scales.
Starting with natural earths 10m geography dataset.

## Data in GeoJSON
Currently used feature classes (and usage count), derived from natural earth:

### geography_10m.geojson
* 165 "archipel"
*   9 "basin"
*  37 "coast"
*   7 "continent"
*  12 "delta"
*   2 "depression"
*  58 "desert"
*   3 "foothills"
*  44 "geoarea"
*   3 "gorge"
* 295 "island"
*   4 "isthmus"
*   3 "lake"
*   5 "lowland"
* 222 "mountain_range"
*  68 "peninsula"
*  30 "plain"
*  72 "plateau"
*   4 "tundra"
*   6 "valley"
*   3 "wetlands"

The statistics are printed quick + dirty with this bash line: `cat geography_10m.geojson |cut -f 9 -d" "|sort|uniq -c`

## Linked Data (internationalization through integration with wikidata)
work in progress
