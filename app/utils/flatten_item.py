def flatten_item_data(item):
    """
    This function flattens the item data by removing the nested structure of the item.
    """
    item_data = {
        "item_id": item["item_id"],
        "name": item["name"],
        "ingredients": ", ".join(item["ingredients"]),
        "nutrient_description": item["nutrient_description"],
        "description": item["description"],   
    }
    
    for key, value in item["nutrients"].items():
        item_data[key] = value["value"]
        item_data[f"{key}_unit"] = value["unit"]

    return item_data