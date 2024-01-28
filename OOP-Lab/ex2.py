
class Book():
        
    def __init__(self):
        pass

    def view(self, title, author, price):
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Price: ${price}")


book_instance = Book()

print(book_instance.view("Interstellar", "Christopher Nolan", 59))