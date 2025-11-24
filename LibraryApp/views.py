from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import LibrarySerializer
from .models import Library

# Create your views here.


# show all books
@api_view(['GET'])
def all_books(request):
    library_books = Library.objects.all()
    serializer = LibrarySerializer(library_books, many = True)
    return Response(serializer.data)

# add books
@api_view(['POST'])
def add_book(request):
    is_many = isinstance(request.data, list)
    serializer = LibrarySerializer(data = request.data, many = is_many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# update book
@api_view(['POST'])
def update_book(request,id):
    book = Library.objects.get(id=id)
    serializer = LibrarySerializer(instance = book, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# delete a book
@api_view(['DELETE'])
def delete_book(request,id):
    book = get_object_or_404(Library,id=id)
    book.delete()
    return Response({"message":"Book deleted successfully"})


# METHOD 1: search a book by name using POST
@api_view(['POST'])
def search_book(request):
    book_name = request.data.get("book_name" , "")
    if not book_name:
        return Response({"error":"Please provide a valid book name"})
    book = Library.objects.filter(book_name__icontains=book_name)
    serializer = LibrarySerializer(book, many = True)
    if book.exists():
        return Response(serializer.data)
    return Response({"message":"No books found matching the search."})
    
# METHOD 2: search book by name using GET
@api_view(['GET'])
def search_books(request):
    book_name = request.GET.get("book_name", "")
    if not book_name:
        return Response({"error": "Please provide a valid book name"})
    books = Library.objects.filter(book_name__icontains=book_name)
    serializer = LibrarySerializer(books, many=True)
    if books.exists():
        return Response(serializer.data)
    return Response({"message": "No books found matching the search."})
