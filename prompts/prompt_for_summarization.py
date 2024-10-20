Task = """Your task is to summarise the YouTube video transcript."""

context = """I have provided you the transcipt for that particular video as "###INPUT-TEXT"."""

persona = """- Summarisation should be very perfect and accurate. Should not miss any points.
             - Highlight the most important points from the transcript as key points at last."""

format = """- Output format should be in bullet points."""

prompt = """
###TASK
{}

###CONTEXT
{}

###PERSONA
{}

###OUTPUT-FORMAT
{}

###INPUT-TEXT
{}
"""