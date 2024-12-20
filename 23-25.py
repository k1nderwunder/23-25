import random
import string

class State:
    def handle(self, context):
        pass

class InputState(State):
    def handle(self, context):
        context.text = context.input_data()
        context.palindromes = []
        context.algorithm_executed = False
        context.transition_to(MainMenuState())

class AlgorithmState(State):
    def handle(self, context):
        if context.text:
            context.palindromes = context.find_palindromes(context.text)
            context.algorithm_executed = True
            context.transition_to(MainMenuState())
        else:
            print("Сначала введите данные.")

class OutputState(State):
    def handle(self, context):
        if context.algorithm_executed:
            if context.palindromes:
                context.print_palindromes(context.palindromes)
            else:
                print("Палиндромы не найдены.")
        else:
            print("Сначала выполните алгоритм.")
        context.transition_to(MainMenuState())

class ExitState(State):
    def handle(self, context):
        context.exit_program()

class MainMenuState(State):
    def handle(self, context):
        print("Меню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            context.transition_to(InputState())
        elif choice == '2':
            context.transition_to(AlgorithmState())
        elif choice == '3':
            context.transition_to(OutputState())
        elif choice == '4':
            context.transition_to(ExitState())
        else:
            print("Неверный выбор. Попробуйте снова.")

class Context:
    def __init__(self, state):
        self.state = state
        self.text = ""
        self.palindromes = []
        self.algorithm_executed = False

    def transition_to(self, state):
        self.state = state
        self.state.handle(self)

    def input_data(self):
        print("Выберите способ ввода данных:")
        print("1. Ввести данные вручную")
        print("2. Сгенерировать данные случайным образом")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            text = input("Введите текст: ")
        elif choice == '2':
            text = self.generate_random_text()
        else:
            print("Неверный выбор. Попробуйте снова.")
            return self.input_data()

        return text

    def generate_random_text(self):
        words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7))) for _ in range(20)]
        return ' '.join(words)

    def find_palindromes(self, text):
        words = ''.join(char if char.isalnum() else ' ' for char in text).split()
        palindromes = [word for word in words if word == word[::-1]]
        return palindromes

    def print_palindromes(self, palindromes):
        print("Найденные палиндромы:")
        for palindrome in palindromes:
            print(palindrome)

    def exit_program(self):
        print("Программа завершена.")
        exit()

if __name__ == "__main__":
    context = Context(MainMenuState())
    while True:
        context.state.handle(context)