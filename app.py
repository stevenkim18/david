from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('menu'))

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route("/test2")
def test2():
    return render_template('test2.html')

if __name__ == "__main__":
    app.run(port=8080)
