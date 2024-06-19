import streamlit as st
import os
from llama_index.core import Document, VectorStoreIndex, ServiceContext
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader

import logging

# Set up logging
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

os.path.dirname(__file__) # relative directory path

st.set_page_config(page_title="AI Chatbot", 
                   initial_sidebar_state="expanded",
                   page_icon="🤖"
                   )

# Change Theme
ms = st.session_state
if "themes" not in ms: 
  ms.themes = {"current_theme": "light",
                    "refreshed": True,
                    
                    "light": {"theme.base": "dark",
                              "theme.backgroundColor": "gray",
                            #   "theme.primaryColor": "#70798c",
                            #   "theme.secondaryBackgroundColor": "#989898",
                            #   "theme.textColor": "white",
                              "button_face": "🌜"},

                    "dark":  {"theme.base": "light",
                              "theme.backgroundColor": "white",
                            #   "theme.primaryColor": "#70798c",
                            #   "theme.secondaryBackgroundColor": "#e1e5ee",
                            #   "theme.textColor": "#black",
                              "button_face": "🌞"},
                    }

def ChangeTheme():
  previous_theme = ms.themes["current_theme"]
  tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
  for vkey, vval in tdict.items(): 
    if vkey.startswith("theme"): st._config.set_option(vkey, vval)

  ms.themes["refreshed"] = False
  if previous_theme == "dark": ms.themes["current_theme"] = "light"
  elif previous_theme == "light": ms.themes["current_theme"] = "dark"


btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
st.button(btn_face, on_click=ChangeTheme)

if ms.themes["refreshed"] == False:
  ms.themes["refreshed"] = True
  st.rerun()

# Display logo 
st.columns(3)[1].image('images/BuyBuddy-logo.png', caption=None,width=250)

# Access the API keys from environment variables
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Display Sidebar for settings and navigation
# sets up sidebar nav widgets
with st.sidebar:   
    st.markdown("# Chat Options")
    # widget - https://docs.streamlit.io/library/api-reference/widgets/st.selectbox

    # models - https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
    model = st.selectbox('What model would you like to use?',('gpt-3.5-turbo-16k','gpt-3.5-turbo', 'gpt-4'))
    
    # https://docs.streamlit.io/library/api-reference/widgets/st.number_input
    temperature = st.slider('Temperature', value=0.1, min_value=0.0, max_value=1.0, step=0.1, 
                            help="The temperature setting to be used when generating output from the model.")
    
    max_token_length = st.number_input('Max Token Length', value=500, min_value=200, max_value=3000, step=100, 
                                    help="Maximum number of tokens to be used when generating output.")

# Define the chatbot function
def show_chatbot():

    if "messages" not in st.session_state.keys():  # Initialize the chat message history
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Ask me a question about BestBuy products!",
            }
        ]

    @st.cache_resource(show_spinner=False)
    def load_data():
       
        with st.spinner(text="Loading and indexing the docs – hang tight! This should take 1-2 minutes."):
            reader = SimpleDirectoryReader(input_dir="data", recursive=True)
            docs = reader.load_data()

            # Service context 
            service_context = ServiceContext.from_defaults(
                llm=OpenAI(
                    model=model, 
                    temp=temperature, 
                    max_tokens=max_token_length,
                    system_prompt="""You are BuyBuddy, an AI-powered Customer Service assistant Chatbot for online customers. 
                    Your users are asking questions about products sold on BestBuy and some documents are provided for you about products sold on https://www.bestbuy.com/
                    Your primary function is to extract details from product manuals and to provide accurate product information, setup instructions, troubleshooting help, and recommend compatible products that meet the customer's requirements.
                    You will be shown the user's question, and the relevant information from the BestBuy informative materials. 
                    Answer the user's question using only this information.
                    Answer using bullet points and include technical information.
                    Dimentions are: width, dept.
                    Remeber to recommend users to buy the products at BestBuy store and website https://www.bestbuy.com/ or stop to a Geek Squad for technical assistance.
                    If you don't know the answer, just say you don't know and to contact BestBuy support or visit the website https://www.bestbuy.com/ .
        
                    When assisting a customer, always be efficient, patient, knowledgeable, friendly, and detail-oriented. 
                    Your communication style should be clear, concise, and focused on providing relevant information promptly.
                    Remember, your goal is to enhance the customers experience by providing relevant and helpful information promptly. 

                    When recomending products provide at least 3 options of various prices for the customer to choose from and provide in the answer short product description and some detials like dimentions, weight, price, URL.
                    When asked about product features, provide detailed yet straightforward descriptions, highlighting key specifications, benefits, price and URL.
                    When asked about setup instructions, provide step-by-step guidance to ensure the customer can easily follow and complete the setup process or stop at a local BestBuy or Geek Squad for technical assistance.
                    When asked about troubleshooting, offer practical, step-by-step solutions to resolve common issues effectively or stop at a local BestBuy or Geek Squad for technical assistance.

                    When answering questions make sure to don't truncate the answers and continue until the end of the sentence.

                    Answer in the user's question language for eaxple: English, French, Italian, Romanian etc.
                    """,
                )
            )

            # Create a VectorStoreIndex from the list of documents
            index = VectorStoreIndex.from_documents(docs, service_context=service_context)
            return index

    index = load_data()

    # Create the chat engine
    if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=False)

    if prompt := st.chat_input(
        "Ask me a question about BestBuy products here..."
    ):  # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:  # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(
                    message
                )  # Add response to message history

show_chatbot()