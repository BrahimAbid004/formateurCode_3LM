from fastapi import APIRouter
from schemas import ChatRequest
from services import obtenir_reponse_tuteur

# Creation d'un sous-routeur. Le prefix indique que toutes les routes ici commenceront par /tutor
router = APIRouter(
    prefix="/tutor",
    tags=["Agent Tuteur"]
)


@router.post("/chat")
async def chat_avec_tuteur(requete: ChatRequest):
    
    texte_pdf_simule = "C'est la formation en programmation Python. Il couvre les bases de la syntaxe, les structures de données, et les concepts de programmation orientée objet."
    
    historique_court = requete.historique[-5:]
    
    try:
        # On délègue le travail complexe à notre service
        reponse_ia = obtenir_reponse_tuteur(
            question=requete.question,
            historique_court=historique_court,
            texte_pdf=texte_pdf_simule
        )
        return {"reponse": reponse_ia}
        
    except Exception as e:
        return {"erreur": f"Impossible de contacter le tuteur IA : {str(e)}"}