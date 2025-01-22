from flask import Flask, render_template, jsonify
from animal_game import animals
import random
from Levenshtein import ratio

app = Flask(__name__)

def is_close_enough(guess, actual, threshold=0.85):
    """Check if the guess is close enough to the actual answer"""
    return ratio(guess.lower(), actual.lower()) >= threshold

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new-game')
def new_game():
    # Pick a random animal and randomize its clues
    animal = random.choice(list(animals.keys()))
    clues = random.sample(animals[animal], len(animals[animal]))
    
    return jsonify({
        'animal': animal,
        'clues': clues
    })

@app.route('/submit-guess/<guess>/<actual>')
def submit_guess(guess, actual):
    return jsonify({
        'isCorrect': is_close_enough(guess, actual),
        'correctSpelling': actual if is_close_enough(guess, actual) else None
    })

if __name__ == '__main__':
    app.run(debug=True)      