from flask import Flask, redirect, url_for, render_template, request, jsonify
import requests
from colorama import Fore, Style

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            response = requests.post(
                "http://localhost:8000/ollama/invoke", 
                json={'input': {'question': user_input}}
            )
            response_data = response.json()
            result = response_data.get('output', 'Cevap alınamadı')
        except Exception as e:
            result = f"Hata oluştu: {str(e)}"
        return render_template("index.html", text=result, question_1='Previous Question : ' + user_input)
    return render_template("index.html", text="", question_1="")

if __name__ == "__main__":
    app.run(debug=True)
