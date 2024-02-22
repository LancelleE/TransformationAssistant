from dotenv import dotenv_values
from backend.LLM import LLM_Mistral
from backend.streamlit_app import app
CONFIG = dotenv_values(".env")

if __name__ == '__main__':
    model = LLM_Mistral(CONFIG['MISTRAL_API_KEY'])
    app()