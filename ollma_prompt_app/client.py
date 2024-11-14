from flask import Flask, redirect, url_for, render_template, request, jsonify
import requests

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
        return render_template("index.html", text=result)
    return render_template("index.html", text="")

if __name__ == "__main__":
    app.run(debug=True)
