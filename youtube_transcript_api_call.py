# libraries
import os
import asyncio
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from regular_expression_to_get_id import get_video_id_from_url
from logging_info import logging_setup


logger = logging_setup()

def get_transcript_from_url(url):
    try:
        video_id = get_video_id_from_url(url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en', 'hi']).fetch()

        video_transcript = ""
        for entry in transcript:
            video_transcript += entry['text']
        return video_transcript
    except TranscriptsDisabled:
        raise("Transcript is disable for this video.")
    except Exception as e:
        logger.error(f"Having following issue with get_transcript_from_url method - {e}")

    

