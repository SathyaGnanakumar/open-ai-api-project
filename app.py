from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    script_name = request.form['script_name']
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    return render_template('result.html', result=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)
