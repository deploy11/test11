from django.shortcuts import render,redirect
from .forms import *
from .models import *
from hitcount.views import get_hitcount_model
from hitcount.views import HitCountMixin
# Create your views here.
def home(request):
    book_class = Books.objects.all()
    images = ProductImage.objects.all()
    return render(request,'home.html',{'b_class':book_class,'ima':images})
def savol(request):
    book_class = Books.objects.all()
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()

    form = DweetForm()
    savollar = Comment.objects.all().order_by('-id')
    return render(request,'savol.html',{'form':form,'sav':savollar,'b_class':book_class})

def javob(request,id):
    book_class = Books.objects.all()
    if request.method == "POST":
        Javob.objects.create(
            comments = id,
            names = request.POST['name'],
        )
    javob = Javob.objects.filter(comments = id)
    savollar = Comment.objects.filter(id=id)
    return render(request,'javob.html',{'jav':javob,'sav':savollar,'b_class':book_class})

def books(request):
    book_class = Books.objects.all()
    books = Books.objects.all().order_by('-id')
    return render(request,'books.html',{'bok':books,'b_class':book_class})
def details_book(request,id):
    book_class = Books.objects.all()
    books = Books.objects.get(id=id)
    return render(request,'books_details.html',{'bok':books,'b_class':book_class})

def book_class(request):
    book_class = Books.objects.all()
    qi = request.GET.get('id-r')
    books = Books.objects.filter(book_class = qi)
    return render(request,'books_sinf_cate.html',{'bok':books,'b_class':book_class})

def yangilik(request):   
    book_class = Books.objects.all()
    blog = Blog.objects.all()
    return render(request,'blog.html',{'blog':blog,'b_class':book_class})

def blog_details(request,id):
    book_class = Books.objects.all()
    blog = Blog.objects.get(id=id)
    image = ProductImage.objects.filter(product=id)
    hit_count = get_hitcount_model().objects.get_for_object(blog)
    hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request,hit_count)
    if hit_count_response.hit_counted:
        hits =+ 1
    return render(request,'blog_details.html',{'blog':blog,'ima':image,'b_class':book_class,'hits':hits})