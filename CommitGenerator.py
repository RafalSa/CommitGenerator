import time
import subprocess

def add_dot_to_readme(file_path):
    with open(file_path, 'a') as file:
        file.write('.')

def commit_and_push_changes():
    subprocess.run(['git', 'add', 'ReadMe.txt'])
    subprocess.run(['git', 'commit', '-m', 'Add dot to ReadMe'])
    subprocess.run(['git', 'push'])

def main():
    file_path = 'ReadMe.txt'
    while True:
        add_dot_to_readme(file_path)
        commit_and_push_changes()
        time.sleep(600)  # Czeka 600 sekund (10 minut)

if __name__ == '__main__':
    main()
