class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Creating book: {self.title} by {self.author}")

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
    