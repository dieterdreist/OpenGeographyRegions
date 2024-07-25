# Layers and features in the data
## Layers
The data is divided in thematic layers, each layer is represented by a geojson file.
* continents
* geoareas
* islands
* maritime
* terrain
* waterrelated
* deserts
* biomes

Note: while deserts are waterrelated, they get their own layer.

## Features
The following table shows which features can currently be expected in the different layers. You can also find this information structured in [featureclasses_layers.json](https://github.com/dieterdreist/OpenGeographyRegions/blob/master/featureclasses_layers.json). This is work in progress, and featureclasses as well as layers may still be added or changed if deemed useful.

| featureclass | layer | definition | wikidata |
|--------------|-------------|-----------------------------------------------------------|----------|
| archipelago | islands | An archipelago is a group of islands | Q33837 |
| basin | terrain | here a basin is a depression on land (seawater covered basins are found in the sea file) | Q190429 |
| coast | terrain | a coastal land area | Q93352 |
| continent | continents | large landmass as recognized by cultural convention | Q5107 |
| delta | waterrelated | a river delta, a landform at the mouth of a river | Q43197 |
| desert | deserts | a landscape with little precipitation | Q8514 |
| foothills | terrain | hilly transition zone between plains and higher mountains or hills | Q1354045 |
| geoarea | geoareas | a geographic region | Q82794 |
| gorge | terrain | a narrow and deep ravine between cliffs, a canyon | Q150784 |
| island | islands | an island: land completely surrounded by water and smaller than a continent | Q23442 |
| isthmus | terrain | a narrow strip of land connecting two larger land areas | Q93267 |
| lake | waterrelated | a body of relatively still water located in a basin | Q23397 |
| lowland | terrain | plains which are located close to the sea level (not above ~150m) | Q193071 |
| mountainrange | terrain | an area with several geologically related mountains | Q46831 |
| peninsula | terrain | a landform which is surrounded more than half but not completely by water | Q34763 |
| plain | terrain | a flat geographic region (see also lowland and plateau) | Q160091 |
| plateau | terrain | a flat geographic region which is higher than the surrounding | Q75520 |
| tundra | biomes | a biome where the tree growth is hindered by low temperatures and short grow seasons | Q43262 |
| valley | terrain | low area between hills, often with a river running through it | Q39816 |
| wetlands | waterrelated | land area that is permanently or seasonally saturated with water | Q170321 |
| bay | maritime | body of water connected to an ocean or lake, formed by an indentation of the shoreline | Q39594 |
| channel | maritime | type of landform; confined river; strait | Q1210950 |
| fjord | maritime | long, narrow inlet of the ocean created in a valley carved by glacial activity | Q45776 |
| generic | maritime |  |  |
| gulf | maritime | large inlet that is an arm of an ocean or sea | Q1322134 |
| inlet | maritime | an indentation of a shoreline that often leads to an enclosed body of salt water, such as a sound, bay, lagoon, or marsh | Q1172599 |
| lagoon | maritime | shallow body of water separated from larger body of water by a barrier | Q187223 |
| ocean | maritime | very large body of saline water | Q9430 |
| reef | maritime | feature lying beneath the surface of the water | Q184358 |
| river | maritime | larger natural watercourse | Q4022 |
| sea | maritime | large body of saline water | Q165 |
| sound | maritime | long, relatively wide body of water, connecting two larger parts of the sea | Q491713 |
| strait | maritime | naturally formed, narrow waterway that connects two larger bodies of water | Q37901 |

### Properties
While all properties are optional you should provide these properties for easier handling (identification)
* name
* featureclass
* scalerank 
* region
* subregion
* wikidata

### Regions
These are the currently used values for the `region`, you should not add more regions:
* Africa
* Antarctica
* Asia
* Europe
* North America
* Oceania
* Seven seas (open ocean)
* South America

### Subregions
These are the currently used values for the `subregion` but you can add more subregions as you see fit:
* Arabian Sea
* Arctic Archipelago
* Arctic Ocean
* Australasia
* Bay of Bengal
* British Isles
* Central America
* Comores
* Falkland Islands
* Galapagos islands
* Greenland
* Iceland
* Indian Ocean
* Is. Revillagigedo
* Malay Archipelago
* Mascarene Islands
* Mediterranean Sea
* Melanesia
* Micronesia
* New Zealand
* North Atlantic Ocean
* Polynesia
* Seychelles
* South China Sea
* Southern Atlantic Ocean
* Southern Indian Ocean
* West Indies

### imported from geography_10m.geojson v.5.0.0 feature classes
*   7 "continent"
*  68 "peninsula"
*  12 "delta"
*   4 "isthmus"
* 295 "island"
* 165 "archipelago"
*  58 "desert"
*   4 "tundra"
*   3 "wetlands"
* 222 "mountain_range"
*  72 "plateau"
*  37 "coast"
*  30 "plain"
*   6 "valley"
*   5 "lowland"
*   11 "basin"
*   3 "foothills"
*   3 "lake"
*   3 "gorge"
*  44 "geoarea"
