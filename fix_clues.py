import re

def fix_clues_functionality(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find the script section
    pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
    
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
            
            const cluesList = document.getElementById('clues-list');
            if (!cluesList) {
                const gameContainer = document.querySelector('.game-container');
                const newCluesList = document.createElement('ul');
                newCluesList.id = 'clues-list';
                newCluesList.style.listStyle = 'none';
                newCluesList.style.padding = '1rem';
                gameContainer.insertBefore(newCluesList, document.querySelector('input[type="text"]'));
            }
            
            const cluesList = document.getElementById('clues-list');
            cluesList.innerHTML = '';
            animal.clues.forEach(clue => {
                const li = document.createElement('li');
                li.textContent = clue;
                li.style.marginBottom = '0.5rem';
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
        document.querySelector('input[type="text"]').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                makeGuess();
            }
        });

        document.querySelector('button:nth-of-type(1)').addEventListener('click', makeGuess);
        document.querySelector('button:nth-of-type(2)').addEventListener('click', showNextClues);
        document.querySelector('button:nth-of-type(3)').addEventListener('click', startNewGame);

        // Initialize the game
        updateLeaderboardDisplay();
        startNewGame();
    </script>"""
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        modified_content = pattern.sub(new_script, content)
        output_file.write(modified_content.encode('utf-8'))

    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    fix_clues_functionality('/home/ubuntu/repos/animalbycoda/templates/index.html')
