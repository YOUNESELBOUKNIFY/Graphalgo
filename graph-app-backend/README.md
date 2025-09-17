
# crée un environnement virtuel
- python -m venv venv
# active l’environnement virtuel
- .\venv\Scripts\Activate.ps1
# install requerment
- pip install -r requirements.txt 
# lancement de API
- uvicorn app.main:app --reload
