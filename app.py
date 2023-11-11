from flask import Flask

app=Flask(__name__)


@app.route('/home')
def hello():
    return "hello"


@app.route('/hii')
def hi():
    return "hi"
    


if __name__=="__main__":
    app.run(debug=True)