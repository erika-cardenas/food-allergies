from os import name
import weaviate
import json

client = weaviate.Client("https://food-allergies.semi.network")


if client.is_ready():
  
  with open('data.json', 'r') as f:
    data = json.load(f)


  client.batch.configure(
    batch_size=100, 
    dynamic=True,
    timeout_retries=3,
    callback=None,
  )

  for allergy in data["FoodAllergies"]:
    print("importing allergies ", allergy.get("allergy", None))

    properties = {
      "name": allergy["name"],
      "age": int(allergy["age"]),
      "allergy": allergy.get("allergy", None)
    }

    client.batch.add_data_object(properties, "FoodAllergies")
  
  client.batch.flush()



else:
  print("The Weaviate cluster is not connected.")