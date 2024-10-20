# library
import os
import openai
import logging
from dotenv import load_dotenv
from logging_info import logging_setup

logger = logging_setup()
load_dotenv(override=True)

def get_open_ai_response(prompt:str):
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500,
        top_p=1
        )
        return completion.choices[0].message.content
    except Exception as e:
        logger.log(logging.ERROR,f"Having following issue with get_open_ai_response method - {e}")
 

