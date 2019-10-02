from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre, Language

def index(request):
	"""View function for the home page of site"""

	# Generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	# Available books
	num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

	# The 'all()' is implied buy default.
	num_authors = Author.objects.count()

	# Number of visits to this view, as per the session variable
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors, 
		'num_visits': num_visits,
	}

	# render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
	model = Book
	paginate_by = 5
	# access page with ?page=2

class BookDetailView(generic.DetailView):
	model = Book

class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 5

class AuthorDetailView(generic.DetailView):
	model = Author
