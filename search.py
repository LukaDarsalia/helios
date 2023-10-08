import os
import openai
from sklearn.metrics.pairwise import cosine_similarity
api_key = ""


openai.api_key = os.getenv(api_key)
def get_embeddings(query):
    response = openai.Embedding.create(
        input=query,
        model="text-embedding-ada-002",
        api_key = api_key
    )
    embeddings = response['data'][0]['embedding']
    return embeddings

def sort_embeddings(query:str, list_of_queries : list):
    emb = get_embeddings(query)
    all_embeddings = [get_embeddings(i) for i in list_of_queries]
    similarities = [cosine_similarity([emb], [e])[0][0] for e in all_embeddings]
    result = []
    for i in range(len(similarities)):
        if similarities[i] > 0.8:
            result.append(list_of_queries[i])
    return result
data = {
    "NASA_Researcher": {
        "UX/UI_Design": {
            "Description": "At NASA, we are pushing the boundaries of human understanding and expanding our reach into the cosmos. To support this mission, we are searching for seasoned UX/UI designers ready to step into the vastness of space exploration through design.",
            "Role": "You will be instrumental in conceptualizing and executing interfaces for groundbreaking applications, ensuring they are both user-friendly and optimized for the unique challenges of space research."
        },
        "Data_Scientist/ML_Engineer": {
            "Description": "As we delve deeper into the mysteries of our universe, the importance of data cannot be overstated. NASA is currently looking for data scientists and ML engineers to collaborate on pioneering space research projects.",
            "Role": "Your expertise will help us decipher vast and complex cosmic datasets, uncover patterns, and derive insights which could reshape our understanding of the universe."
        },
        "Electrical_Engineers": {
            "Description": "The complexity of space missions demands the very best in electrical engineering. We at NASA are in search of adept electrical engineers ready to take on the grand challenges of space exploration.",
            "Role": "Your role would involve crafting, refining, and troubleshooting sophisticated electrical systems tailored for the harsh environment of space."
        }
    },
    "Collaborator": {
        "UX/UI_Design": {
            "Motivation": "Space has always ignited my imagination, and my background in UX/UI design equips me to translate that passion into tangible interfaces.",
            "Intent": "I wish to collaborate with NASA on its open science projects, bringing a fresh perspective to the design of interactive platforms."
        },
        "Data_Scientist/ML_Engineer": {
            "Motivation": "Diving into vast datasets and unveiling patterns is where my strengths lie, and the prospect of doing so with the cosmic data from NASA's open science projects thrills me.",
            "Intent": "Collaborating with NASA would provide an opportunity to employ advanced algorithms in the context of space exploration, contributing to our collective understanding of the universe."
        },
        "Electrical_Engineer": {
            "Motivation": "Space exploration presents unique challenges that demand innovative engineering solutions. With a rich background in electrical engineering, I'm keen on collaborating with NASA's open science projects.",
            "Intent": "I envision designing resilient electrical systems capable of withstanding the rigor of space, ensuring our experiments and missions continue unhindered."
        }
    }
}
q = "i am a Machine learning enginner who wants to help a researcher develop several algorithms"
descriptions = [role_data["Description"] for role_data in data["NASA_Researcher"].values()]
res = sort_embeddings(q, descriptions)
print("QUERY:")
print(q)
print()
print()
print()
print("RESULT: ")
print(res)

