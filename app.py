from flask import Flask,render_template, request, redirect, session, flash, url_for
from models.jogos import *
from models.usuarios import *

cs=Jogo('CS','FPS','PC')
valorant=Jogo('Valorant','FPS','PC')

usuario1=Usuarios('Nilo','river','1234')
usuario2=Usuarios('Luana','lua','abcd')

app=Flask(__name__)
app.secret_key='alura'

@app.route('/')
def index():
    jogos=Jogo.jogos
    return render_template('lista_jogos.html', titulo='Jogos',jogos=jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    plataforma=request.form['plataforma']
    jogo=Jogo(nome,categoria, plataforma)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima=request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in Usuarios.usuarios:
        usuario=Usuarios.usuarios[request.form['usuario']]
        if usuario.senha==request.form['senha']:
            session['usuario_logado']=request.form['usuario']
            flash(f'{usuario.nickname} logado com sucesso')
            proxima_pagina=request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado']=None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run()

