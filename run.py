# Library
import os
from dotenv import load_dotenv
from logging_info import logging_setup
from youtube_transcript_api_call import get_transcript_from_url
from models.youtube_transcript_model import Youtube_Transcript
from Invoke_OpenAI import get_open_ai_response
from prompts.prompt_for_summarization import prompt,Task,context,format,persona

load_dotenv(override=True)
logger = logging_setup()

def main():
    url = os.getenv('YouTube_URL')
    if not url:
        logger.error("Error: 'YouTube_URL' environment variable is not set.")
        return
    video_transcript:Youtube_Transcript = Youtube_Transcript()
    video_transcript.transcript = get_transcript_from_url(url)

    transcript_prompt = prompt.format(Task,context,persona,format,video_transcript.transcript)
    response = get_open_ai_response(transcript_prompt)

    print(response)

if __name__ == "__main__":
    main()