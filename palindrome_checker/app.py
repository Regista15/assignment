from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_palindrome():
    number = request.form['number']
    if number == number[::-1]:
        result = "Yes, it's a palindrome!"
    else:
        result = "No, it's not a palindrome."
    return render_template('index.html', result=result)

if __name__ == '_main_':
    app.run(debug=True)