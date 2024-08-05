import time
import subprocess
import json
from datetime import datetime
import os

CONFIG_FILE = 'config.json'
RUN_DURATION = 3600  # Czas dzia³ania skryptu w sekundach (1 godzina)
INTERVAL = 600       # Czas miêdzy dodawaniem kropek w sekundach (10 minut)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        # Jeœli plik konfiguracyjny nie istnieje, stwórz nowy z domyœlnymi wartoœciami
        config = {"last_commit_date": "", "commit_count": 0}
        save_config(config)
    else:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
    return config

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

    # Rejestracja czasu rozpoczêcia dzia³ania
    start_time = time.time()
    
    while time.time() - start_time < RUN_DURATION:
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
        
        # Czekaj przez 10 minut przed kolejnym dodaniem kropki
        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()
