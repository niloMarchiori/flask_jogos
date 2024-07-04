from flask import Flask,render_template, request, redirect
from models.jogos import *

app=Flask(__name__)
cs=Jogo('CS','FPS','PC')
valorant=Jogo('Valorant','FPS','PC')

@app.route('/')
def index():
    jogos=Jogo.jogos
    return render_template('lista_jogos.html', titulo='Jogos',jogos=jogos)

@app.route('/novo')

def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    plataforma=request.form['plataforma']
    jogo=Jogo(nome,categoria, plataforma)

    return redirect('/')

if __name__=='__main__':
    app.run()

