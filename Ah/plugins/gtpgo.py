import requests

async def tanya(text):
  url = "https://widipe.com/gptgo"
  text = "resep seblak yang gurih kuah kare"
  params = {'text': text}
  headers = {'accept': 'application/json'}
  response = requests.get(url, headers=headers, params=params)
  data = response.json()
  if 'result' in data:
    return data['result'])
else:
    return f"{response.text}"