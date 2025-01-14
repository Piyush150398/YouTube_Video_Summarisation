### YouTube Video Summarization 🎥
This project provides a YouTube video summarization tool that leverages the ChatGPT-4o-mini model to generate concise summaries from YouTube videos. The project uses the youtube_transcript_api to extract video transcripts and presents the summary through a user-friendly Streamlit interface.

### Features ✨
1) Extracts transcripts from YouTube videos using youtube_transcript_api.
2) Generates summaries using the ChatGPT-4o-mini API.
3) Streamlit-based web interface for ease of use.
4) Provides error handling and success messages to improve user experience.

### Project Structure 📁

	YOUTUBE_VIDEO_SUMMARY/
	│
	├── models/
	│   └── youtube_transcript_model.py      # Handles transcript operations.
	├── prompts/
	│   └── prompt_for_summarization.py      # Stores prompts for ChatGPT-4o-mini API.
	├── logs/                                # Logs for monitoring errors and usage.
	├── .env                                 # Environment variables (API keys, etc.).
	├── Invoke_OpenAI.py                     # Manages API interactions with GPT-4o-mini.
	├── logging_info.py                      # Configures logging settings.
	├── regular_expression_to_get_id.py      # Extracts YouTube video ID from URLs.
	├── run.py                               # Main entry point for the project.
	├── streamlit_app.py                     # Streamlit web app for video summarization.
	├── youtube_transcript_api_call.py       # API call logic for fetching transcripts.
	└── README.md                            # Project documentation (this file).


### Prerequisites 🛠️
	Ensure you have the following installed:
	Python 3.8+
	Streamlit
	OpenAI Python API (openai package)
	youtube-transcript-api (youtube_transcript_api package)

### Environment Setup ⚙️
	Create a .env file to store API keys:
    OPENAI_API_KEY=your_openai_api_key_here
    Install the necessary Python packages.

### How to Run 🚀
	Start the Streamlit app:
	streamlit run streamlit_app.py
	Paste the YouTube video URL into the input field and click "Submit".
	Wait for the video transcript to be fetched and summarized.

### Dependencies 📦
	OpenAI API for text summarization.
	youtube-transcript-api for fetching transcripts.
	Streamlit for the user interface.
### Example Usage 🎯
Step-1) Enter a valid YouTube URL (e.g., https://www.youtube.com/watch?v=abc123).

Step-2) Press enter key and click on submit button.

Step-3) Wait for few seconds and you will have summary.

### Future Improvements 🚀
1) Add support for multiple languages.
2) Improve summary accuracy with more context-specific prompts.
3) Save transcripts and summaries locally for offline access.
### Author 💻
	Developed by [Piyush Sonawane].
