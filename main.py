#4-m
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def about(self):
        print(f"Kitob :{self.title}, Muallif :{self.author}")
        
s1 = Book("Python","Aliyev")
s1.about()

#5-m
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def display(self):
        print(f"User: {self.username}, Email: {self.email}")
        
s1 = User("admin", "admin@gmail.com")
s1.display()

#6-m
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        
    def show_popoulation(self):
        print(f"{self.name} aholisi {self.population}")
        
s1 = City("Toshkent", "3mln")
s1.show_popoulation()
