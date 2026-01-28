class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

class Magazine:
    def __init__(self, title, issue, quantity):
        self.title = title
        self.issue = issue
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.books = {}
        self.magazines = {}

    def add_book(self, title, author, isbn, quantity):
        self.books[isbn] = Book(title, author, isbn, quantity)

    def add_magazine(self, title, issue, quantity):
        self.magazines[issue] = Magazine(title, issue, quantity)

    def update_quantity(self, item_type, identifier, quantity):
        if item_type == "BOOK" and identifier in self.books:
            self.books[identifier].quantity = quantity
        elif item_type == "MAGAZINE" and identifier in self.magazines:
            self.magazines[identifier].quantity = quantity

    def display(self):
        books_sorted = sorted(self.books.values(), key=lambda x: x.title)
        magazines_sorted = sorted(self.magazines.values(), key=lambda x: x.title)
        
        lines = ["Books:"]
        for book in books_sorted:
            lines.append(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Quantity: {book.quantity}")

        lines.append("Magazines:")
        for magazine in magazines_sorted:
            lines.append(f"Title: {magazine.title}, Issue: {magazine.issue}, Quantity: {magazine.quantity}")

        return "\n".join(lines)


def process_commands(n, commands):
    inventory = Inventory()
    output = []

    for command in commands:
        parts = command.split()
        if parts[0] == "ADD" and len(parts) >= 5:
            item_type = parts[1]
            if item_type == "BOOK" and len(parts) == 6:
                title, author, isbn, quantity = parts[2], parts[3], parts[4], int(parts[5])
                inventory.add_book(title, author, isbn, quantity)
            elif item_type == "MAGAZINE" and len(parts) == 5:
                title, issue, quantity = parts[2], parts[3], int(parts[4])
                inventory.add_magazine(title, issue, quantity)
        elif parts[0] == "UPDATE" and len(parts) == 4:
            item_type, identifier, quantity = parts[1], parts[2], int(parts[3])
            inventory.update_quantity(item_type, identifier, quantity)
        elif parts[0] == "DISPLAY" and len(parts) == 1:
            output.append(inventory.display())

    return "\n".join(output)