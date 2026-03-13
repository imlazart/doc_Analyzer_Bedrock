import streamlit as st
import boto3
#import json


KB_ID = "TLVUXRKVJF"

bedrock_agent = boto3.client("bedrock-agent-runtime",region_name="us-east-1")

def ask_bedrock(question):

    response = bedrock_agent.retrieve_and_generate(
        input={"text": question},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KB_ID,
                "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-haiku-20240307-v1:0"
            }
        }
    )

    return response["output"]["text"]

st.title("AI Document Analyzer")
question = st.chat_input("Ask about the document")

if question:

    answer = ask_bedrock(question)

    st.chat_message("user").write(question)
    st.chat_message("assistant").write(answer)