from flask import Flask, render_template, request

app = Flask(__name__)

# Page d'accueil
@app.route("/")
def index():
    return render_template("index.html")

# Action quand on clique
@app.route("/action", methods=["POST"])
def action():
    resultat = 10 + 20  # Exemple d'action Python
    return render_template("resultat.html", resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)
