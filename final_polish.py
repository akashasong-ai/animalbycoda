import re
import shutil
import os

def apply_final_polish(file_path):
    # Copy both background and logo images
    attachments_dir = os.path.expanduser('~/attachments')
    static_dir = os.path.join(os.path.dirname(file_path), '..', 'static', 'images')
    os.makedirs(static_dir, exist_ok=True)
    
    # Find the logo file
    for filename in os.listdir(attachments_dir):
        if filename.endswith('Vector-Smart-Object.png'):
            logo_source = os.path.join(attachments_dir, filename)
            shutil.copy2(logo_source, os.path.join(static_dir, 'dmt-logo.png'))
            break
    
    # Find the background image
    for filename in os.listdir(attachments_dir):
        if filename.startswith('Screenshot') and filename.endswith('.png'):
            bg_source = os.path.join(attachments_dir, filename)
            shutil.copy2(bg_source, os.path.join(static_dir, 'new_game_bg.png'))
            break
    
    temp_output = file_path + '.tmp'
    
    # Patterns to fix
    progress_pattern = re.compile(r'(<label[^>]*>Your Progress:.*?</label>)\s*\d+/10')
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        
        # Remove duplicate progress display
        modified_content = progress_pattern.sub(r'\1', content)
        
        # Update logo container
        modified_content = modified_content.replace(
            '<a href="https://domoretech.ai">',
            '<div class="logo-container"><a href="https://domoretech.ai" target="_blank">'
        )
        modified_content = modified_content.replace(
            '</a>',
            '</a></div>',
            1  # Replace only the first occurrence
        )
        
        # Add class to progress label
        modified_content = modified_content.replace(
            '<label>Your Progress:',
            '<label class="progress-label">Progress:'
        )
        
        output_file.write(modified_content.encode('utf-8'))

    os.replace(temp_output, file_path)

if __name__ == '__main__':
    apply_final_polish('/home/ubuntu/repos/animalbycoda/templates/index.html')
