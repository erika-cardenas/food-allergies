from os import name
import weaviate
import json

client = weaviate.Client("https://food-allergies.semi.network")


if client.is_ready():
  
  data_file = open('data.json')
  data = json.load(data_file)
  data_file.close()

  client.batch.configure(
    batch_size=100, 
    dynamic=True,
    timeout_retries=3,
    callback=None,
  )

  for allergy in data["FoodAllergies"]:
    print("importing allergies ", allergy.get("allergy"))

    properties = {
      "name": allergy["name"],
      "age": int(allergy["age"]),
      "allergy": allergy.get("allergy", None)
    }

    client.batch.add_data_object(properties, "FoodAllergies")
  
  client.batch.flush()



else:
  print("The Weaviate cluster is not connected.")