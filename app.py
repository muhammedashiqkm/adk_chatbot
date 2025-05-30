from flask import Flask, request, jsonify
import asyncio
import os

from dotenv import load_dotenv
from college_agent.agent import root_agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai.types import Content, Part

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Constants
APP_NAME = "college_rag_app"

# In-memory session service (volatile memory)
session_service = InMemorySessionService()

# ADK Runner setup
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)

# ----------------------------------------
# Async helper to run the agent
# ----------------------------------------
async def run_agent(user_id: str, session_id: str, user_input: str) -> str:
    content = Content(role="user", parts=[Part(text=user_input)])
    final_response = ""
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response() and event.content and event.content.parts:
            raw = event.content.parts[0].text
            final_response = raw.strip() if isinstance(raw, str) else raw
    return final_response

# ----------------------------------------
# POST /start_session
# ----------------------------------------
@app.route("/start_session", methods=["POST"])
def start_session():
    try:
        data = request.json
        username = data.get("username")
        session_name = data.get("session_name")

        if not username or not session_name:
            return jsonify({"error": "Missing 'username' or 'session_name'"}), 400

        asyncio.run(session_service.create_session(
            app_name=APP_NAME,
            user_id=username,
            session_id=session_name
        ))

        return jsonify({
            "user_id": username,
            "session_id": session_name,
            "message": f"Session created: user/{username}/session/{session_name}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------------------
# POST /ask
# ----------------------------------------
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        username = data.get("username")
        session_name = data.get("session_name")
        question = data.get("question")

        if not username or not session_name or not question:
            return jsonify({"error": "Missing 'username', 'session_name', or 'question'"}), 400

        # Ensure session exists
        try:
            asyncio.run(session_service.get_session(
                app_name=APP_NAME,
                user_id=username,
                session_id=session_name
            ))
        except:
            return jsonify({"error": f"Session not found: user/{username}/session/{session_name}"}), 404

        # Ask the agent
        response_text = asyncio.run(run_agent(username, session_name, question))

        return jsonify({
            "user_id": username,
            "session_id": session_name,
            "response": response_text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------------------
# POST /end_session
# ----------------------------------------
@app.route("/end_session", methods=["POST"])
def end_session():
    try:
        data = request.json
        username = data.get("username")
        session_name = data.get("session_name")

        if not username or not session_name:
            return jsonify({"error": "Missing 'username' or 'session_name'"}), 400

        asyncio.run(session_service.delete_session(
            app_name=APP_NAME,
            user_id=username,
            session_id=session_name
        ))

        return jsonify({
            "message": f"Session deleted: user/{username}/session/{session_name}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------------------
# Run Flask app
# ----------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
