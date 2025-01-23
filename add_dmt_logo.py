import re

def add_dmt_logo(file_path):
    chunk_size = 1024 * 1024  # 1MB chunks
    temp_output = file_path + '.tmp'
    pattern = re.compile(r'(<div class="game-container" id="game-container">)')
    
    logo_html = r'\1\n            <div style="position: absolute; top: 1rem; right: 1rem; z-index: 10;">' + \
                r'\n                <a href="https://domoretech.ai" target="_blank">' + \
                r'\n                    <img src="/static/images/dmt-logo.png" alt="DMT Logo" style="width: 50px; height: auto;">' + \
                r'\n                </a>' + \
                r'\n            </div>'
    
    with open(file_path, 'r') as input_file, open(temp_output, 'w') as output_file:
        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break
                
            modified_chunk = pattern.sub(logo_html, chunk)
            output_file.write(modified_chunk)

    # Use shell commands to move the file
    import os
    os.replace(temp_output, file_path)

if __name__ == '__main__':
    add_dmt_logo('/home/ubuntu/repos/animalbycoda/templates/index.html')
