# OpenGeographyRegions
A project to create a free, global, crowdsourced, multilingual dataset of geographic regions. Typical usecase is drawing an oriented label at an approximate position and shape.

**This is work in progress, pull requests and other input are welcome.**

Just draw a geographic region that you know, add a reference to wikidata, and sent your pull request. A basic geojson editor can be found at [geojson.io](http://geojson.io/).

## Simple polygons, appropriate for different scales.
The project started with the 10m geography dataset from [natural earth](https://www.naturalearthdata.com/). There are currently 1050 features.
The structure of the data can be seen here: [Features](Features.md)

![](resources/names.png)

## Linked Data
The integration of wikidata allows for internationalization in many languages and provides semantic information beyond location.
Add a property `wikidata` with value "Q..." (wikidata id) to reference a wikidata object.

## Open License
The license is CC0.

## Data in GeoJSON
The data is available in GeoJSON. Here is the [raw version](https://github.com/dieterdreist/OpenGeographyRegions/raw/master/geojson/).

### Editing conventions
Feel free to draw polygons for areas that you know and propose them for inclusion. See [CONTRIBUTING](CONTRIBUTING) for more information.

#### Properties
Stick to this property ordering to avoid unnecessary history cluttering (the script is ensuring the correct order).
Do not add additional properties without discussion. Major importance is on the wikidata item link, as the idea is to pull names in different languages from wikidata and not store them here.
* name
* featureclass
* scalerank *(not sure this is needed, might be removed in a following version)*
* region
* subregion
* wikidata

(the marine layer does not have `region` and `subregion` properties). 

#### Regions
* Africa
* Antarctica
* Asia
* Europe
* North America
* Oceania
* Seven seas (open ocean)
* South America

![](resources/regions.png)

### Usage hints
#### Localized names
You can query wikidata for localized names with the script [add_localized_names.py](scripts/add_localized_names.py), for example `./add_localized_names.py input.geojson output.geojson de en fr it` will get the localized names in German, English, French and Italian and add them as name_de etc. in the output file.
#### Labels
For labeling you can reduce the areas to a line, e.g. with PostGIS and [ST_ApproximateMedialAxis](https://postgis.net/docs/ST_ApproximateMedialAxis.html) or with the python tool [label_centerlines](https://github.com/ungarj/label_centerlines) by Joachim Ungar.
