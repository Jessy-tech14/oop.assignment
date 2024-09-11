# Class for Books
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."
    
book = Book("1984", "George Orwell", 328)
print(book.get_summary())