from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "abc123"
TOKEN = "token"
user_params = {
    "token": "token",
    "username": "ptesting977",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Create new Pixela Account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph2",
    "name": "Hours of Learning Coding",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# Create new Graph
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
pixel_endpoint = f"{graph_endpoint}/graph2"
quantity = input("Hours learned today?: ")
pixel_config = {
    "date": formatted_date,
    "quantity": quantity,
}

# recording new data
response = requests.post(
    url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

modify_pixel_endpoint = f"{pixel_endpoint}/{formatted_date}"

modify_config = {
    "quantity": "4.5",
}
