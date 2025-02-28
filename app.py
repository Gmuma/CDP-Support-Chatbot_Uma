import logging
from flask import Flask, render_template, request, jsonify
from chatbot import get_cdp_response

app = Flask(__name__)

# Enable detailed error logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        question = data.get("question", "")
        cdp_name = data.get("cdp", "").lower()

        if not question or not cdp_name:
            logging.error("Invalid input received")
            return jsonify({"error": "Invalid input"}), 400

        response = get_cdp_response(question, cdp_name)
        return jsonify({"answer": response})

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Something went wrong!"}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
