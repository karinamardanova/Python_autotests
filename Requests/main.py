# Создание питомца

import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 100,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "karina",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


# Смена имени питомца

import requests

response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 100,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "vasilisa",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

# Нахождение пета по ID

import requests

response = requests.get("https://petstore.swagger.io/v2/pet/100")
print(response.text)