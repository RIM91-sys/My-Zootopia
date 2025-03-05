import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_animal_info(file_path):
    """Reads and prints required animal information"""
    animals_data = load_data(file_path)

    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "characteristics" in animal:
            print(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")
        if "characteristics" in animal:
            print(f"Type: {animal['characteristics']['type']}")

        print()


print_animal_info("animals_data.json")