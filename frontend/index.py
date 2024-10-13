import streamlit as st
import requests
import logging
from streamlit_lottie import st_lottie
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="Podcast AI", page_icon="🤖", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 1.5rem;
    }
    
    .stButton>button {
        width: 100%;
        height: 3.5rem;
        font-size: 1.2rem;
        font-weight: 600;
        background-color: #1E88E5;
        color: white;
        border: none;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #1565C0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #D3D3D3;  /* Light grey background */
        color: #333;  /* Dark text color for contrast */
        border: 1px solid #A9A9A9;  /* Darker border for definition */
        border-radius: 5px;
        padding: 0.5rem;
        font-size: 1.1rem;
    }
    
    .response-container {
        background-color: #F5F5F5;
        border-left: 5px solid #1E88E5;
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# API endpoint
API_ENDPOINT = "https://magical-famous-emu.ngrok-free.app"
API_TIMEOUT = 60
# Load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
lottie_animation = load_lottieurl(lottie_url)

# Query Page

def query_page():
    st.markdown("<h2 class='section-title'>Ask a Question</h2>", unsafe_allow_html=True)
    query = st.text_area("Enter your query", height=150)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Submit", key='submit_query'):
            if query:
                with st.spinner("Processing your query..."):
                    try:
                        response = requests.get(f"{API_ENDPOINT}/ask", params={"userQuery": query}, timeout=API_TIMEOUT)
                        response.raise_for_status()
                        st.success("Query processed!")
                        st.markdown("<div class='response-container'>", unsafe_allow_html=True)
                        st.markdown("### Response:")
                        st.markdown(response.text)
                        st.markdown("</div>", unsafe_allow_html=True)
                        logger.info(f"Query processed successfully: {query}")
                    except requests.RequestException as e:
                        st.error(f"An error occurred: {str(e)}")
                        logger.error(f"Error processing query: {str(e)}")
            else:
                st.warning("Please enter a query before submitting.")

def post_page():
    st.markdown("<h2 class='section-title'>Share a YouTube Video</h2>", unsafe_allow_html=True)
    youtube_link = st.text_input("Enter YouTube Link")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Share", key='share_video'):
            if youtube_link:
                with st.spinner("Processing your video..."):
                    try:
                        response = requests.get(f"{API_ENDPOINT}/post", params={"youtubeLink": youtube_link}, timeout=API_TIMEOUT)
                        response.raise_for_status()
                        st.success("Video processed!")
                        st.markdown("<div class='response-container'>", unsafe_allow_html=True)
                        st.markdown("### Response:")
                        st.markdown(response.text)
                        st.markdown("</div>", unsafe_allow_html=True)
                        logger.info(f"Video processed successfully: {youtube_link}")
                    except requests.RequestException as e:
                        st.error(f"An error occurred: {str(e)}")
                        logger.error(f"Error processing video: {str(e)}")
            else:
                st.warning("Please enter a YouTube link before sharing.")


# Main App
def main():
    st.markdown("<h1 class='main-title'>Podacst AI🎧</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2,1])
    with col1:
        option = st.radio("Choose an option:", ("Ask a Question", "Share a Video"))
    with col2:
        st_lottie(lottie_animation, height=200, key="lottie")

    if option == "Ask a Question":
        query_page()
    else:
        post_page()

    # Add a footer
    st.markdown("---")
    st.markdown("Created with ❤️ by Ansuman")

if __name__ == "__main__":
    main()