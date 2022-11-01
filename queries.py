import weaviate
client = weaviate.Client("https://food-allergies.semi.network/")

where_filter = {
    "path": ["allergy"],
    "operator": "Equal",
    "valueString": "Peanut"
}

query_result = (
  client.query
  .get("FoodAllergies", "allergy")
  .with_where(where_filter)
  .do()
)

print(query_result)