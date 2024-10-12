# Vegapunk AI Chatbot

Welcome to the **Vegapunk AI Chatbot**, a conversational AI inspired by Dr. Vegapunk from the anime *One Piece*, designed to answer questions and analyze images, all within a futuristic, One Piece-themed interface! Set on the legendary **Egghead Island**, this chatbot is powered by Google’s **Gemini 1.5 Flash** model.

## 🌟 Features

- **Text-based Conversations:** Chat with the AI, ask it anything, and enjoy custom responses tailored to Dr. Vegapunk’s personality from *One Piece*.
- **Image Processing:** Upload images for analysis, and the AI will generate insightful responses based on the content of the image.
- **Anime-Themed UI:** The application features a custom design inspired by Egghead Island, with **Monkey D. Luffy** taking the spotlight!
- **Gemini AI Integration:** Powered by Google’s Gemini 1.5 Flash, it brings intelligent and creative conversations directly to your screen.

## 🚀 Quick Demo

![Vegapunk Banner](https://images6.alphacoders.com/132/1329768.png)

The app uses Streamlit for easy and interactive chat and file upload capabilities, allowing for a smooth and intuitive user experience.

---

## 🔧 Installation & Setup Guide

Follow these instructions to set up and run the Vegapunk AI Chatbot on your local machine.

### Prerequisites

- **Python 3.7+**
- **Google API Key** (for Gemini AI)

### Step 1: Clone the Repository

```bash
git clone https://github.com/jeevangowda0711/Vegapunk---chatbot.git
cd Vegapunk---chatbot
```

### Step 2: Create a Virtual Environment

It is recommended to use a virtual environment for this project to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Keys

Create a `.env` file in the project root and add your Google API key for accessing the Gemini AI:

```bash
API_KEY=your_google_api_key_here
```

Make sure the `.env` file is listed in the `.gitignore` to keep it private.

### Step 5: Run the Application

Run the following command to launch the chatbot:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

---

## 🛠️ Project Structure

Here’s a quick overview of the project structure:

- **`app.py`**: The main Python file that runs the Streamlit application and handles the chatbot logic.
- **`.env`**: Contains the Google API key (excluded from version control).
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`.gitignore`**: Specifies files and folders that Git should ignore.
- **`README.md`**: Project documentation (you’re reading it now).

---

## 💬 Usage

1. **Chat with Vegapunk**: Simply type in a question, and Vegapunk will respond.
2. **Custom Responses**: Ask Vegapunk “Who are you?” for a special response.
3. **Upload Images**: Upload images and let Vegapunk analyze them.
4. **Experience One Piece Aesthetics**: Enjoy the *One Piece*-themed UI with Luffy and Egghead Island elements.

---

## 🤖 Technologies Used

- **Python**: The core programming language used for this project.
- **Streamlit**: Framework for building the interactive UI.
- **Google Gemini AI**: Provides the AI chatbot functionality.
- **Pillow**: Used for image processing and handling.
- **Requests**: Handles downloading images from external URLs.
- **dotenv**: Manages environment variables, including the API key.

---

## 🌍 Custom Vegapunk Response

When you ask the bot “Who are you?”, it will respond in a way that channels Dr. Vegapunk from *One Piece*:

```markdown
I am Dr. Vegapunk, the world's greatest scientist! My research spans across countless fields, from artificial Devil Fruits to revolutionary scientific breakthroughs that push the boundaries of what’s possible. You’ve likely heard of my work with the Pacifistas and the Seraphim projects. How can I assist you in your journey?
```

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add a new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## 🔒 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📧 Contact

For any questions or suggestions, feel free to reach out via the GitHub Issues tab.

---

Enjoy your experience with **Vegapunk AI Chatbot**! Let the adventures on Egghead Island begin 🧠🚀!
