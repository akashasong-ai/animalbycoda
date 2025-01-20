from flask import Flask, render_template, jsonify, session
from animal_game import animals
import random
from Levenshtein import ratio

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

def is_close_enough(guess, actual, threshold=0.85):
    """Check if the guess is close enough to the actual answer"""
    return ratio(guess.lower(), actual.lower()) >= threshold

@app.route('/')
def home():
    # Initialize or reset the score when starting
    session['score'] = 0
    session['questions_asked'] = 0
    return render_template('index.html')

@app.route('/new-game')
def new_game():
    # Increment questions counter
    if 'questions_asked' not in session:
        session['questions_asked'] = 0
    if 'score' not in session:
        session['score'] = 0
    
    session['questions_asked'] = session.get('questions_asked', 0) + 1
    
    # Check if we've reached 10 questions
    if session['questions_asked'] > 10:
        final_score = session['score']
        session['score'] = 0
        session['questions_asked'] = 0
        return jsonify({
            'gameOver': True,
            'finalScore': final_score,
            'won': final_score >= 7  # 70% of 10 questions
        })
    
    # Pick a random animal and randomize its clues
    animal = random.choice(list(animals.keys()))
    clues = random.sample(animals[animal], len(animals[animal]))
    
    return jsonify({
        'animal': animal,
        'clues': clues,
        'questionsAsked': session['questions_asked'],
        'currentScore': session['score']
    })

@app.route('/submit-guess/<guess>/<actual>')
def submit_guess(guess, actual):
    if is_close_enough(guess, actual):
        session['score'] = session.get('score', 0) + 1
        return jsonify({
            'score': session['score'],
            'questionsAsked': session['questions_asked'],
            'isCorrect': True,
            'correctSpelling': actual
        })
    
    return jsonify({
        'score': session['score'],
        'questionsAsked': session['questions_asked'],
        'isCorrect': False
    })

if __name__ == '__main__':
    app.run(debug=True) 