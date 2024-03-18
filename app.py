import os
from flask import Flask, render_template

app = Flask(__name__)

testing_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'docs'))
app.template_folder = testing_dir

@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=6210)
