import requests
from decouple import config

from entities import RequestMessage, RequestPayload, ResponseData


def get_chatgpt_response(message: str) -> ResponseData:
    request_payload = RequestPayload(
        model="gpt-3.5-turbo", messages=[RequestMessage(role="user", content=message)]
    )
    response_data = requests.post(
        "https://api.openai.com/v1/chat/completions",
        data=request_payload.json(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config('OPENAI_API_KEY')}",
        },
    ).json()
    return ResponseData(**response_data)


if __name__ == "__main__":
    response = get_chatgpt_response(message="Tell me a joke")
    for choices in response.choices:
        print(choices.message.content)
