from flask import Flask, render_template  # Adicione render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
       return render_template('index.html')  # Em vez de return 'Hello, World!'

   # O resto permanece igual (incluindo o if __name__ para local)
   
# Apenas para desenvolvimento local (remova ou comente isso para o Render)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
