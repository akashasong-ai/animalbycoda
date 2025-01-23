import re
import shutil
import os

def fix_remaining_issues(file_path):
    # Copy the new logo to static/images
    logo_source = os.path.expanduser('~/attachments/a2b29aaa-24e2-4b4b-b5b9-b2897412db28/DMT-Smybol_0002_Vector-Smart-Object.png')
    logo_dest = os.path.join(os.path.dirname(file_path), '..', 'static', 'images', 'dmt-logo.png')
    os.makedirs(os.path.dirname(logo_dest), exist_ok=True)
    shutil.copy2(logo_source, logo_dest)
    
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find the script section
    script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
    
    new_script = """<script>
        let leaderboard = JSON.parse(localStorage.getItem('leaderboard')) || [];
        let currentClues = [];
        let currentAnimal = '';
        let score = 0;
        
        // Animal data with clues
        const animals = [
            { name: 'lion', clues: ['I am the king of the jungle', 'I have a magnificent mane', 'I live in pride'] },
            { name: 'elephant', clues: ['I am the largest land animal', 'I have a long trunk', 'I never forget'] },
            { name: 'penguin', clues: ['I waddle when I walk', 'I love the cold', 'I am an excellent swimmer'] },
            { name: 'giraffe', clues: ['I have a very long neck', 'I am the tallest land animal', 'I have spotted patterns'] },
            { name: 'dolphin', clues: ['I am very intelligent', 'I live in the ocean', 'I communicate with clicks'] }
        ];

        function getRandomAnimal() {
            const randomIndex = Math.floor(Math.random() * animals.length);
            return animals[randomIndex].name;
        }

        function displayClues() {
            const animal = animals.find(a => a.name === currentAnimal);
            if (!animal) return;
            
            let cluesList = document.getElementById('clues-list');
            if (!cluesList) {
                cluesList = document.createElement('ul');
                cluesList.id = 'clues-list';
                const inputField = document.querySelector('input[type="text"]');
                inputField.parentNode.insertBefore(cluesList, inputField);
            }
            
            cluesList.innerHTML = '';
            animal.clues.forEach(clue => {
                const li = document.createElement('li');
                li.textContent = clue;
                cluesList.appendChild(li);
            });
        }

        function updateLeaderboardDisplay() {
            const leaderboardList = document.getElementById('leaderboard-list');
            if (!leaderboardList) return;
            
            leaderboardList.innerHTML = '';
            leaderboard.forEach((entry, index) => {
                const li = document.createElement('li');
                li.textContent = `${entry.name}: ${entry.score}`;
                leaderboardList.appendChild(li);
            });
        }

        function addToLeaderboard(name, score) {
            leaderboard.push({ name, score });
            leaderboard.sort((a, b) => b.score - a.score);
            leaderboard = leaderboard.slice(0, 5); // Keep only top 5 scores
            localStorage.setItem('leaderboard', JSON.stringify(leaderboard));
            updateLeaderboardDisplay();
        }

        function makeGuess() {
            const guessInput = document.querySelector('input[type="text"]');
            const guess = guessInput.value.toLowerCase().trim();
            
            if (guess === currentAnimal.toLowerCase()) {
                score++;
                document.getElementById('score-progress').value = score;
                if (score >= 10) {
                    const playerName = prompt('Congratulations! You won! Enter your name:');
                    if (playerName) {
                        addToLeaderboard(playerName, score);
                    }
                    startNewGame();
                } else {
                    showNextClues();
                }
            } else {
                alert('Try again!');
            }
            guessInput.value = '';
        }

        function showNextClues() {
            currentAnimal = getRandomAnimal();
            displayClues();
        }

        function startNewGame() {
            score = 0;
            document.getElementById('score-progress').value = 0;
            showNextClues();
        }

        // Add event listeners
        document.addEventListener('DOMContentLoaded', function() {
            const guessInput = document.querySelector('input[type="text"]');
            const guessButton = document.querySelector('button:nth-of-type(1)');
            const nextCluesButton = document.querySelector('button:nth-of-type(2)');
            const newGameButton = document.querySelector('button:nth-of-type(3)');
            
            guessInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    makeGuess();
                }
            });
            
            guessButton.addEventListener('click', makeGuess);
            nextCluesButton.addEventListener('click', showNextClues);
            newGameButton.addEventListener('click', startNewGame);
            
            // Initialize the game
            updateLeaderboardDisplay();
            startNewGame();
        });
    </script>"""
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        modified_content = script_pattern.sub(new_script, content)
        output_file.write(modified_content.encode('utf-8'))

    os.replace(temp_output, file_path)

if __name__ == '__main__':
    fix_remaining_issues('/home/ubuntu/repos/animalbycoda/templates/index.html')
