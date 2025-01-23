import re

def update_description_block_color(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    pattern = re.compile(r'(\.description-block\s*{\s*background:\s*)var\(--accent-color\)(\s*;)')
    
    with open(file_path, 'r') as input_file, open(temp_output, 'w') as output_file:
        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break
                
            # Replace with a lighter purple that's still visible
            modified_chunk = pattern.sub(r'\1rgba(156, 131, 232, 0.2)\2', chunk)
            output_file.write(modified_chunk)

    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    update_description_block_color('/home/ubuntu/repos/animalbycoda/templates/index.html')
