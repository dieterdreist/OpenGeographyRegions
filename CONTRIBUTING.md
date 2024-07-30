Contributions are welcome. You agree that everything you contribute can be distributed with the specified license (cc-0) and you confirm that you have all the rights necessary for publishing the content you contribute under this license.

## Formatting
Only use spaces, 2 spaces for each indentation level. Do not break the `geometry` value into lines so that the file becomes easier readable.

You can use formatjson.py from the [scripts folder](scripts) to format a geojson file accordingly (but does not round the coordinate precision yet).

Note that you have to escape special characters in json (e.g. names). You can use for quick adhoc conversions `echo -n "your strange näme" | jq -Rsa .`

### Properties
Stick to this property ordering to avoid unnecessary history cluttering (the script is ensuring the correct order).
Do not add additional properties without discussion. Major importance is on the wikidata item link, as the idea is to pull names in different languages from wikidata and not store them here.
* name
* featureclass
* scalerank *(not sure this is needed, might be removed in a following version)*
* region
* subregion
* wikidata

(the marine layer does not have `region` and `subregion` properties). 

### Names
The indicated name should be in English or the local language. It is not very relevant because you are expected to add the wikidata property so that any name available in wikidata can be pulled on the fly (see localized name script in the scripts folder).

### Coordinate precision
4 digits coordinate precision is more than sufficient (this corresponds to about 11.1m resolution at the equator)

### Sort order
Within the geojson file, the features are sorted by `region` and within the region by `name`.

#### Regions
* Africa
* Antarctica
* Asia
* Europe
* North America
* Oceania
* Seven seas (open ocean)
* South America

