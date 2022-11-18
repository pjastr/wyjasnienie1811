class Book:

    def __init__(self, author, title, published_by, publish_house, publish_year):
        self.author = author
        self.title = title
        self.published_by = published_by
        self.publish_house = publish_house
        self.publish_year = publish_year

    def __repr__(self):
        return f"[{self.author},{self.title},{self.publish_year},{self.publish_house},{self.publish_year}]"

    def __lt__(self, other):
        ## sortowanie po tytule zgodnie z porządkiem leksykograficznym
        return self.title < other.title


books = [Book("Adam Mickiewicz", "Pan Tadeusz", "Znak", "Kraków", 2000),
         Book("Juliusz Słowacki", "Balladyna", "Znak", "Kraków", 2000)]
books.sort()
print(books)
