from flask import render_template, request, redirect, url_for # type: ignore
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amount = request.form['amount']
        # Adicione a lógica para processar o depósito aqui
        return redirect(url_for('index'))
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        amount = request.form['amount']
        # Adicione a lógica para processar o saque aqui
        return redirect(url_for('index'))
    return render_template('withdraw.html')

@app.route('/statement')
def statement():
    # Adicione a lógica para exibir o extrato aqui
    return render_template('statement.html')
