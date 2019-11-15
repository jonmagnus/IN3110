from flask import Flask, escape, request, render_template, send_file
import os
from visualize import handle_image_generation
from fitting import classifier_map
from data import get_numerical_columns 
import time

template_folder = os.path.join(os.getcwd(), 'templates')
assert os.path.exists(template_folder), f'Missing template folder \'{template_folder}\''
app = Flask(__name__, template_folder=template_folder)

# Specify global image path to avoid sending around adresses
imagename = 'image.svg'
resourcepath = os.path.join(os.getcwd(), 'resources')
if not os.path.exists(resourcepath):
    os.makedirs(resourcepath)

imagepath = os.path.join(os.getcwd(), resourcepath, imagename)

def get_classifier_options():
    return list(classifier_map.keys())

def get_feature_options():
    return get_numerical_columns()

@app.route('/')
def root():
    classifier_options = get_classifier_options()
    feature_options = get_feature_options()
    return render_template(
            'root.html',
            classifier_options=classifier_options,
            feature_options=feature_options,
            )

@app.route('/render_image', methods=['POST'])
def render_image():
    assert request.method == 'POST'
    classifier = request.form['classifier']
    feature_options = get_feature_options()
    
    feature_set = request.form.getlist('feature_set')

    train_score, test_score = handle_image_generation(
            classifier,
            imagepath=imagepath,
            feature_set=feature_set,
            title='Train score {train_score:.5f} Test score {test_score:.5f}',
            )
    
    classifier_options = get_classifier_options()
    return render_template(
            'root.html',
            classifier=classifier,
            classifier_options=classifier_options,
            feature_options=feature_options,
            feature_set=feature_set,
            timestamp=time.time(),
            visualizable=len(feature_set) == 2,
            train_score=f'{train_score:.5f}',
            test_score=f'{test_score:.5f}',
            )


@app.route('/image.svg', methods=['GET'])
def generate_image():
    return send_file(imagepath, mimetype='image/svg+xml')

if __name__=='__main__':
    app.run(debug=True)

