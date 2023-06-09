import json
import os
from datetime import datetime

notes_file = "notes.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().isoformat()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана.")

def read_notes():
    if len(notes) == 0:
        print("Нет доступных заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время создания: {note['timestamp']}")
            print("-----------------------")

def update_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    found = False
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно обновлена.")
            found = True
            break
    if not found:
        print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    found = False
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            found = True
            break
    if not found:
        print("Заметка с указанным ID не найдена.")

# Загрузка существующих заметок
notes = load_notes()

while True:
    print("Выберите действие:")
    print("1. Создать заметку")
    print("2. Просмотреть заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        update_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
