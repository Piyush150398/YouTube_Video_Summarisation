#library
import re
from logging_info import logging_setup


logger = logging_setup()

def get_video_id_from_url(url):
    try:
        pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/.*[?&]v=|youtu\.be\/)([^#\n]+)'
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
    except Exception as e:
        logger.error(f"Having following issue in get_video_id_from_url function - {e}")
    return video_id
