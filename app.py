# rodar no cmd
#pip install flask
#importar a biblioteca Flask
from flask import Flask
#Cria uma instância da aplicação Flask
app = Flask(__name__)
# Este é um decorador que associa a URL
# '/' (a URL raiz do site) à função que vem logo abaixo.
@app.route('/')
# A função que é executada quando a rota '/' é acessada. 
# Ela retorna a string "Hello, World!".
def hello_world():
    return 'Hello, World!'

# Executa o servidor de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)

