import json

# Function to import JSON data
def require_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data