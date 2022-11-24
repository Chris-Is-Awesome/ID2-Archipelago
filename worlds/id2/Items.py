from Data import item_amounts, items, progression_items
from typing import Dict, NamedTuple

# Class for item
class ID2Item(NamedTuple):
	id: int
	progression: bool
	type: str

# Initialize empty dictionaries
item_table = {}
item_frequencies = {}

for i, (item_name, item_type) in enumerate(items.items()):
	# Add values to item_table based on contents in Data.py
	item_table[item_name] = ID2Item(id=i, progression=item_name in progression_items, type=item_type)
	# Determine item frequencies based on conntents in Data.py
	item_frequencies[item_name] = item_amounts[item_type]

# Tell Arch about the items
lookup_id_to_name: Dict[int, str] = {data.id: item_name for item_name, data in item_table.items() if data.id}

print(item_frequencies)