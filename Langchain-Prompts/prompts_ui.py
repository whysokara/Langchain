from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables from a .env file
load_dotenv()

# Set the header of the Streamlit app
st.header('Research Tool')

# Create a dropdown menu for selecting a research paper
paper_input = st.selectbox(
    "Select Research Paper Name", 
    [
        "Attention Is All You Need", 
        "BERT: Pre-training of Deep Bidirectional Transformers", 
        "GPT-3: Language Models are Few-Shot Learners", 
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

# Create a dropdown menu for selecting the explanation style
style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

# Create a dropdown menu for selecting the explanation length
length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = load_prompt("./template.json")

# Fill the placeholders in the template with the selected inputs
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

# Initialize the ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.4)

# Create a button in the Streamlit app
if st.button("Summarize"):
    # If the button is clicked, invoke the model with the prompt
    result = model.invoke(prompt)
    # Display the result in the Streamlit app
    st.write(result.content)