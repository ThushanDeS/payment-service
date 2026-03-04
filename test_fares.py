import requests

response = requests.get("http://localhost:5003/api/fares/")
print(f"Status: {response.status_code}")
fares = response.json()['fares']
print(f"Total fares: {len(fares)}")
print("\nSample fares:")
for fare in fares[:5]:
    print(f"  - Flight {fare['flight_id']}: ${fare['total']} ({fare['fare_class']})")
