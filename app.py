from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")  # Get user message from the request
        if not user_message:
            return jsonify({"response": "Please provide a message."})
        response = get_response(user_message)  # Get response from chatbot
        return jsonify({"response": response})  # Return the chatbot response
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, there was an error processing your request."})

if __name__ == "__main__":
    app.run(debug=True, port=5017)
