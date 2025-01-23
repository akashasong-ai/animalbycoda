import re

def fix_text_visibility(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find the style section
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    
    new_style = """<style>
        :root {
            --accent-color: #9C83E8;
            --background-color: #ffffff;
        }
        
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
            background: url('/static/images/new_game_bg.png') center/cover no-repeat, var(--background-color);
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        
        h1 {
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            margin-bottom: 1rem;
        }
        
        .description-block {
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            color: #333;
        }
        
        #clues-list {
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
            list-style: none;
        }
        
        #clues-list li {
            margin-bottom: 0.5rem;
            color: #333;
            font-size: 1.1rem;
        }
        
        input[type="text"] {
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border: 2px solid var(--accent-color);
            border-radius: 0.5rem;
            margin: 1rem 0;
            width: 80%;
            max-width: 300px;
        }
        
        button {
            background-color: var(--accent-color);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border-radius: 0.5rem;
            cursor: pointer;
            margin: 0.5rem;
            transition: background-color 0.2s;
        }
        
        button:hover {
            background-color: #8670d4;
        }
        
        #score-progress {
            width: 80%;
            height: 20px;
            margin: 1rem auto;
        }
        
        #score-progress::-webkit-progress-value {
            background-color: #9C83E8;
        }
        
        #score-progress::-webkit-progress-bar {
            background-color: #f0f0f0;
            border-radius: 10px;
        }
        
        .progress-label {
            color: #ffffff;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
            margin-bottom: 0.5rem;
        }
        
        #leaderboard-list {
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            border-radius: 0.5rem;
            margin-top: 1rem;
            list-style: none;
        }
        
        #leaderboard-list li {
            color: #333;
            margin-bottom: 0.5rem;
        }
    </style>"""
    
    # Pattern to find the game container div
    container_pattern = re.compile(r'(<div class="game-container"[^>]*>)')
    
    # Add description block wrapper
    description_wrapper = r'\1\n<div class="description-block">'
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        # Replace style section
        modified_content = style_pattern.sub(new_style, content)
        # Add description block wrapper
        modified_content = container_pattern.sub(description_wrapper, modified_content)
        # Add closing div for description block before the input
        modified_content = modified_content.replace('<input', '</div><input')
        output_file.write(modified_content.encode('utf-8'))

    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    fix_text_visibility('/home/ubuntu/repos/animalbycoda/templates/index.html')
