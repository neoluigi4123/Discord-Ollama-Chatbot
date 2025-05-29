import csv
import ollama
import chromadb

MODEL="paraphrase-multilingual" # You actually need to install it: `ollama pull paraphrase-multilingual`

def load_dataset(n, user, query):
    input = f"{user} {query}"
    # Load documents from CSV
    documents = []
    with open("data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            documents.append(f"{row['user']} {row['content']}")

    # Create ChromaDB collection
    client = chromadb.Client()
    collection = client.create_collection(name="docs")

    # Embed and store each document
    for i, d in enumerate(documents):
        response = ollama.embed(model=MODEL, input=d)
        embeddings = response["embeddings"]
        collection.add(
            ids=[str(i)],
            embeddings=embeddings,
            documents=[d]
        )

    # Generate embedding for input and search relevant document
    response = ollama.embed(model=MODEL, input=input)
    results = collection.query(
        query_embeddings=[response["embeddings"][0]],
        n_results=n
    )
    data = results['documents'][0]
    return(data)