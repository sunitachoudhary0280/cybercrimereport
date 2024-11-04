from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def analyze_text(text):
    """
    Analyze the given text for potential cybercrime categories.
    """
    lowercased_text = text.lower()
    keywords = {
        "phishing": ["phishing", "email", "link", "account", "password"],
        "malware": ["malware", "virus", "trojan", "infected", "suspicious file"],
        "ddos": ["ddos", "denial of service", "attack", "website down", "traffic"],
        "identity_theft": ["identity theft", "personal information", "stolen", "fraud", "impersonation"],
    }

    detected_categories = [
        category
        for category, words in keywords.items()
        if any(word in lowercased_text for word in words)
    ]

    if not detected_categories:
        return "No specific cybercrime category detected. Please provide more details."

    return f"Potential cybercrime categories detected: {', '.join(detected_categories)}. Please provide this report to the appropriate authorities for further investigation."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        if file:
            report_text = file.read().decode('utf-8')
    else:
        report_text = request.form.get('report_text', '')

    if not report_text.strip():
        return jsonify({"error": "Report text is empty. Please provide a non-empty report."}), 400

    result = analyze_text(report_text)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)