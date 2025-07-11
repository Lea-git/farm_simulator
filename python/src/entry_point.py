from flask import Flask
from api import app 

if __name__ == "__main__":
    # On lance l'app depuis ici
    app.run(host="0.0.0.0", port=3005, debug=True)