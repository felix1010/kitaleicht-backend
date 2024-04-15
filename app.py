from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有源的请求访问该应用

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
