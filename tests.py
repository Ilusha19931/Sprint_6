import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize("book_name", [
        "",
        "12345678901234567890123456789012345678901234"
    ])
    def test_add_new_book_invalid_book_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_set_book_genre_valid_name_add_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Светлое будущее")
        collector.set_book_genre("Светлое будущее", "Фантастика")
        assert collector.get_book_genre("Светлое будущее") == "Фантастика"

    def test_set_book_genre_invalid_unnamed(self):
        collector = BooksCollector()
        collector.set_book_genre("Некрономикон", "Фантастика")
        assert collector.get_book_genre("Некрономикон") is None

    def test_get_books_with_specific_genre_valid_add_in_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Ужасная книга")
        collector.set_book_genre("Ужасная книга", "Ужасы")
        collector.add_new_book("Приключенческая книга")
        collector.set_book_genre("Приключенческая книга", "Комедии")

        assert collector.get_books_with_specific_genre("Ужасы") == ["Ужасная книга"]
        assert collector.get_books_with_specific_genre("Комедии") == ["Приключенческая книга"]
        assert collector.get_books_with_specific_genre("Фантастика") == []

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Ужасно")
        collector.set_book_genre("Ужасно", "Ужасы")
        collector.add_new_book("Детская Книга")
        collector.set_book_genre("Детская Книга", "Фантастика")

        assert collector.get_books_for_children() == ["Детская Книга"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Тестовая Книга")
        collector.add_book_in_favorites("Тестовая Книга")
        assert "Тестовая Книга" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_valid_deleted_name(self):
        collector = BooksCollector()
        collector.add_new_book("Тестовая Книга")
        collector.add_book_in_favorites("Тестовая Книга")
        collector.delete_book_from_favorites("Тестовая Книга")
        assert "Тестовая Книга" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_included_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Тестовая Книга")
        collector.add_book_in_favorites("Тестовая Книга")
        collector.add_new_book("Тестовая Книга2")
        collector.add_book_in_favorites("Тестовая Книга2")
        assert collector.get_list_of_favorites_books() == ["Тестовая Книга","Тестовая Книга2"]
