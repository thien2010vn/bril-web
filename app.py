from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/swap')
def swap():
    return render_template("swap.html")

if __name__ == '__main__':
    app.run(debug=True)
