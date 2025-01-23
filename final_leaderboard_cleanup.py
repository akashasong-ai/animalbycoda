import re

def final_cleanup_leaderboard(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to match the entire leaderboard section including duplicates
    pattern = re.compile(r'let\s+leaderboard\s*=.*?function\s+addToLeaderboard.*?updateLeaderboardDisplay\(\);(\s*}\);)*\s*}', re.DOTALL)
    
    # The correct leaderboard code
    new_code = """let leaderboard = JSON.parse(localStorage.getItem('leaderboard')) || [];

        function addToLeaderboard(name, score) {
            leaderboard.push({ name, score });
            leaderboard.sort((a, b) => b.score - a.score);
            leaderboard = leaderboard.slice(0, 5); // Keep only top 5 scores
            localStorage.setItem('leaderboard', JSON.stringify(leaderboard));
            updateLeaderboardDisplay();
        }"""
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        modified_content = pattern.sub(new_code, content)
        output_file.write(modified_content.encode('utf-8'))

    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    final_cleanup_leaderboard('/home/ubuntu/repos/animalbycoda/templates/index.html')
