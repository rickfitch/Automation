from books import Book
from ebooks import Ebook

book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
print(f" Title: {book1.title},   Author: {book1.author}")
print(f" Title: {book2.title},   Author: {book2.author}")
print(f" Title: {book3.title},   Author: {book3.author}")
book2.reading()
ebook1 = Ebook("The Boy in the Bubble", "RFitch", "PDF")
ebook1.reading()