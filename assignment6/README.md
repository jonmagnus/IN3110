# Assignment 6
```
$ python3 data.py
```
Produces a 4 by 4 grid of plots showing the correspondence between different features.

```
$ python3 fitting.py
train_score 0.7827476038338658 test_score 0.6835443037974683
``` 
Trains a random classifier on all the features.

```
$ python3 visualize.py
```
Trains a random classifier on two random features and produces a contour map for the classifier with the datapoints shown.

```
$ sh generate_docs.sh
$ python3 web_visualization.py
 * Serving Flask app "web_visualization" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 203-905-210
```
Starts a flask web-server.
Access the website through your browser with at the address `localhost:5000`.
Debugging on the server is set to be active.
Remember to run `generate_docs.sh` first to generate the html documents for the documentation.
