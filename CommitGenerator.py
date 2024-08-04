import time
import subprocess
import json
from datetime import datetime

CONFIG_FILE = 'config.json'

def load_config():
    with open(CONFIG_FILE, 'r') as file:
        return json.load(file)

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def add_dot_to_readme(file_path):
    with open(file_path, 'a') as file:
        file.write('.')

def commit_and_push_changes():
    subprocess.run(['git', 'add', 'ReadMe.txt'])
    subprocess.run(['git', 'commit', '-m', 'Add dot to ReadMe'])
    subprocess.run(['git', 'push'])

def main():
    file_path = 'ReadMe.txt'
    config = load_config()

    current_date = datetime.now().strftime('%Y-%m-%d')
    if config['last_commit_date'] != current_date:
        config['last_commit_date'] = current_date
        config['commit_count'] = 0

    if config['commit_count'] < 5:
        add_dot_to_readme(file_path)
        commit_and_push_changes()
        config['commit_count'] += 1
        save_config(config)
    else:
        print("Reached maximum number of commits for today.")

if __name__ == '__main__':
    main()
