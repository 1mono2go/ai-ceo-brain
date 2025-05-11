import requests

def route_task(query, sensitivity):
    anakin_url = "https://api.anakin.ai/v1/apps/YOUR_APP_ID/run"
    response = requests.post(
        anakin_url,
        json={"query": query, "sensitivity_level": sensitivity},
        headers={"Authorization": "Bearer YOUR_ANAKIN_KEY"}
    )
    return response.json()["next_step"]
