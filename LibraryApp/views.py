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
