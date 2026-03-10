import chromadb
from sentence_transformers import SentenceTransformer

# load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# initialize chromadb
client = chromadb.Client()

collection = client.get_or_create_collection(name="paraphrases")


def store_sentence(original, paraphrased):

    embedding = embedding_model.encode(original).tolist()

    collection.add(
        documents=[paraphrased],
        embeddings=[embedding],
        ids=[original]
    )


def search_similar(sentence):

    embedding = embedding_model.encode(sentence).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    return results