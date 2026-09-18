from flask import Flask, request, jsonify, send_from_directory
from agent import ask_chemcalc

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory(".", "chemcalc.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data["question"]

    result = ask_chemcalc(question)

    return jsonify({"answer": result})


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
