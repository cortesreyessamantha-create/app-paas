from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola desde PaaS en AWS"

if __name__ == '__main__':
    app.run()
