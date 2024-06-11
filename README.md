# AI-Chatbot; Python, Streamlit, OpenAI API

## Chatbot requirements 
1. Business Usecase: 
 - Customer Service for Online Retailers: Develop a chatbot that can provide information on products that automatically answer customer inquiries about product features.
2. Traits:
 - Efficient, Patient, Knowledgeable, Friendly, Detail-Oriented
3. Function:
 - Extracts details from product manuals to provide accurate product information, setup instructions, and troubleshooting help.
4. Communication Style:
 - Clear, concise, and focused on providing relevant information promptly to enhance the customer shopping experience.

## Getting OpenAI API key
To interact with the chatbot, you need to have your OpenAI API key. Follow these steps to get started:

- Open platform.openai.com.
- Click on your name or icon option which is located on the top right corner of the page and select “API Keys” or click on the link — Account API Keys — OpenAI API 
- Alternativelly, you can go to: https://platform.openai.com/api-keys 
- Click on create new secret key button to create a new openai key and save it.

## Getting Started
1. Fork this repo
2. Clone the repository to your local machine.
3. Install the required dependencies using:
 - pip install -r requirements.txt.
4. Set up your OpenAI API key in the file: 
 - .streamlit/secrets.toml  
 - OPENAI_API_KEY = "Your OPENAI_API_KEY here"
5. Run the code and start chattingbot: 
 - python -m streamlit run app.py

## Deploy your Chatbot app with Streamlit from your Github repository
- [Streamlit: How to deploy your app from your Github repository with Streamlit](https://medium.com/@alfredolhuissier/streamlit-how-to-deploy-your-ai-app-7a516548eb90)

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as needed.