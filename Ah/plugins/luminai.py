async def chatgptold(messagestr):
    url = "https://lumin-ai.xyz/"
    payload = {"query": messagestr}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        return None
    return response.json()