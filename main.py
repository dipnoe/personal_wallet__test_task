from consts import FILE
from note_manager import NoteManager
from interaction_handlers import (add_new_note_interaction,
                                  update_note_interaction,
                                  display_balance_interaction,
                                  search_notes_interaction)

actions = {
    '1': add_new_note_interaction,
    '2': display_balance_interaction,
    '3': search_notes_interaction,
    '4': update_note_interaction
}


def main():
    note_manager = NoteManager(file_path=FILE)

    print('''Вас приветствует личный финансовый кошелек. Выберите действие:\n
        1. Добавление записи: Возможность добавления новой записи о доходе или расходе.
        2. Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
        3. Поиск по записям: Поиск записей по категории, дате, сумме или описанию.
        4. Редактирование записи: Изменение существующих записей о доходах и расходах.
        ''')
    while True:
        user_input = input('Введите цифру (или "q" для выхода): ')
        if user_input.lower() == 'q':
            break

        action = actions.get(user_input)

        if action:
            try:
                action(note_manager)
            except ValueError:
                print("Введено некорректное значение.")
            continue

        print('Такого у нас нет. Попробуйте выбрать другое действие.')


if __name__ == '__main__':
    main()
