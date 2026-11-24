class publisher:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("publisher:",self.name)
class book(publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        print("publisher:", self.name)
        print("title:", self.title)
        print("author:", self.author)

class python(book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        print("publisher:",self.name)
        print("title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
        print("no_of_pages:",self.no_of_pages)
b=python("tech publications","python programming","john smith",450,320)
b.display()