from dotenv import dotenv_values
import backend.streamlit_app as streamlit_app
CONFIG = dotenv_values(".env")

if __name__ == '__main__':
    streamlit_app.app(openai_key=CONFIG['OPENAI_API_KEY'])