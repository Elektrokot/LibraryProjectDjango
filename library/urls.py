from django.urls import path
from .views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView, AuthorCreateView, \
    AuthorUpdateView, AuthorListView, RecommendBookView, ReviewBookView

app_name = 'library'


urlpatterns = [
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('books/', BookListView.as_view(), name='books_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('book/recommend/<int:pk>/', RecommendBookView.as_view(), name='recommend_book'),
    path('book/review/<int:pk>/', ReviewBookView.as_view(), name='review_book'),

    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/', AuthorListView.as_view(), name='authors_list'),
]
