from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

##TODO: create sqlite3 DB connection to import user_bios in forms [name:bios]
user_bios = {}

names = list(user_bios.keys())
bios = list(user_bios.values())
embeddings = model.encode(bios)

similarity_matrix = cosine_similarity(embeddings)

def show_matches(name, top_n=3):
    idx = names.index(name)
    scores = similarity_matrix[idx]
    matches = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
    matches = [(n,s) for n,s in matches if n!=name][:top_n]
    
    print(f"\nTop matches for {name}:")
    for n,s in matches:
        print(f"{n}: {s}")

for n in names:
    show_matches(n)