import os
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from markdown import markdown

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24).hex())

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

API_KEY = os.getenv('GEMINI_API_KEY')
if not API_KEY:
    logger.warning("GEMINI_API_KEY is not set. Chat functionality will be disabled.")
    client = None
else:
    client = genai.Client(api_key=API_KEY)

MAX_MESSAGE_LENGTH = 2000


def get_gemini_response(prompt):
    if not client:
        return {"error": "API key not configured. Please set GEMINI_API_KEY."}
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return {"text": markdown(response.text)}
    except Exception as e:
        logger.exception("Gemini API call failed")
        print(e)
        return {"error": "Sorry, something went wrong. Please try again."}


@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    if len(message) > MAX_MESSAGE_LENGTH:
        return jsonify({"error": f"Message too long (max {MAX_MESSAGE_LENGTH} characters)."}), 400

    result = get_gemini_response(message)

    if "error" in result:
        return jsonify({"error": result["error"]}), 500

    return jsonify({
        "response": result["text"],
        "user_message": message
    })


if __name__ == "__main__":
    debug = os.getenv('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug)
