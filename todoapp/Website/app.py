from flask import Flask, Blueprint, render_template
from rotas import page

#inicialização
def create_app():
    page = Flask(__name__)
    page.config['SECRET_KEY'] = 'KDLSIEKDLSEI598985'
    from rotas import page
    return page

app = create_app()

#inicialização servidor
if __name__ == '__main__':
    app.run(debug = True)