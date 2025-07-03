from google import genai
from google.genai import types
from service.barista import BaristaService
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def load_prompt():
    with open("agent/prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

COFFEE_BOT_PROMPT = load_prompt()

barista_service = BaristaService()

ordering_system = [
    barista_service.add_to_order,
    barista_service.get_order,
    barista_service.remove_item,
    barista_service.clear_order,
    barista_service.place_order,
]
model_name = "gemini-2.5-flash"  #["gemini-2.5-flash-lite","gemini-2.5-flash","gemini-2.5-pro"]

chat = client.chats.create(
    model=model_name,
    config=types.GenerateContentConfig(
        tools=ordering_system,
        system_instruction=COFFEE_BOT_PROMPT,
    ),
)

placed_order = []
order = []