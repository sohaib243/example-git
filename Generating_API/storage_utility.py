import json
import os

def load_books(filename):
    """
    Load books from json file
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as file:
        data = file.read()
    return json.loads(data)

def update_books(books: list, filename):
    """
    Update books in json file
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'w') as file:
        file.write(json.dumps(books, indent=4))  # Added indent for better readability
