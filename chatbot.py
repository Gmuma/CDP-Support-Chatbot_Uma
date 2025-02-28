import openai
import logging
from scraper import fetch_documentation

# 🚨 WARNING: This is insecure. Use environment variables instead.
openai.api_key = ""

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_cdp_response(question, cdp_name):
    """
    Fetches documentation and queries OpenAI API for a response.

    :param question: User's question
    :param cdp_name: Name of the Customer Data Platform (Segment, mParticle, Lytics, Zeotap)
    :return: AI-generated response or error message
    """
    documentation = fetch_documentation(cdp_name)

    if "Error" in documentation:
        logging.error(f"Error fetching documentation for {cdp_name}")
        return "Failed to fetch documentation."

    prompt = f"CDP Chatbot | {cdp_name} Help:\n{documentation}\n\nUser: {question}\n\nResponse:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful support chatbot for CDP platforms."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract response safely
        return response.get("choices", [{}])[0].get("message", {}).get("content", "No response generated.")

    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API Error: {str(e)}")
        return f"API Error: {str(e)}"
    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}")
        return "An unexpected error occurred. Please try again."
