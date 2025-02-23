import requests

# Define constants
API_KEY = '/EmMQfLDmjxUCotWswgwRA==v88dotSfqCvJuO9T'
BASE_URL = 'https://api.api-ninjas.com/v1/animals'

def fetch_data(animal_name):
    """
    Fetches the animal data for the animal 'animal_name' from the API.
    Returns: A list of animals, each animal is a dictionary:
    """
    url = f'{BASE_URL}?name={animal_name}'
    response = requests.get(url, headers={'X-Api-Key': API_KEY})

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the list of animals as JSON data
    else:
        print(f"Error fetching data for {animal_name}: {response.status_code}")
        return []  # Return an empty list if the API call fails
