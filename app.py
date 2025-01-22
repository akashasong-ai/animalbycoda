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
    # Initialize used_animals if not exists
    if not hasattr(app, 'used_animals'):
        app.used_animals = set()
    
    # Get available animals (ones we haven't used yet)
    available_animals = set(animals.keys()) - app.used_animals
    
    # If we've used all animals or this is a new game, reset the used animals
    if not available_animals:
        app.used_animals.clear()
        available_animals = set(animals.keys())
    
    # Pick a random animal from available ones
    animal = random.choice(list(available_animals))
    clues = animals[animal]
    
    # Add to used animals
    app.used_animals.add(animal)
    
    return jsonify({
        'animal': animal,
        'clues': clues,
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