from flask import Flask
import os  # Adicione esta importação

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Apenas para desenvolvimento local (remova ou comente isso para o Render)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
