from typing import Dict

import requests
from decouple import config


def get_models_response() -> Dict:
    response_data = requests.get(
        "https://api.openai.com/v1/models",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config('OPENAI_API_KEY')}",
        },
    ).json()
    return response_data


if __name__ == "__main__":
    response = get_models_response()
    print(response)
