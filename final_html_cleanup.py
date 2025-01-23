import re

def cleanup_html_structure(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find and clean up the progress display
    progress_pattern = re.compile(r'(<label>Your Progress:.*?</label>)\s*\d+/10')
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        
        # Remove duplicate progress display
        modified_content = progress_pattern.sub(r'\1', content)
        
        # Update the progress bar styling
        modified_content = modified_content.replace(
            '<label>Your Progress:',
            '<label class="progress-label">Progress:'
        )
        
        output_file.write(modified_content.encode('utf-8'))

    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    cleanup_html_structure('/home/ubuntu/repos/animalbycoda/templates/index.html')
