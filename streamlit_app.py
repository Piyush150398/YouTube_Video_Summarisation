import streamlit as st
import markdown2
from models.youtube_transcript_model import Youtube_Transcript
from youtube_transcript_api_call import get_transcript_from_url
from Invoke_OpenAI import get_open_ai_response
from prompts.prompt_for_summarization import prompt,Task,context,format,persona

# Set the title for the app
st.title("YouTube Video Summarization 🎥")

url = st.text_input("Paste Your URL Here 🤠:")

# Check if the user has entered a URL
if url:
    if st.button("Submit"):
        st.success("URL submitted successfully!")
        try:
            video_transcript:Youtube_Transcript = Youtube_Transcript()
            video_transcript.transcript = get_transcript_from_url(url)

            with st.container():
                st.markdown("### YouTube video summarisation:")
                try:
                    transcript_prompt = prompt.format(Task,context,persona,format,video_transcript.transcript)
                    response = get_open_ai_response(transcript_prompt)
                    value=st.markdown(response)
                    st.success("Got the response successfully 🤑")
                except Exception as e:
                    st.error(f"No Response from OpenAI side 😨 - {e}")
            
        except Exception as e:
            st.error(f"Failed to retrieve transcript 😰: {e}")

        
else:
    st.warning("Please provide a valid URL.")
