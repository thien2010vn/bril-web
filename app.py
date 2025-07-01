from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/swap')
def swap():
    return render_template("swap.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Lấy port do Render cung cấp
    app.run(host='0.0.0.0', port=port, debug=True)  # Mở cho Render truy cập
