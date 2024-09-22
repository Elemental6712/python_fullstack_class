from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self, data: str):
        pass

class TextFileHandler(FileHandler):
    def __init__(self, check_file):
        self.check_file = check_file
    
    def read(self):
        with open(self.check_file, 'r') as file:
            text_file = file.read()
            print(f'Файл прочитан: {text_file}')
    
    def write(self, data: str):
        with open(self.check_file, 'w') as file:
            file.write(data)
            print(f'Запись была сделана')
    
class BinaryFileHandler(FileHandler):
    def __init__(self, check_file):
        self.check_file = check_file
    
    def read(self):
        with open(self.check_file, 'rb') as file:
            text_file = file.read()
            print(f"Файл был прочитан: {text_file}")
    
    def write(self, text):
        with open(self.check_file, "wb") as file:
            file.write(text.encode('utf-8'))
            print('Запись была сделана.')

def save_data(handler: FileHandler, data: str):
    handler.write(data)
    handler.read()


text = TextFileHandler("check file.txt")
binary = BinaryFileHandler('check file.bin')
save_data(text, 'Какая-то информация...')
save_data(binary, 'Какая-то информация...')



"""Задание 2: Работа с файлами (Использование протоколов)
Создайте протокол FileHandler с методами read() и write(data: str).
Реализуйте два класса, TextFileHandler и BinaryFileHandler, которые реализуют этот протокол.
TextFileHandler должен читать и писать текстовые файлы, а BinaryFileHandler — бинарные файлы. В реализации не обязательно действительно использовать файлы, но вы можете добавить такой функционал. В качестве решения достаточно вывести информацию, что файл был прочитан и записан
Создайте функцию save_data(handler: FileHandler, data: str), которая сохраняет данные, используя переданный "обработчик файлов"."""

