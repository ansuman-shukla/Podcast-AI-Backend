
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 12,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def final_response(response):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    generation_config=generation_config,
      safety_settings={
          HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
          HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
      }
    )
    
    chat_session = model.start_chat(
        history=[
        ]
    )

    response = chat_session.send_message(f"{response}  use every bit of given resource to come up with a information dense  output also don't missout any important point,OVERSHARING is OK")
    return response.text
    # print(response.text)
