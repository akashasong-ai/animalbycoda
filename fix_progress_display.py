import re

def fix_progress_display(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    
    # Pattern to find the progress display section
    pattern = re.compile(r'(<label>Your Progress:.*?</label>)\s*\d+/10')
    
    with open(file_path, 'rb') as input_file, open(temp_output, 'wb') as output_file:
        content = input_file.read().decode('utf-8')
        # Remove the duplicate progress display
        modified_content = pattern.sub(r'\1', content)
        output_file.write(modified_content.encode('utf-8'))

    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    fix_progress_display('/home/ubuntu/repos/animalbycoda/templates/index.html')
