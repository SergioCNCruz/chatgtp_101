from typing import Dict

from decouple import config
import openai


def get_whisper_response(path: str) -> Dict:
    with open(path, "rb") as audio_file:
        openai.api_key = config("OPENAI_API_KEY")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript


if __name__ == "__main__":
    response = get_whisper_response(
        path=f"./{config('TEST_FILE_AUDIO_PATH')}"
    )
    print(response["text"])
