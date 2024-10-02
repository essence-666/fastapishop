from items.schemas import Item

def create_item(item : Item):
    return {
        "status" : "succsess",
        "message" : f'item {item.item_name} was succsessfully added',
        "item" : item.model_dump()
    }