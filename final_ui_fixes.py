import re
import shutil
import os

def apply_final_ui_fixes(file_path):
    # Copy the logo to static/images
    logo_source = os.path.expanduser('~/attachments/a2b29aaa-24e2-4b4b-b5b9-b2897412db28/DMT-Smybol_0002_Vector-Smart-Object.png')
    logo_dest = os.path.join(os.path.dirname(file_path), '..', 'static', 'images', 'dmt-logo.png')
    os.makedirs(os.path.dirname(logo_dest), exist_ok=True)
    shutil.copy2(logo_source, logo_dest)
    
    temp_output = file_path + '.tmp'
    
    # Patterns to fix
    progress_pattern = re.compile(r'(<label>Your Progress:.*?</label>)\s*\d+/10')
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    
    new_style = """<style>
        :root {
            --accent-color: #9C83E8;
            --background-color: rgba(255, 255, 255, 0.9);
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
            background: url('/static/images/new_game_bg.png') center/cover no-repeat;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        
        .logo-container {
            position: absolute;
            top: 1rem;
            right: 1rem;
            z-index: 10;
        }
        
        .logo-container img {
            width: 50px;
            height: auto;
        }
        
        h1 {
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            margin-bottom: 1rem;
        }
        
        .description-block {
            background: var(--background-color);
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            color: #333;
        }
        
        #clues-list {
            background: var(--background-color);
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
            list-style: none;
        }
        
        #clues-list li {
            margin-bottom: 0.5rem;
            color: #333;
        }
        
        .progress-label {
            color: #ffffff;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
            margin: 0.5rem 0;
            display: block;
        }
        
        #score-progress {
            width: 80%;
            height: 20px;
            margin: 1rem auto;
        }
        
        #score-progress::-webkit-progress-value {
            background-color: var(--accent-color);
        }
        
        #score-progress::-webkit-progress-bar {
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
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
        
        #leaderboard-list {
            background: var(--background-color);
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
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        
        # Remove duplicate progress display
        modified_content = progress_pattern.sub(r'\1', content)
        
        # Update styles
        modified_content = style_pattern.sub(new_style, modified_content)
        
        # Update logo container
        modified_content = modified_content.replace(
            '<a href="https://domoretech.ai">',
            '<div class="logo-container"><a href="https://domoretech.ai">'
        )
        modified_content = modified_content.replace(
            '</a>',
            '</a></div>',
            1  # Replace only the first occurrence
        )
        
        output_file.write(modified_content.encode('utf-8'))

    os.replace(temp_output, file_path)

if __name__ == '__main__':
    apply_final_ui_fixes('/home/ubuntu/repos/animalbycoda/templates/index.html')
