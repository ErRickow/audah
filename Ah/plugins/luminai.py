async def luminer(messagestr):
    url = "https://lumin-ai.xyz/"
    response = requests.post(url, json={"content": content})
    if response.status_code != 200:
        return None
    return response.json()