from django.urls import path
from . import views

urlpatterns = [
    path('api/all_books',views.all_books,name='all_book'),
    path('api/add_book',views.add_book,name='add_book'),
    path('api/update_book/<int:id>',views.update_book,name='update_book'),
    path('api/delete_book/<int:id>',views.delete_book,name='delete_book'),
    path('api/search_book',views.search_book,name='search_book'),
]
