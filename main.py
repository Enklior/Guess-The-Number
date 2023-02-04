from flask import Flask, render_template, request
from random import choice
from replit import db

app = Flask(__name__)

if 'guesses' not in db:
  db['guesses'] = []

if 'computer_number' not in db:
  db['computer_number'] = choice(range(1, 101))

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    guess = int(request.form['number_guess'])
    message = check_number_show_message(guess, db['computer_number'])
    db['guesses'].append(message)
    print(db['guesses'])
    print(db['computer_number'])
    
  return render_template('index.html', guesses=reversed(db['guesses']))

@app.route('/reset')
def reset():
  db['computer_number'] = choice(range(1, 101))
  db['guesses'] = []
  return render_template('index.html', guesses=db['guesses'])

'''
It will take in the guessed number and the computer number
2 arguments

>>> check_number_show_message(guessed_number=5, computer_number=50)
"5 is too low"

>>> check_number_show_message(guessed_number=75, computer_number=50)
"75 is too high"

>>> check_number_show_message(guessed_number=50, computer_number=50)
"50 is correct"
'''
def check_number_show_message(guessed_number, computer_number):
  if guessed_number < computer_number:
    return f"{guessed_number} is too low"
    
  elif guessed_number > computer_number:
    return f"{guessed_number} is too high"
    
  else:
    return f"{guessed_number} is correct"

# print(check_number_show_message(50, 50))

app.run(host='0.0.0.0', port=81)