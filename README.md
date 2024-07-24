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
Add a property "wikidata" with value "Q..." to reference a wikidata object.

## Open License
The license is CC0.

## Data in GeoJSON
The data is available in GeoJSON. Here is the [raw version](https://github.com/dieterdreist/OpenGeographyRegions/raw/master/geojson/geography_10m.geojson).

### Editing conventions
Only use spaces, 2 spaces for each indentation level. Do not break the *geometry* value into lines so that the file becomes easier readable. 4 digits coordinate precision should be sufficient (this corresponds to about 11.1m resolution at the equator)
You can use formatjson.py from the [scripts folder](scripts) to format a geojson file accordingly.
Note that you have to escape special characters in json (e.g. names). You can use for quick adhoc conversions `echo -n "your strange näme" | jq -Rsa .`
#### Properties
Stick to this property ordering to avoid unnecessary history cluttering (the script is ensuring the correct order).
* name
* featureclass
* scalerank *(not sure this is needed, might be removed in a following version)*
* region
* subregion
* wikidata

#### Regions
* Africa
* Antarctica
* Asia
* Europe
* North America
* Oceania
* South America
* Seven seas (open ocean)

![](resources/regions.png)
