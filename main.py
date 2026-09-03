from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi, PyCharm! This is my VTS server."

if __name__ == '__main__':
    # ⚠️ Écoute sur 0.0.0.0 pour être accessible depuis l'extérieur
    app.run(host='0.0.0.0', port=3000)