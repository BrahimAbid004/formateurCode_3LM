from fastapi import FastAPI
from dotenv import load_dotenv

# 1. Charger les variables d'environnement EN PREMIER (crucial pour que le service lise la clé)
load_dotenv()

# 2. Importer le routeur (après le load_dotenv)
from routers import tutor

# 3. Initialiser FastAPI
app = FastAPI(
    title="Plateforme de Formation - Agent Tuteur API",
    description="API permettant de discuter avec un agent IA sur la base d'un cours PDF."
)

# 4. Connecter le routeur à l'application
app.include_router(tutor.router)