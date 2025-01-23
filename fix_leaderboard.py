import re

def fix_leaderboard_code(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find the entire leaderboard section
    leaderboard_pattern = re.compile(r'let\s+leaderboard\s*=\s*\[.*?\];.*?function\s+addToLeaderboard\s*\([^)]*\)\s*{[^}]*}', re.DOTALL)
    
    new_leaderboard_code = """let leaderboard = JSON.parse(localStorage.getItem('leaderboard')) || [];

        function addToLeaderboard(name, score) {
            leaderboard.push({ name, score });
            leaderboard.sort((a, b) => b.score - a.score);
            leaderboard = leaderboard.slice(0, 5); // Keep only top 5 scores
            localStorage.setItem('leaderboard', JSON.stringify(leaderboard));
            updateLeaderboardDisplay();
        }"""
    
    with open(file_path, 'r') as input_file, open(temp_output, 'w') as output_file:
        content = input_file.read()
        modified_content = leaderboard_pattern.sub(new_leaderboard_code, content)
        output_file.write(modified_content)

    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    fix_leaderboard_code('/home/ubuntu/repos/animalbycoda/templates/index.html')
