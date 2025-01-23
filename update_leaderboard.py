import re

def update_leaderboard_code(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find the leaderboard initialization
    init_pattern = re.compile(r'(let\s+leaderboard\s*=\s*)\[\](\s*;)')
    
    # Pattern to find the addToLeaderboard function
    add_pattern = re.compile(r'(function\s+addToLeaderboard\s*\([^)]*\)\s*{[^}]*})')
    
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
        
        # Replace the initialization and function
        modified_content = init_pattern.sub(r'\1JSON.parse(localStorage.getItem("leaderboard")) || []\2', content)
        modified_content = add_pattern.sub(new_leaderboard_code, modified_content)
        
        output_file.write(modified_content)

    # Use shell commands to move the file
    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    update_leaderboard_code('/home/ubuntu/repos/animalbycoda/templates/index.html')
