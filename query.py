import weaviate
client = weaviate.Client("https://food-allergies.semi.network")

where_filter = {
    "path": "len(allergy)",
    "operator": "Equal",
    "valueInt": 0
}

query_result = (
  client.query
  .get("FoodAllergies", "name")
  .with_where(where_filter)
  .do()
)

print(query_result)
