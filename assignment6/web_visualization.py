from flask import Flask, escape, request, render_template
import os

template_folder = os.path.join(os.getcwd(), 'templates')
assert os.path.exists(template_folder), f'Missing template folder \'{template_folder}\''
app = Flask(__name__, template_folder=template_folder)

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {escape(name)}'

@app.route('/')
def main():

    assert request.method == 'POST'

    classifier = request.form['classifier']

    template_file = 'web_visualization.html'
    return render_template(template_file)

if __name__=='__main__':
    app.run(debug=True)

