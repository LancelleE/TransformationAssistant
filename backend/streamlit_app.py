import streamlit as st
import pandas as pd
from backend.DATA import Data
from backend.LLM import LLM_OpenAI, LLM_Mistral

def app(openai_key):
    st.title('Data Transformation Assistant')
    with st.sidebar:
        dataset = st.file_uploader(label = 'Upload your dataset', accept_multiple_files=False, type=['csv','txt'])
        additional_informations = st.text_area('What additional information would you like to provide ?', placeholder='Type here...')

    if dataset:
        with st.expander("See dataset snippet"):
            data = Data(dataset=pd.read_csv(dataset), filename=dataset.name)
            st.write(data.dataset.head(5))

        transformation_instructions = st.text_area(
            label='Provide here the transformation needed on the dataset.',
            placeholder='Type here...',

        )

        if st.button(label='Compute'):
            context = f"""
                            Act as a Python developer. I will provide you with a dataset along with its main metadata. Additionally, I will give you a list of transformations that I need to be applied to the dataset.

                            Your task is to write Python code that performs these transformations. Use basic libraries such as numpy, pandas, or polars. Remember to include comments in your code explaining each step.
                            You don't need to import the data, since it is already loaded in the Python environment. Data is stored as a pandas DataFrame, in the object : data.dataset.

                            Dataset Metadata:
                            - Describe the dataset briefly (e.g., its structure, columns, size).
                            - Provide any relevant information about the dataset's format (e.g., CSV, Excel).

                            Transformations List:
                            - Clearly state each transformation required, including any conditions or filters to be applied.
                            - Specify the desired output or format after each transformation.

                            Please return only the Python code necessary to perform the transformations. Don't return the Python balise.
                    """
            
            prompt = f"""
                            The input filename is {data.filename}.\n
                            It is constituted by these features : {data.var_type()}.\n
                            Additional informations on the dataset : {additional_informations}.\n
                            Transformations needed : {transformation_instructions}
                    """

            model = LLM_OpenAI(openai_key)
            answer = model.get_completion(context, prompt)
            exec(answer[9:len(answer)-3])
            st.write(data.dataset)
            st.write(answer)