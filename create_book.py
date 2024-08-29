from services.books_service import BookService

book_name = input("Book Name: ")
amazon_link = input("Amazon Link: ")

book = BookService.create_book(book_name, amazon_link)


