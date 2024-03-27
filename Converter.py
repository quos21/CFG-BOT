from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from py2cfg import CFGBuilder
import streamlit as st
from langchain.chains import LLMChain,SequentialChain
import os
key = os.environ.get('key')

template='''I want you to act as a code converter that converts a piece of code in from any language to Python. Please keep in mind that
            the control flow of the converted code should be same as the C code given.The code is {code}. Just output the required code,without any text above or below it.
            and also remove any comment in the code, just pure code.'''


st.title('CFG Bot')
text=st.text_input("give the code")

#prompt template

first_input_prompt=PromptTemplate(
    input_variables=['code'],
    template=template
)

#we initialize the llm now
llm = ChatOpenAI(openai_api_key=key)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='converted')

parent=SequentialChain(chains=[chain],input_variables=['code'],output_variables=['converted'],verbose=False)

if text:
    st.write(parent({'code':text}))
res=parent({'code':text})

file_name = "cfg.py"

# Write the contents of TEXT into the Python file
try:
    with open(file_name, "w") as file:
        file.write(res['converted'])
except SyntaxError:
    st.error('Enter some text')
except KeyError:
    st.error('Enter valid code')

# def read_pdf(file_path):
#     with open(file_path, "rb") as file:
#         pdf_bytes = file.read()
#         st.write(pdf_bytes)

cfg = CFGBuilder().build_from_file('Control Flow Grapg', 'cfg.py')
cfg.build_visual('CFG', 'pdf')
