from flask import Flask, request, render_template

# App erstellen
app = Flask(__name__)

# Website programmieren
@app.route("/home", methods=["GET"])
def Home():
    #return "Hallo, dies ist die Startseite."
    return render_template("index.html")
# App ausführen
app.run(host="127.0.0.1", port=80, debug=True)
