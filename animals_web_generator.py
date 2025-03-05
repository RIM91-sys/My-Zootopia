import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def generate_animal_info(data):
    """Generates a formatted string for the animals' information."""

    output = ""

    for animal in data:
        if 'name' not in animal or 'diet' not in animal['characteristics'] or 'type' not in animal['characteristics'] or 'locations' not in animal:
            continue  # Skip animals missing required fields

        output += f"Name: {animal['name']}\n"

        if 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}\n"

        if isinstance(animal['locations'], list) and animal['locations']:
            output += f"Location: {animal['locations'][0]}\n"

        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"

        output += " " * 30 + "\n"  # Separator for readability

    return output



def create_html_file(template_path, output_path, animals_info):
    """ Generates an HTML file replacing the placeholder with the animal data """
    with open(template_path, "r") as file:
        html_content = file.read()

    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_path, "w") as file:
        file.write(new_html_content)

animals_data = load_data("animals_data.json")

animals_info = generate_animal_info(animals_data)

create_html_file("animals_template.html", "animals.html", animals_info)
print(animals_info)