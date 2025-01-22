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
    # Pick a random animal and get its clues
    animal = random.choice(list(animals.keys()))
    clues = animals[animal]  # Get the original clues array
    
    return jsonify({
        'animal': animal,
        'clues': clues,  # Return unmodified clues array
        'score': 0,
        'questionsAsked': 0,
        'totalQuestions': 10
    })

@app.route('/submit-guess/<guess>/<actual>')
def submit_guess(guess, actual):
    is_correct = is_close_enough(guess, actual)
    return jsonify({
        'isCorrect': is_correct,
        'correctSpelling': actual if is_correct else None,
        'score': 1 if is_correct else 0
    })

if __name__ == '__main__':
    app.run(debug=True)                  