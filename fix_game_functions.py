import re

def fix_game_functions(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find the script section
    pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
    
    new_script = """<script>
        let leaderboard = JSON.parse(localStorage.getItem('leaderboard')) || [];
        let currentClues = [];
        let currentAnimal = '';
        let score = 0;

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
            // Reset clues for new animal
            currentClues = [];
            currentAnimal = getRandomAnimal();
            displayClues();
        }

        function startNewGame() {
            score = 0;
            document.getElementById('score-progress').value = 0;
            showNextClues();
        }

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
    fix_game_functions('/home/ubuntu/repos/animalbycoda/templates/index.html')
