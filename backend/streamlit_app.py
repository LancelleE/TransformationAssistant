import streamlit as st
import pandas as pd
from backend.DATA import Data

def app():
    st.title('Data Transformation Assistant')
    with st.sidebar:
        dataset = st.file_uploader(label = 'Upload your dataset', accept_multiple_files=False, type=['csv','txt'])
        additional_informations = st.text_input('What additional information would you like to provide ?', placeholder='Type here...')

    if dataset:
        with st.expander("See dataset snippet"):
            data = Data(pd.read_csv(dataset))
            st.write(data.dataset.head(5))

        transformation_instructions = st.text_input(
            label='Provide here the transformation needed on the dataset.',
            placeholder='Type here...'
        )

        
    
    
