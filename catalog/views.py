from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/book_detail.html', context={'book': book})


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter()[:5] # Get 5 books containing the title war
    template_name = 'books/book_list.html'  # Specify your own template name/location
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    
    
class BookDetailView(generic.DetailView):
    model = Book    
    
class AuthorListView(generic.ListView):   
    model = Author
    context_object_name = 'author_list'
    template_name = 'books/author_list.html'
    
    paginate_by = 10
    def get_book_queryset(self):
        return Book.objects.filter()[:5]
    
class AuthorDetailView(generic.DetailView):    
    model = Author
    
    
    
    
    