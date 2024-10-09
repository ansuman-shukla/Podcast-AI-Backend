
from tools.transcriptManager import load_documents, split_documents
import logging
from database.retriverModel import retriever

logging.basicConfig(level=logging.INFO)

def embedder(link):
    documents = load_documents(link)

    if not documents:
        logging.error("No documents were loaded. Please check the YouTube link and try again.")
    else:
        chunk = split_documents(documents)
        logging.info(f"Number of chunks: {len(chunk)}")

        # Extract text content from each Document
        texts = [doc.page_content for doc in chunk]
        
        if texts:
            retriever.add_texts(texts)
            logging.info("Texts successfully added to the retriever.")
        else:
            logging.error("No text content found in the documents.")
