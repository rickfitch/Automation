from books import Book


class Ebook(Book):
    def __init__(self, title, author, format_):
        super().__init__(title, author)
        self.format_ = format_
        print(f"Creating ebook: {self.title} by {self.author} in {self.format_}")

    def __str__(self):
        return f"{self.title} by {self.author} in {self.format_}"

    def __repr__(self):
        return f"<Ebook {self.title} by {self.author} in {self.format_}>"
    
    def reading(self):
        super().reading()
        print(f"info: {self.title} by {self.author} in {self.format_}")

