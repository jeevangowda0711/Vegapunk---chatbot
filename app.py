import os
import base64
import io
import mimetypes
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
import requests

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found. Please set your API key in the .env file.")

# Initialize session state variables
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# Function to handle text request to Gemini API and customize the response for 'who are you'
def get_ai_response(prompt):
    if "who are you" in prompt.lower():
        return """I am Dr. Vegapunk, the world's greatest scientist! My research spans across countless fields,
        from artificial Devil Fruits to revolutionary scientific breakthroughs that push the boundaries of what’s possible.
        You’ve likely heard of my work with the Pacifistas and the Seraphim projects. How can I assist you in your journey?"""
    else:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            st.error(f"API request failed: {e}")
            return "I'm sorry, but I'm having trouble responding right now."

# Function to handle image request to Gemini API
def request_image(image, prompt: str) -> str:
    try:
        # Convert image to base64
        buffer = io.BytesIO()
        image_format = image.format if image.format else 'PNG'
        image.save(buffer, format=image_format)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        # Get the correct MIME type
        mime_type = f"image/{image_format.lower()}"

        # Send image and prompt to Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([
            {"data": image_data, "mime_type": mime_type},
            {"text": prompt or "What do you see in this image?"}
        ])
        return response.text
    except Exception as e:
        st.error(f"Image analysis failed: {str(e)}")
        return "Sorry, I couldn't analyze the image."

# Function to reset form inputs
def reset_form():
    st.session_state['reset_user_input'] = True

# Function to load an image from a URL
def load_image_from_url(url):
    try:
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        return img
    except Exception as e:
        st.error(f"Failed to load image: {e}")
        return None

# Background and banner image URLs
bg_image_url = "https://images7.alphacoders.com/132/1329456.jpeg"
luffy_image_url = "https://images6.alphacoders.com/132/1329768.png"

# Streamlit app layout
def main():
    st.set_page_config(
        page_title="Vegapunk AI - Egghead Island",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Custom CSS for styling
    st.markdown(f"""
    <style>
        body {{
            background-image: url("{bg_image_url}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .main {{
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 15px;
            color: white;
        }}
        .chat-message {{
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            word-wrap: break-word;
            max-width: 70%;
        }}
        .user-message {{
            background-color: rgba(255, 204, 102, 0.8);
            text-align: right;
            align-self: flex-end;
        }}
        .vegapunk-message {{
            background-color: rgba(102, 255, 255, 0.8);
            text-align: left;
            align-self: flex-start;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Check if we need to reset the user input
    if st.session_state.get('reset_user_input', False):
        st.session_state['user_input'] = ''
        st.session_state['reset_user_input'] = False

    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.title("Vegapunk AI")
    st.subheader("Welcome to Egghead Island!")

    # Load and display Luffy banner image
    luffy_image = load_image_from_url(luffy_image_url)
    if luffy_image:
        st.image(luffy_image, use_column_width=True)

    # Display conversation history
    for msg in st.session_state['conversation']:
        if msg['role'] == 'user':
            st.markdown(f"<div class='chat-message user-message'>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-message vegapunk-message'>{msg['content']}</div>", unsafe_allow_html=True)

    # User input within a form
    with st.form(key='user_input_form'):
        user_input = st.text_input("Ask Vegapunk anything:", key='user_input')
        image_file = st.file_uploader("Upload an image (optional):", type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'], key='image_file')
        submit_button = st.form_submit_button(label='Send')

    if submit_button:
        user_message = user_input.strip()
        img = Image.open(image_file) if image_file else None
        if user_message or img:
            if img:
                # Handle image input
                st.session_state['conversation'].append({"role": "user", "content": f"[Image Uploaded] {user_message}"})
                ai_response = request_image(img, user_message)
            else:
                # Handle text input
                st.session_state['conversation'].append({"role": "user", "content": user_message})
                ai_response = get_ai_response(user_message)
            # Add AI's response to conversation
            st.session_state['conversation'].append({"role": "vegapunk", "content": ai_response})
            # Reset the form inputs
            reset_form()
            st.rerun()
        else:
            st.warning("Please enter a message or upload an image before sending.")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
