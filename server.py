from flask import Flask, render_template, redirect, request, session
from random import randint
app = Flask(__name__)

app.secret_key = "keep it a secret"

#root route
@app.route('/')
def index():
    random_int=randint(0, 100)
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        session['number']=random_int
    return render_template('index.html', message=session['message'])

@app.route('/guess', methods=['POST'])
def guess():
    print("Displaying users guesses")
    print(request.form)
    session['user_guess'] = user_guess = int(request.form['guess'])
    if user_guess == session['number']:
        session['message'] = "You guessed the correct number!"
    elif user_guess > session['number']:
        session['message'] = "Too high! Guess again."
    elif user_guess < session['number']:
        session['message'] = "Too low! Guess again"
    else:
        session['message'] = "Enter a number in range, between 1-100."
    return render_template('index.html', user_guess=session['user_guess'], rand_int=session['number'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)