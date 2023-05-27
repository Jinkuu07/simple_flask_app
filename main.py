from flask import Flask, render_template, request
app = Flask(__name__)

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message='Hello, World!')

@app.route('/form', methods=['GET', 'POST'])
def render_form():
    message = ''
    if request.method == 'POST':
        text = request.form.get('text')
        if request.form['submit_button'] == 'Lowercase':
            message = text.lower()
        elif request.form['submit_button'] == 'Uppercase':
            message = text.upper()
        elif request.form['submit_button'] == 'Count':
            count = len(text.split())
            message = f"Total number of words: {count}"
    return render_template('form.html', message=message)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
