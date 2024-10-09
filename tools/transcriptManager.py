from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from pytube import YouTube
import logging

def load_documents(link):
    try:
        # First, try to get the video title to check if the video is accessible
        yt = YouTube(link)
        yt.check_availability()
        
        loader = YoutubeLoader.from_youtube_url(
            link,
            add_video_info=True,
            language=["en", "id", "hi"],
            translation="en",
        )
        return loader.load()
    except Exception as e:
        logging.error(f"Error loading YouTube video: {str(e)}")
        return []  # Return an empty list if there's an error

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)
