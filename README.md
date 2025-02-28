**CDP Support Chatbot**

**Overview**

The CDP Support Chatbot is a Flask-based application that helps users get support for different Customer Data Platforms (CDPs) like Segment, mParticle, Lytics, and Zeotap. The chatbot fetches relevant documentation and provides answers to user queries using OpenAI's GPT model.

**Features**

Interactive chatbot for answering CDP-related queries.

Fetches documentation dynamically for better responses.

Simple and user-friendly UI built with HTML, CSS, and JavaScript.

Flask backend integrated with OpenAI API.

**Prerequisites**

Before running the chatbot, ensure you have the following installed:

Python 3.8+

Flask

**Requests**

If not installed, run the following:

    pip install flask requests python-dotenv openai

**Installation & Setup**

1️⃣ Clone the Repository

  git clone https://github.com/Gmuma/CDP-Support-Chatbot_Uma.git
cd CDP-Support-Chatbot_Uma

2️⃣ Set Up Environment Variables

Create a .env file in the root directory and add your OpenAI API key:

echo "OPENAI_API_KEY=your_openai_api_key_here" > .env

Or manually create .env and add:

OPENAI_API_KEY=your_openai_api_key_here

3️⃣ Run the Flask Application

      python app.py

You should see:

  Running on http://127.0.0.1:5000/

**Usage**

Open a browser and go to http://127.0.0.1:5000/

Select a CDP from the dropdown menu.

Type your question and click Ask.

The chatbot will fetch relevant information and respond.

**Troubleshooting**

1️⃣ OpenAI API Key Error

Error: You exceeded your current quota or Invalid API Key

Ensure you have a valid OpenAI API key set in .env.

If your key is leaked, revoke and generate a new one from OpenAI here.

2️⃣ API Call Failing

Error: module 'openai' has no attribute 'OpenAI'

Ensure you are using OpenAI Python SDK v1.0+.

**Run:**

  pip install --upgrade openai

**License**

This project is open-source under the MIT License.

![image](https://github.com/user-attachments/assets/91302750-1369-4db2-be02-73bdb5df5e11)

