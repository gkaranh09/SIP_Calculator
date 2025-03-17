from flask import Flask, request, render_template
from calculate_sip import calculate_sip

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        rate = float(request.form["rate"])
        years = int(request.form["years"])
        result = calculate_sip(amount, rate, years)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
