from src.account import Account
from src.note import Note
from src.note_manager import NoteManager

from consts import CATEGORIES, FIELDS

def print_notes(note):
    for key, value in note.items():
        print(f"{key}: {value}")
    print()


def add_new_note_interaction(note_manager: NoteManager):
    """Добавление записи через пользовательский ввод."""
    print("Доступные категории:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")
    category_index = int(input("Выберите категорию по номеру: ")) - 1

    category = CATEGORIES[category_index]
    amount = int(input("Введите сумму: "))
    description = input("Введите описание: ")

    note = Note(
        category=category,
        amount=amount,
        description=description
    )

    dict_note = note.to_dict()
    note_manager.add_note(dict_note)
    return print_notes(dict_note)


def update_note_interaction(note_manager: NoteManager):
    """Обновление записи пользователем."""
    note_id = int(input('Введите ID записи (чтобы узнать ID, воспользуйтесь поиском): '))

    if note_manager.search_id(note_id) is None:
        raise ValueError('Запись не найдена')

    _key = input('Введите поле, которое хотите изменить: ').title()
    if _key not in FIELDS:
        return "Такого поля нет."
    new_value = input('Введите новое значение: ').lower()
    note_manager.edit_note(note_id, new_pair={_key: new_value})
    print('Успешно.')


def display_balance_interaction(note_manager: NoteManager):
    """Вывод текущих баланса, доходов и расходов."""
    total, incomes, expenses = Account(note_manager.read_notes()).calculate_balance()
    print(f'Всего средств: {total}\nДоходы: {incomes}\nРасходы: {expenses}')


def search_notes_interaction(note_manager: NoteManager):
    """Пользовательский поиск записей по ключевому слову."""
    search_word = input('Введите слово для поиска: ')
    notes = note_manager.search_note(search_word)
    if notes:
        for note in notes:
            return print_notes(note)
    print("Не найдено.")
