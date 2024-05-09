import json
import os
from typing import Any

from src.note import Note


def check_file(file: str) -> bool:
    return os.path.exists(file) and os.path.getsize(file) > 0


class NoteManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.notes = self.read_notes()

    def add_note(self, note: dict[str, Any]) -> None:
        """Добавление новой записи."""
        self.notes.append(note)
        self.write_notes()

    def write_notes(self) -> None:
        """Запись в файл."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            for note in self.notes:
                f.write(json.dumps(note, ensure_ascii=False) + "\n")

    def read_notes(self) -> list[dict[str, Any]]:
        """Чтение записи из файла, если файл существует."""
        if check_file(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return [json.loads(line.strip()) for line in f.readlines()]
        return []

    def search_note(self, search_string: str) -> list[dict[str, Any]]:
        """Поиск записей по вхождению строки."""
        suitable_notes = []
        for note in self.notes:
            for value in note.values():
                if isinstance(value, str) and search_string.lower() in value:
                    suitable_notes.append(note)
        return suitable_notes

    def edit_note(self, note_id: int, new_pair: dict[str, Any]) -> None:
        """Обновление записи по ID."""
        note = self.search_id(note_id)
        for key, value in new_pair.items():
            if key.lower() == "id":
                raise ValueError("Нельзя менять id записи.")
            if key in note.keys():
                note[key] = value
            else:
                raise ValueError("Нет такого поля.")
            try:
                Note(
                    description=note["Описание"],
                    category=note["Категория"],
                    amount=note["Сумма"]
                )
            except Exception as e:
                print(e)
            else:
                note.update(new_pair)
                self.write_notes()

    def search_id(self, note_id: int) -> dict[str, Any] | None:
        """Поиск записи по ID."""
        for note in self.notes:
            if note["id"] == note_id:
                return note
