from pydantic import BaseModel
from typing import List
#Modele d un message dans l historique
class Message(BaseModel):
    role: str
    content: str
#Modele d une requete complete
class ChatRequest(BaseModel):
    id_formation: str
    question: str
    historique: List[Message]=[]