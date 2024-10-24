#class Vehicle:
    def __int__(self, model, reg):
        self.model = model
        self.reg = reg  #whatever you write in this model in whcih whatever you write will be added
        print("A Vehicle is created")
    
    def display_details(self):
        print({model},{reg})
    def honk(self):
        print("Hoooonk!")


import requests
URL = "https://seas.gift.edu.pk/index.html"
response = requests.get(URL)
print(response.content)





