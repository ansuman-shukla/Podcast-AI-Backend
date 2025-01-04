from pinecone import Pinecone
from langchain_community.retrievers import PineconeHybridSearchRetriever
from pinecone_text.sparse import BM25Encoder
import os
import nltk
# nltk.download('punkt_tab')
import dotenv
from pinecone import Pinecone,ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# index_name = "openai-large-embedding"
index_name = "curriculum-embeddings"



openai_api_key = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

dotenv.load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768,
        metric='dotproduct',
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
        )
else:
    print(f"Index {index_name} already exists.")

index = pc.Index(index_name)

# Instantiate the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
print(f"Creating embeddings...{embeddings}")

bm25encoder = BM25Encoder()
# print(f"Creating BM25 encoder...{bm25encoder}")

sentences = [
    "Apple is a tech company known for its iPhones and MacBooks.",
    "Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne.",
    "Apple was founded in Cupertino, California.",
    "Apple's headquarters is in Cupertino, California.",
    "Apple's first product was the Apple I, a computer designed by Steve Wozniak.",
]

bm25encoder.fit(sentences)

# bm25encoder.dump("bm25encoder.json")

