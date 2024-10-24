import requests

URL = f"https://www.themealdb.com/api/json/v1/1/search.php?s=Biryani"

response = requests.get(URL)

meal = input("Please enter meal name: ")

