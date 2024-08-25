class  Library:

    def __init__(self):
        self.list_book = []
        
    
    def add_book(self, title_book, author_book): # добавляем книгу
        self.list_book.append({'title_book': title_book, 'author_book': author_book})
        return self
    
    def remove_book(self, title_book): # удаляем книгу
        for i in self.list_book:
            if i['title_book'] == title_book:
                self.list_book.remove(i)
                return self
        return self
    
    def __getitem__(self, index): # находим книгу по индуксу
        return self.list_book[index]

    def __contains__(self, title_book): # проверка библиотеки на наличие книги
        for i in self.list_book:
            if i['title_book'] == title_book:
                return True
        return False
        
library = Library()

library.add_book('Книга1', 'Автор1').add_book('Книга2', "Автор2").remove_book("Книга1").add_book('Книга 3', "Автор 3").add_book("Книга 4", "Автор 4")
print(library.list_book)

print(library[2])

print('Книга 7' in library)
