import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve API Key and Base URL
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animal data for the given 'animal_name' from the API.
    Returns:
        A list of animals (each animal is a dictionary), or an empty list if the API call fails.
    """
    if not API_KEY:
        print("Error: API key is missing! Please check your .env file.")
        return []

    url = f'{BASE_URL}?name={animal_name}'

    try:
        response = requests.get(url, headers={'X-Api-Key': API_KEY})

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Return the JSON data

        # Handle different types of errors
        else:
            print(f"Error fetching data for {animal_name} (Status Code: {response.status_code})")
            print(f"Response: {response.text}")  # Print API error message for debugging
            return []

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []  # Return empty list in case of a network failure

