# Animal Guessing Game

A fun web-based game where players guess animals based on clues. Features include:
- 10-question gameplay
- Score tracking
- Spelling forgiveness
- Multiple clues per animal

## Setup
1. Create a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scriptsctivate
```

2. Install dependencies:
```bash
pip install flask python-Levenshtein
```

3. Run the game:
```bash
python app.py
```

4. Open http://127.0.0.1:5000 in your browser

## How to Play
- You'll get clues about an animal
- Try to guess the animal based on the clues
- Get 7 out of 10 correct to win!

