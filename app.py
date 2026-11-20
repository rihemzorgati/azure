
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Bienvenue dans notre école privée</h1>
    <p>Application Flask hébergée sur Microsoft Azure.</p>
    <h2>Nos formations</h2>
    <ul>
        <li>Informatique</li>
        <li>Cloud Computing</li>
        <li>Intelligence Artificielle</li>
    </ul>
    """

@app.route("/contact")
def contact():
    return "<h1>Contactez notre école</h1>"

if __name__ == "__main__":
    app.run()
