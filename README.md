# CommitGenerator - Skrypt Dodający Kropkę do Pliku ReadMe Codziennie (max 7 razy dziennie)

Ten projekt zawiera skrypt w Pythonie, który dodaje kropkę do pliku `ReadMe.txt`oraz 'README.md'  co 500sekund, maksymalnie 7 razy dziennie. Zmiany są automatycznie commitowane i pushowane do zdalnego repozytorium GitHub. Zadanie jest skonfigurowane za pomocą Harmonogramu zadań (Task Scheduler) w systemie Windows.

## Spis treści

1. [Wymagania](#wymagania)
2. [Pliki w repozytorium](#pliki-w-repozytorium)
3. [Instalacja](#instalacja)
4. [Konfiguracja Harmonogramu zadań (Task Scheduler) w systemie Windows](#konfiguracja-harmonogramu-zadań-task-scheduler-w-systemie-windows)
    - [Krok 1: Otwórz Harmonogram zadań](#krok-1-otwórz-harmonogram-zadań)
    - [Krok 2: Utwórz nowe zadanie](#krok-2-utwórz-nowe-zadanie)
    - [Krok 3: Skonfiguruj ogólne ustawienia zadania](#krok-3-skonfiguruj-ogólne-ustawienia-zadania)
    - [Krok 4: Skonfiguruj wyzwalacz](#krok-4-skonfiguruj-wyzwalacz)
    - [Krok 5: Skonfiguruj akcję](#krok-5-skonfiguruj-akcję)
    - [Krok 6: Skonfiguruj warunki (opcjonalnie)](#krok-6-skonfiguruj-warunki-opcjonalnie)
    - [Krok 7: Skonfiguruj ustawienia (opcjonalnie)](#krok-7-skonfiguruj-ustawienia-opcjonalnie)
    - [Krok 8: Zakończ i zapisz zadanie](#krok-8-zakończ-i-zapisz-zadanie)
5. [Skrypt `commit_generator.py`](#skrypt-commit_generatorpy)
6. [Plik `config.json`](#plik-configjson)
7. [Konfiguracja Git](#konfiguracja-git)
8. [Uruchamianie skryptu](#uruchamianie-skryptu)

## Wymagania

- Python 3.x
- Git
- Konto GitHub i skonfigurowane zdalne repozytorium
- System operacyjny Windows

## Pliki w repozytorium

- `CommitGenerator.py`: Skrypt Python dodający kropkę do pliku `ReadMe.txt`, commitujący i pushujący zmiany do GitHub.
- `config.json`: Plik konfiguracyjny przechowujący informacje o liczbie commitów wykonanych danego dnia.
- `ReadMe.txt`: Plik, do którego będą dodawane kropki.

## Instalacja

1. **Klonowanie repozytorium:**

   Skopiuj repozytorium na swój komputer:
   ```bash
   git clone <https://github.com/RafalSa/CommitGenerator>
   cd <CommitGenerator>
   ```
Zainstaluj Python i Git:

Upewnij się, że Python i Git są zainstalowane na Twoim komputerze. Możesz je pobrać i zainstalować z oficjalnych stron:

Python
Git
Konfiguracja zdalnego repozytorium:

Skonfiguruj zdalne repozytorium:

bash

git remote add origin <https://github.com/RafalSa/CommitGenerator>
Sprawdź ścieżki:

Znajdź ścieżkę do interpretera Python:
bash

where python
Znajdź ścieżkę do skryptu commit_generator.py i config.json.
## Konfiguracja Harmonogramu zadań (Task Scheduler) w systemie Windows
## Krok 1: Otwórz Harmonogram zadań
Kliknij przycisk Start.
Wpisz "Harmonogram zadań" i kliknij na aplikację "Harmonogram zadań", aby ją otworzyć.
## Krok 2: Utwórz nowe zadanie
W okienku po prawej stronie kliknij na "Utwórz zadanie...".
## Krok 3: Skonfiguruj ogólne ustawienia zadania
W zakładce "Ogólne" wpisz nazwę zadania, np. "CommitGenerator - Dodaj kropkę do ReadMe".
Opcjonalnie możesz wpisać opis zadania.
Zaznacz opcję "Uruchom z najwyższymi uprawnieniami".
## Krok 4: Skonfiguruj wyzwalacz
Przejdź do zakładki "Wyzwalacze".
Kliknij "Nowy...".
W sekcji "Rozpocznij zadanie" wybierz "Na podstawie harmonogramu".
Wybierz opcję "Codziennie".
Ustaw czas rozpoczęcia (np. 00:00).
W sekcji "Powtarzaj zadanie co" wybierz "1 godzinę" i "trwające" wybierz "Nieograniczony".
Kliknij "OK".
## Krok 5: Skonfiguruj akcję
Przejdź do zakładki "Akcje".
Kliknij "Nowa...".
W sekcji "Akcja" wybierz "Uruchom program".
W polu "Program/skrypt" wpisz ścieżkę do interpretera Python, np. C:\Python39\python.exe.
W polu "Dodaj argumenty (opcjonalne)" wpisz ścieżkę do skryptu, np. C:\Users\TwojeImie\Documents\commit_generator.py.
Kliknij "OK".
## Krok 6: Skonfiguruj warunki (opcjonalnie)
Przejdź do zakładki "Warunki".
Możesz dostosować ustawienia, np. w sekcji "Zasilanie" odznaczyć "Uruchom tylko, jeśli komputer jest podłączony do zasilania sieciowego".
## Krok 7: Skonfiguruj ustawienia (opcjonalnie)
Przejdź do zakładki "Ustawienia".
Zaznacz opcję "Uruchom nowe wystąpienie".
## Krok 8: Zakończ i zapisz zadanie
Kliknij "OK".
Zostaniesz poproszony o podanie hasła do konta użytkownika. Wprowadź hasło i kliknij "OK".
## Skrypt commit_generator.py
Poniżej znajduje się kod skryptu commit_generator.py, który należy umieścić w katalogu z repozytorium:

python
```bash
# -*- coding: utf-8 -*-

import time
import subprocess
import json
from datetime import datetime
import os

CONFIG_FILE = 'config.json'
RUN_DURATION = 3600
INTERVAL = 500

def load_config():
    if not os.path.exists(CONFIG_FILE):
        # Jeśli plik konfiguracyjny nie istnieje, stwórz nowy z domyślnymi wartościami
        config = {"last_commit_date": "", "commit_count": 0}
        save_config(config)
    else:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
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

    # Rejestracja czasu rozpoczęcia działania
    start_time = time.time()
    
    while time.time() - start_time < RUN_DURATION:
        current_date = datetime.now().strftime('%Y-%m-%d')
        if config['last_commit_date'] != current_date:
            config['last_commit_date'] = current_date
            config['commit_count'] = 0

        if config['commit_count'] < 7:
            for file_path in files:
                add_dot_to_file(file_path)
            commit_and_push_changes()
            config['commit_count'] += 1
            save_config(config)
        else:
            print("Reached maximum number of commits for today.")
        
        # Czekaj przez 10 minut przed kolejnym dodaniem kropki
        time.sleep(INTERVAL)
        

if __name__ == '__main__':
    main()

```
## Plik config.json
Poniżej znajduje się przykład pliku config.json, który należy umieścić w katalogu z repozytorium:

json
```bash
{
    "last_commit_date": "",
    "commit_count": 0
}
```
## Konfiguracja Git
Upewnij się, że masz skonfigurowane zdalne repozytorium:

```bash

git init
git remote add origin <URL_DO_TWOJEGO_REPOZYTORIUM>
```
## Uruchamianie skryptu
Skrypt będzie uruchamiany automatycznie przez Harmonogram zadań zgodnie z ustawieniami.




...............................................................................................................................................................................