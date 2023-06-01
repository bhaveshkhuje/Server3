from flask import Flask, render_template, request
import my_script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process():
    user_input = request.form['user_input']
    result = my_script.process_input(user_input)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)