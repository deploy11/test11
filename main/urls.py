from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('savol-javol/',savol,name='savol'),
    path('javob/<int:id>/',javob,name='javob'),
    path('books/',books,name='bok'),
    path('books/<int:id>/',details_book,name='details_book'),
    path('books/sif_category/',book_class,name='book_class'),
    path('yangiliklar/',yangilik,name='yangilik'),
    path('yangilik/<int:id>?/',blog_details,name='detailts_blog')
]