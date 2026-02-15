"""
Legacy Flask chat interface for the Policy LLM research project.

As of May 2025, the primary interface is Open WebUI (see README). This app is
retained for reference and local use. Contact: Stany.Nzobonimpa@enap.ca
"""

import os

from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Maximum length for a single user message (characters)
MAX_MESSAGE_LENGTH = 8000


def _get_client():
    """Return configured OpenAI client; raises if API key is missing."""
    key = os.getenv("OPENAI_API_KEY")
    if not key or not key.strip():
        raise ValueError("OPENAI_API_KEY is not set")
    openai.api_key = key
    return openai


@app.route("/")
def index():
    """Serve the chat UI."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    Handle a chat message: validate input, call OpenAI, return the assistant reply.
    Expects JSON body: { "message": "<user text>" }.
    """
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json(silent=True) or {}
    user_input = data.get("message")

    if user_input is None:
        return jsonify({"error": "Missing 'message' field"}), 400

    if not isinstance(user_input, str):
        return jsonify({"error": "'message' must be a string"}), 400

    text = user_input.strip()
    if not text:
        return jsonify({"error": "Message cannot be empty"}), 400

    if len(text) > MAX_MESSAGE_LENGTH:
        return (
            jsonify({"error": f"Message exceeds maximum length ({MAX_MESSAGE_LENGTH} characters)"}),
            400,
        )

    try:
        client = _get_client()
    except ValueError as e:
        return jsonify({"error": str(e)}), 503

    try:
        response = client.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": text}],
        )
    except openai.error.RateLimitError:
        return jsonify({"error": "Service is busy; please try again later."}), 503
    except openai.error.APIError as e:
        return jsonify({"error": "The assistant service is temporarily unavailable."}), 503
    except Exception:
        return jsonify({"error": "An unexpected error occurred."}), 500

    reply = response.choices[0].message.get("content", "")
    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
