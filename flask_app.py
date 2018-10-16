import random
from flask import Flask, render_template
from frase_do_dia import gerador_de_frase_i18n as frase_do_dia

app = Flask(__name__)

@app.route("/")
def home():
    frase = frase_do_dia()
    background = random.choice(
        ["red", "blue", "green", "pink", "yellow"]
        )
    
    return render_template(
        'index.html', frase=frase, background=background)
