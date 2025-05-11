from flask import Flask, render_template, request, send_from_directory, abort
import os

app = Flask(__name__)

# Folder where files (including images) are stored
FILES_DIR = os.path.join(os.getcwd(), "files")

# Create some sample images for the game
os.makedirs(FILES_DIR, exist_ok=True)

# Sample images (for demonstration purposes)
with open(os.path.join(FILES_DIR, 'image1.jpg'), 'w') as f:
    f.write("This is a photo of a cute cat!")

with open(os.path.join(FILES_DIR, 'image2.jpg'), 'w') as f:
    f.write("This is a photo of a lovely dog!")

# Simulating /etc/passwd file (as in a Linux system)
os.makedirs(os.path.join(FILES_DIR, 'etc'), exist_ok=True)

# Adding the hidden flag inside the /etc/passwd file
with open(os.path.join(FILES_DIR, 'etc', 'passwd'), 'w') as f:
    f.write("root:x:0:0:root:/root:/bin/bash\n")
    f.write("user:x:1000:1000:Linux User:/home/user:/bin/bash\n")
    f.write("flag:WW91X2ZvdW5kX3RoZV9mbGFnX3VzaW5nX2RpcmVjdG9yeV90cmF2ZXJzYWw=\n")  # Hidden flag in /etc/passwd

CORRECT_FLAG = "flag{You_found_the_flag_using_directory_traversal}"

@app.route('/')
def index():
    return render_template('index.html', correct_flag=None, incorrect_flag=None)

@app.route('/check_flag', methods=['POST'])
def check_flag():
    # Get the user-submitted flag from the form
    user_flag = request.form['flag']

    # Check if the user-submitted flag matches the correct flag
    if user_flag == CORRECT_FLAG:
        return render_template('index.html', correct_flag=True, incorrect_flag=None)
    else:
        return render_template('index.html', correct_flag=None, incorrect_flag=True)



@app.route('/download')
def download_file():
    file_name = request.args.get('file')

    # Simulate directory traversal vulnerability by allowing the user to navigate to files
    # NOTE: In real-world applications, this should NOT be done. Never allow directory traversal!
    safe_path = os.path.join(FILES_DIR, file_name)

    # Check if the file path is inside the allowed directory (FILES_DIR)
    if os.path.commonprefix([safe_path, FILES_DIR]) != FILES_DIR:
        abort(403)  # Forbidden: Prevent access to directories outside the allowed folder

    # Check if the file exists within the files directory and its subfolders
    if not os.path.isfile(safe_path):
        abort(404)  # File not found

    try:
        # Serve the requested file
        return send_from_directory(FILES_DIR, file_name)
    except FileNotFoundError:
        abort(404)  # File not found


if __name__ == '__main__':
    app.run(debug=True)
