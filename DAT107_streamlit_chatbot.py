import streamlit as st
from langchain.graphs import NeptuneGraph
from langchain.llms import Bedrock
from langchain.chains import NeptuneOpenCypherQAChain
from langchain_community.graphs import NeptuneAnalyticsGraph
from langchain.chat_models import BedrockChat

import boto3


bedrock_client = boto3.client('bedrock-runtime')
#get your graph_id first
graph = NeptuneAnalyticsGraph(graph_identifier="g-y5ki4mu2ga")
# connecting to LLM model - model need to be enabled first 
llm = BedrockChat(
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0",
    client = bedrock_client,
    model_kwargs={
        "temperature": 0,
        "top_k": 250,
        "top_p": 1,  
    }
)

extra_info=""" Holder Node represents the business or entity Each Holder node contains name and description attribute The id attribute of the Holder node represents the CIK value which is an SEC assigned identified 
HolderQuarter Node represents the quarter, the name represents the quarter (i.e. 2023Q2) and the id is a combination of the quarter and id value of the Holder Node 
has_holderquarter  Edge represents a fiscal quarter in which the Holder Node had reportable investments this egde connect to HolderQuarter Nodes.  
owns edge represents a security owned by a Holder in a HolderQuarter The edge contains quantity attribute and value attribute, which represents the number and value of the shares owned by the Holder Node in a HolderQuarter.
Holding Node represents the security owned by the Holder Node in the HolderQuarter. Holding Node contains a class attribute, type attribute, and name attribute.
"""

chain = NeptuneOpenCypherQAChain.from_llm(llm=llm, graph=graph,verbose=True,top_K=5,
               return_intermediate_steps=False, return_direct=False)

chain.extra_instructions = extra_info

st.title("LLM chat using Bedrock and Neptune")
st.title("EDGAR Data Model")
st.image('LOGO.jpg', caption='')


def generate_response(input_text):
    st.info(chain.invoke(input_text)['result'])

with st.form('my_form'): 
    text = st.text_area('Enter text:', 'who is the top 10 Holders where they have >$1B USD invested ?')
    submitted = st.form_submit_button('Submit 🦜🔗')
    generate_response(text)