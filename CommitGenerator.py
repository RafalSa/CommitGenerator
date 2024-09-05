# -*- coding: utf-8 -*-

import time
import subprocess
import json
from datetime import datetime
import os
import random  # Dodane do generowania losowej liczby kropek

CONFIG_FILE = 'config.json'
RUN_DURATION = 3600  # Czas dzia�ania skryptu w sekundach
INTERVAL = 500       # Czas mi�dzy dodawaniem kropek w sekundach

def load_config():
    if not os.path.exists(CONFIG_FILE):
        # Je�li plik konfiguracyjny nie istnieje, stw�rz nowy z domy�lnymi warto�ciami
        config = {"last_commit_date": "", "commit_count": 0, "daily_commit_limit": 0}
        save_config(config)
    else:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
        
        # Sprawd�, czy w pliku istnieje klucz 'daily_commit_limit', je�li nie, dodaj go
        if "daily_commit_limit" not in config or config["daily_commit_limit"] == 0:
            config["daily_commit_limit"] = random.randint(3, 7)  # Ustaw losowy limit commit�w
            save_config(config)  # Zapisz zmiany w pliku konfiguracyjnym
    
    return config

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def add_dot_to_file(file_path):
    with open(file_path, 'a') as file:
        file.write('.')

def commit_and_push_changes():
    subprocess.run(['git', 'add', 'ReadMe.txt', 'README.md'])
    subprocess.run(['git', 'commit', '-m', 'Add dot to files'])
    subprocess.run(['git', 'push'])

def main():
    files = ['ReadMe.txt', 'README.md']
    config = load_config()

    # Rejestracja czasu rozpocz�cia dzia�ania
    start_time = time.time()
    
    while time.time() - start_time < RUN_DURATION:
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Sprawd�, czy jest nowy dzie�
        if config['last_commit_date'] != current_date:
            # Nowy dzie� - reset licznika i losowanie nowego limitu commit�w
            config['last_commit_date'] = current_date
            config['commit_count'] = 0
            config['daily_commit_limit'] = random.randint(3, 7)  # Losowanie liczby commit�w na dzie�
            print(f"New daily commit limit: {config['daily_commit_limit']}")  # Debug: sprawd� warto�� limitu
            save_config(config)

        # Wykonywanie commit�w w zale�no�ci od dziennego limitu
        if config['commit_count'] < config['daily_commit_limit']:
            for file_path in files:
                add_dot_to_file(file_path)
            commit_and_push_changes()
            config['commit_count'] += 1
            print(f"Commit {config['commit_count']} of {config['daily_commit_limit']}")  # Debug: sprawd� licznik commit�w
            save_config(config)
        else:
            print("Reached maximum number of commits for today.")
        
        # Czekaj przez INTERVAL przed kolejnym dodaniem kropki
        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()
