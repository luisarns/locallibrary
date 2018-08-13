from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    # Libros disponibles (status = 'a')
    num_instances_available = BookInstance.objects.filter(status='a').count()
    # El 'all()' esta implícito por defecto.
    num_authors = Author.objects.count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request, 'index.html', context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    })
