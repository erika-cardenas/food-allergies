import weaviate
import json

client = weaviate.Client("https://food-allergies.semi.network")

class_obj = {
    "class": "FoodAllergies", 
    "description": "Properties include people and potential allergy",
    "invertedIndexConfig": {
    "IndexNullState": True,         
    "IndexPropertyLength": True
    },
    "properties": [
        {
            "name": "name",
            "dataType": ["string"],
            "description": "Name of people",
        },
        {
            "name": "allergy",
            "dataType": ["string[]"],
            "description": "Type of allergy",
        }
    ]
}

# resetting the schema 
client.schema.delete_all()

# add the schema
client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))