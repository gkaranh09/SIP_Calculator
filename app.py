# app.py
from flask import Flask, request, render_template
from src.calculate_sip import calculate_sip  # Ensure correct import

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            rate = float(request.form["rate"])
            years = int(request.form["years"])
            months = years * 12  # Convert years to months
            result = calculate_sip(amount, months, rate)
        except ValueError:
            result = "Invalid input! Please enter valid numbers."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
