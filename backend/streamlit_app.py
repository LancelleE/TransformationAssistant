import streamlit as st
import pandas as pd
from backend.DATA import Data

def app():
    st.title('Salut !')
    st.write('Ma première app !')
    with st.sidebar:
        dataset = st.file_uploader(label = 'Upload your dataset', accept_multiple_files=False, type=['csv','txt'])
        data = Data(pd.read_csv(dataset))
        additional_informations = st.text_input('What additional information would you like to provide ?')

    if dataset:
        st.write(data.dataset)
    
    
