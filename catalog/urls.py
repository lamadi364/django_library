
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<str:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'), 
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'), 
    path('borrowed/', permission_required("catalog.can_mark_returned")(views.LoanedBooksByLibrarianListView.as_view()), name='all-borrowed'), 
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


