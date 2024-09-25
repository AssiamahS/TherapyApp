from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample questions and responses
questions = [
    "How are you feeling today?",
    "What has been on your mind lately?",
    "Can you describe your current mood?",
    "What are you grateful for today?"
]

responses = []

@app.route('/ask', methods=['GET'])
def ask_question():
    if len(questions) > 0:
        question = questions.pop(0)
        return jsonify({"question": question})
    else:
        return jsonify({"message": "No more questions available."})

@app.route('/answer', methods=['POST'])
def answer_question():
    data = request.get_json()
    response = data.get('response')
    if response:
        responses.append(response)
        return jsonify({"message": "Response recorded."})
    else:
        return jsonify({"message": "No response provided."}), 400

if __name__ == '__main__':
    app.run(debug=True)
