from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

thoughts = []

@app.route('/')
def index():
    return render_template('index.html', thoughts=thoughts)

@app.route('/add_thought', methods=['POST'])
def add_thought():
    thought = request.form['thought']
    thoughts.append(thought)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
