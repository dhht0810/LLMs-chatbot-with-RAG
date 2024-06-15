import streamlit as st
from model import generate_response

# Load CSS from file
def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Markdown from file
def load_markdown(file_name):
    with open(file_name, "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)


def main():
    # Streamlit UI
    st.markdown("""
    <style>
    html, body, .main {
    height: 100%;
    margin: 0;
    }
    .main {
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/9/9f/Sekigaharascreen.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Georgia', serif;
    }
    .stTextInput label {
        font-size: 20px;
        color: #4b5320;
    }
    .stTextInput div input {
        background-color: #e5e4e2;
        color: #4b5320;
        border: 2px solid #4b5320;
        font-family: 'Georgia', serif;
    }
    .stButton button {
        background-color: #4b5320;
        color: #f5f5dc;
        font-family: 'Georgia', serif;
        border: 2px solid #4b5320;
    }
    .stTextArea label {
        font-size: 20px;
        color: #4b5320;
    }
    .stTextArea div textarea {
        background-color: #e5e4e2;
        color: #4b5320;
        border: 2px solid #4b5320;
        font-family: 'Georgia', serif;
    }
    </style>
    """, unsafe_allow_html=True)

    # Streamlit UI
    load_markdown("content.md")
    user_input = st.text_input("User Input", "")
    # Streamlit UI
    if st.button("Send"):
        response = generate_response(user_input)
        st.text_area("Bot Response", response)

if __name__ == "__main__":
    main()