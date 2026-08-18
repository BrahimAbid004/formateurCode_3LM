import os
from google import genai
from google.genai import types
from schemas import Message
from typing import List

# 1. Initialisation du client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 2. Chargement du prompt
with open("prompt_systeme.txt", "r", encoding="utf-8") as file:
    PROMPT_SYSTEME = file.read()

# 3. Fonction métier dédiée
def obtenir_reponse_tuteur(question: str, historique_court: List[Message], texte_pdf: str) -> str:
    messages_gemini = []
    
    # Formatage de l'historique
    for msg in historique_court:
        role_google = "model" if msg.role == "assistant" else "user"
        messages_gemini.append({
            "role": role_google, 
            "parts": [{"text": msg.content}]
        })
        
    # Ajout du contexte
    message_utilisateur = (
        f"Voici le contenu du cours sur lequel tu dois te baser :\n"
        f"<cours>\n{texte_pdf}\n</cours>\n\n"
        f"Question de l'apprenant : {question}"
    )
    
    messages_gemini.append({
        "role": "user", 
        "parts": [{"text": message_utilisateur}]
    })
    
    # Appel à l'API
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages_gemini,
        config=types.GenerateContentConfig(
            system_instruction=PROMPT_SYSTEME
        )
    )
    
    return response.text