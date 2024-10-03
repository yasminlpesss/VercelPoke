from flask import Flask, render_template, request, redirect
lista = []

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Home.html', Titulo='Bem-vindo ao site de Pokémon')

@app.route('/pokemon')
def pokemon():
    return render_template('Pokemon.html', Titulo='Melhores pokémons')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Titulo='Sobre o nosso site')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro de Pokémon')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo='Pokémons cadastrados', lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    numero = request.form['numero']
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    pokemon = [numero, nome, tipo, altura, peso]
    lista.append(pokemon)
    return redirect('/exibir')