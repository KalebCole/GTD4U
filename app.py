from flask import Flask, request, jsonify
from model import classifier

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    if not data or 'tasks' not in data:
        return jsonify({"error": "Invalid request. Please provide a 'tasks' key with a list of tasks."}), 400

    try:
        tasks = data['tasks']
        results = [{'task': task, 'category': classifier.classify(task)} for task in tasks]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
