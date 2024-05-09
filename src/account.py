from consts import CATEGORIES


class Account:
    def __init__(self, notes):
        self.notes = notes

    def calculate_balance(self) -> [int, int, int]:
        """Подсчет баланса, расходов и доходов."""
        incomes = 0
        expenses = 0
        if self.notes:
            for note in self.notes:
                if note["Категория"] == CATEGORIES[0]:
                    incomes += int(note["Сумма"])
                elif note["Категория"] == CATEGORIES[1]:
                    expenses -= int(note["Сумма"])
            total = incomes + expenses
            return total, incomes, expenses
