# Layers and features in the data
## Layers
The data is divided in thematic layers, each layer is represented by a geojson file.
* continents
* geoareas
* islands
* terrain
* waterrelated
* deserts
* biomes 

Note: while deserts are waterrelated, they get their own layer.

## Features
The following table shows which features can currently be expected in the different layers. You can also find this information structured in featureclasses_layers.json. This is work in progress, and featureclasses as well as layers may still be added or changed if deemed useful.

| featureclass | layer | definition | wikidata |
|--------------|-------------|-----------------------------------------------------------|----------|
| archipel | islands | An archipelago is a group of islands | Q33837 |
| basin | terrain | here a basin is a depression on land (seawater covered basins are found in the sea file) | Q190429 |
| coast | waterrelated | a coastal land area | Q93352 |
| continent | continents | large landmass as recognized by cultural convention | Q5107 |
| delta | waterrelated | a river delta, a landform at the mouth of a river | Q43197 |
| desert | deserts | a landscape with little precipitation | Q8514 |
| foothills | terrain | hilly transition zone between plains and higher mountains or hills | Q1354045 |
| geoarea | geoareas | a geographic region | Q82794 |
| gorge | terrain | a narrow and deep ravine between cliffs, a canyon | Q150784 |
| island | islands | an island: land completely surrounded by water and smaller than a continent | Q23442 |
| isthmus | waterrelated | a narrow strip of land connecting two larger land areas | Q93267 |
| lake | waterrelated | a body of relatively still water located in a basin | Q23397 |
| lowland | terrain | plains which are located close to the sea level (not above ~150m) | Q193071 |
| mountain_range | terrain | an area with several geologically related mountains | Q46831 |
| peninsula | waterrelated | a landform which is surrounded more than half but not completely by water | Q34763 |
| plain | terrain | a flat geographic region (see also lowland and plateau) | Q160091 |
| plateau | terrain | a flat geographic region which is higher than the surrounding | Q75520 |
| tundra | biomes | a biome where the tree growth is hindered by low temperatures and short grow seasons | Q43262 |
| valley | terrain | low area between hills, often with a river running through it | Q39816 |
| wetlands | waterrelated | land area that is permanently or seasonally saturated with water | Q170321 |
