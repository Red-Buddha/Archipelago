import json
import os

from BaseClasses import Location

######################
# Load location tables from JSON
######################

location_table = {}
with open(os.path.join(os.path.dirname(__file__), '_locations.json'), 'r') as file:
    location_table = json.loads(file.read())

######################
# Generate location lookups
######################

count = 787000

# add sequential generated ids to the lists
for key, _ in enumerate(location_table):
    location_table[key]["id"] = count
    location_table[key]["region"] = "Manual" # all locations are in the same region for Manual
    count += 1

# Add the game completion location, which will have the Victory item assigned to it automatically
location_table.append({
    "id": count + 1,
    "name": "__Manual Game Complete__",
    "region": "Manual",
    "requires": []
})

location_id_to_name = {}
for item in location_table:
    location_id_to_name[item["id"]] = item["name"]

# location_id_to_name[None] = "__Manual Game Complete__"
location_name_to_id = {name: id for id, name in location_id_to_name.items()}

######################
# Location classes
######################


class ManualLocation(Location):
    game = "Manual"