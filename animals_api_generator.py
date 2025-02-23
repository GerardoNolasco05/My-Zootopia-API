import json
import requests

API_KEY = '/EmMQfLDmjxUCotWswgwRA==v88dotSfqCvJuO9T'
ANIMAL_NAME = 'Fox'


def load_animal_data():
    """Load the animals_template.html file and return its content."""
    with open("animals_template.html", "r", encoding="utf-8") as file:
        return file.read()


def animal_content(animals_data):
    """Generate HTML list items for animals."""
    output = []

    for animal in animals_data:
        output.append(f'''
        <li class="cards__item">
            <div class="card__title">{animal["name"]}</div>
            <p class="card__text">
                <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>
                <strong>Location:</strong> {animal["locations"][0]}<br/>
                {(
            f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>'
            if "type" in animal["characteristics"]
            else ""
        )}
            </p>
        </li>
        ''')

    return "\n".join(output)


def generate_animal_html(template, animals_data):
    """Insert animal data into the HTML template."""
    animal_info_html = animal_content(animals_data)
    return template.replace("__REPLACE_ANIMALS_INFO__", animal_info_html)


def save_html(filename, content):
    """Save the given content to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def fetch_animal_data(name):
    """Fetch data from the API based on the animal's name."""
    url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(url, headers={'X-Api-Key': API_KEY})

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON data
    else:
        print(f"Error fetching data for {name}: {response.status_code}")
        return []  # Return an empty list if the API call fails


def main():
    """Main function to process animal data and generate an HTML file."""
    # Fetch data for "Fox" from the API
    animals_data = fetch_animal_data(ANIMAL_NAME)

    if animals_data:  # If data is fetched successfully
        html_template = load_animal_data()
        updated_html = generate_animal_html(html_template, animals_data)
        save_html("animals.html", updated_html)
        print("HTML file generated successfully: animals.html")
    else:
        print(f"No data found for {ANIMAL_NAME}")


if __name__ == "__main__":
    main()
