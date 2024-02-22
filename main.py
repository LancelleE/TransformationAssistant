from dotenv import dotenv_values
from backend.LLM import LLM_Mistral
from backend.streamlit_app import app
CONFIG = dotenv_values(".env")

if __name__ == '__main__':
    print(CONFIG['MISTRAL_API_KEY'])
    model = LLM_Mistral(CONFIG['MISTRAL_API_KEY'])
    context = 'You say hello'
    prompt = 'My name is Etienne'
    print(model.get_completion(context, prompt))
    app()