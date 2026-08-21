import json

with open("calgary_traffic_incidents.json", "r") as f:
    data = json.load(f)

unique_data = list({json.dumps(item): item for item in data}.values())