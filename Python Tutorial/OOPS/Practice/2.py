class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
        print("Review added successfully.")

    def count_reviews(self):
        print(f"Total Reviews: {len(self.reviews)}")

    def display_reviews(self):
        print("Reviews:")
        for review in self.reviews:
            print("-", review)


# Creating an object
book1 = Book("Python Programming", "Abhishek")

# Adding reviews
book1.add_review("Excellent book for beginners.")
book1.add_review("Easy to understand.")
book1.add_review("Very helpful examples.")

# Counting reviews
book1.count_reviews()

# Displaying all reviews
book1.display_reviews()