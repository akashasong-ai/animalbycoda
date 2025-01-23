import re

def update_progress_bar_color(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    pattern = re.compile(r'(#score-progress::-webkit-progress-value\s*{\s*background-color:\s*)var\(--accent-color\)(\s*;)')
    
    with open(file_path, 'r') as input_file, open(temp_output, 'w') as output_file:
        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break
                
            modified_chunk = pattern.sub(r'\1#9C83E8\2', chunk)
            output_file.write(modified_chunk)

    # Use shell commands to move the file
    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    update_progress_bar_color('/home/ubuntu/repos/animalbycoda/templates/index.html')
