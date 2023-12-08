import requests as req


list_url = "https://172.20.10.12:8000/names"


start = input("Would you like to: \n"
              "1 - Get a list of 20 people and their favorite games\n"
              "2 - Get the details for each person\n"
              ">> ")
on = True

while on:
    if start == "1":
        url = "http://172.20.10.12:8000/names?api_key=pnmnyyyyss"
        response = req.get(url=url)
        json_data = response.json()
        print(json_data)
    elif start == "2":
        name = input("Which person would you like to get details on?\n"
                     ">> ")
        url = f"http://172.20.10.12:8000/names/{name}?api_key=pnmnyyyyss"
        response = req.get(url=url)
        json_data = response.json()
        print(json_data)

    is_done = input("Is that all? yes/no\n"
                    ">> ")
    if is_done == "y" or is_done == "Y":
        on = False
