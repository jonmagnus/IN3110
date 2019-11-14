from flask import Flask, escape, request, render_template, send_file
import os
from visualize import handle_image_generation

template_folder = os.path.join(os.getcwd(), 'templates')
assert os.path.exists(template_folder), f'Missing template folder \'{template_folder}\''
app = Flask(__name__, template_folder=template_folder)

state = {
    'classifier': None,
    'test_score': None,
    'train_score': None,
    }


@app.route('/')
def root():
    return render_template('root.html')

@app.route('/render_image', methods=['POST'])
def render_image():
    global state
    assert request.method == 'POST'
    classifier = request.form['classifier']
    

    return render_template(
            'root.html',
            classifier=classifier,
            train_score=state['train_score'],
            test_score=state['test_score'],
            )


@app.route('/image.svg', methods=['GET'])
def generate_image():
    global state
    classifier = request.args.get('classifier', '')
    train_score, test_score = handle_image_generation(classifier)
    state['train_score'] = train_score
    state['test_score'] = test_score
    
    imagename = 'image.svg'
    resourcepath = os.path.join(os.getcwd(), 'resources')
    if not os.path.exists(resourcepath):
        os.path.makedirs(resourcepath)

    imagepath = os.path.join(resourcepath, imagename)
    return send_file(imagepath, mimetype='image/svg+xml')

if __name__=='__main__':
    app.run(debug=True)

