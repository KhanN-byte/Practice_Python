'''

lsof -i:5000 #search for all hosts with that port 5000
kill -9 <PID> #this ends the hosts running in the background with port 5000

'''
import logging

# Logging Configuration
logging.basicConfig(filename='err.log', level=logging.DEBUG)
logging.debug('This is a debug msg')

###########################################
# Flask Server Code
###########################################

from flask import Flask, request
import requests
import threading
import time
import os

app = Flask(__name__)
shutdown_event = threading.Event()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'This is a GET request'
    elif request.method == 'POST':
        return 'This is a POST request'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        print('Not running with the Werkzeug Server')
    else:
        func()
        print('Server shutting down...')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_event.set()
    shutdown_server()
    return 'Server shutdown initiated'

def send_data():
    time.sleep(1)  # Give the server a moment to start
    resp = requests.post('http://127.0.0.1:5000/')
    if resp.request.method == 'POST':
        print('This was a POST method call') 
    # Send shutdown request
    resp = requests.post('http://127.0.0.1:5000/shutdown')
    if resp.status_code == 200:
        print('Server shutdown initiated')

def run_app():
    app.run()

if __name__ == '__main__':
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_app)
    flask_thread.start()

    # Send POST request
    send_data()

    # Wait for shutdown event
    shutdown_event.wait()

    print('Flask server has been shutdown')

###########################################
# Scikit-Learn Code
###########################################

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Decision Tree classifier on the training set
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Optional: Print feature importances
feature_importances = clf.feature_importances_
print("Feature importances:")
for feature, importance in zip(iris.feature_names, feature_importances):
    print(f'{feature}: {importance:.2f}') 

