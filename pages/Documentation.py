import streamlit as st 

from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# Set up logging
# logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def run():
    st.set_page_config(page_title="AI Chatbot", 
                   initial_sidebar_state="expanded",
                   page_icon="🤖"
    )
    st.write("# 👈 OpenAI Chatbot Demo!🌟")

    st.markdown(
        """
        ## Resources to continue learning:
        ### Learning and Documentation:
        - [OpenAI Cookbook](https://cookbook.openai.com/) -- Open-source examples and guides for building with the OpenAI API. Browse a collection of snippets, advanced techniques and walkthroughs.
        - [Quickstart tutorial - OpenAI API](https://platform.openai.com/docs/quickstart)
        - [DeepLearning.AI](https://www.deeplearning.ai/) -- Full specializations + many short 1-hour courses
        ### Tutorials:
        - [Streamlit Tutorials](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps) -- Build a basic LLM chat app
        - [Fine-Tuning OpenAI Models for Retrieval Augmented Generation (RAG) with Qdrant and Few-Shot Learning](https://github.com/openai/openai-cookbook/blob/main/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant.ipynb)
        - [Implementing RAG with Langchain and Hugging Face | by Akriti Upadhyay | Medium](https://medium.com/@akriti.upadhyay/implementing-rag-with-langchain-and-hugging-face-28e3ea66c5f7)
        - [How to parse PDF docs for RAG | OpenAI Cookbook](https://cookbook.openai.com/examples/parse_pdf_docs_for_rag)
        - [Parse PDF docs for RAG applications | OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/Parse_PDF_docs_for_RAG.ipynb)
        - [Retrieval-Augmented Generation (RAG): From Theory to LangChain Implementation | by Leonie Monigatti | Towards Data Science](https://towardsdatascience.com/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2)
        - [Streamlit Theme with a Toggle Button](https://discuss.streamlit.io/t/changing-the-streamlit-theme-with-a-toggle-button-solution/56842/1)
        - [Video - Streamlit-OpenAI-Chatbot](https://www.youtube.com/watch?v=UKclEtptH6k)
        - [Streamlit-OpenAI-Chatbot](https://github.com/AIDevBytes/Streamlit-OpenAI-Chatbot/)
        - [Video - Build Chat PDF app in Python with LangChain, OpenAI, Streamlit](https://www.youtube.com/watch?v=WYzFzZg4YZI)
        - [Build Chat PDF app in Python with LangChain, OpenAI, Streamlit](https://github.com/strongSoda/chat-with-pdf-tutorial)
        ### Deploy your app with Streamlit:
        - [Video Deploy your app with Streamlit - min 54:30](https://youtu.be/kbgr4RlE-xs)
        ### Mock Data:
        - [Mock Data](https://github.com/openai/openai-cookbook/tree/main/examples/data)
        ### Debugging:
        - [Poppler in path for pdf2image](https://stackoverflow.com/questions/53481088/poppler-in-path-for-pdf2image)
        - [How to install Poppler on Windows?](https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows)
        - [Pdf2image Convert From: Is Poppler Installed And In Path - Error Fixed](https://www.youtube.com/watch?v=IDu46GjahDs)
      """
    )

if __name__ == "__main__":
    run()
