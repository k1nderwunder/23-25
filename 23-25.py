import random
import string
from abc import ABC, abstractmethod

# Интерфейс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретные команды
class InputDataCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.input_data()

class ExecuteAlgorithmCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.execute_algorithm()

class PrintResultCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.print_result()

class ExitProgramCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.exit_program()

# Получатель (Receiver)
class PalindromeFinder:
    def __init__(self):
        self.text = ""
        self.palindromes = []
        self.algorithm_executed = False

    def input_data(self):
        print("Выберите способ ввода данных:")
        print("1. Ввести данные вручную")
        print("2. Сгенерировать данные случайным образом")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            self.text = input("Введите текст: ")
        elif choice == '2':
            self.text = self.generate_random_text()
        else:
            print("Неверный выбор. Попробуйте снова.")
            return self.input_data()

        self.palindromes = []
        self.algorithm_executed = False

    def generate_random_text(self):
        words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7))) for _ in range(20)]
        return ' '.join(words)

    def execute_algorithm(self):
        if self.text:
            self.palindromes = self.find_palindromes(self.text)
            self.algorithm_executed = True
        else:
            print("Сначала введите данные.")

    def find_palindromes(self, text):
        words = ''.join(char if char.isalnum() else ' ' for char in text).split()
        palindromes = [word for word in words if word == word[::-1]]
        return palindromes

    def print_result(self):
        if self.algorithm_executed:
            if self.palindromes:
                self.print_palindromes(self.palindromes)
            else:
                print("Палиндромы не найдены.")
        else:
            print("Сначала выполните алгоритм.")

    def print_palindromes(self, palindromes):
        print("Найденные палиндромы:")
        for palindrome in palindromes:
            print(palindrome)

    def exit_program(self):
        print("Программа завершена.")
        exit()

# Инвокер (Invoker)
class Invoker:
    def __init__(self):
        self.commands = {}

    def set_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name):
        if name in self.commands:
            self.commands[name].execute()
        else:
            print("Неверный выбор. Попробуйте снова.")

# Клиентский код
if __name__ == "__main__":
    receiver = PalindromeFinder()
    invoker = Invoker()

    invoker.set_command('1', InputDataCommand(receiver))
    invoker.set_command('2', ExecuteAlgorithmCommand(receiver))
    invoker.set_command('3', PrintResultCommand(receiver))
    invoker.set_command('4', ExitProgramCommand(receiver))

    while True:
        print("Меню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")
        invoker.execute_command(choice)