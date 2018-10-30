from flask import Flask,jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'hello': 'world'})

@app.route('/test',endpoint='test')
def test():
    return jsonify({'message':'test'})

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)