from flask import Flask,render_template, request, redirect, session
from models.jogos import *

cs=Jogo('CS','FPS','PC')
valorant=Jogo('Valorant','FPS','PC')

app=Flask(__name__)
app.secret_key='alura'


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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'Senha'==request.form['senha']:
        session['usuario_logado']=request.form['usuario']
        flash('Usuario logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')

if __name__=='__main__':
    app.run()

