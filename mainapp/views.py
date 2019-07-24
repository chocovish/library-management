from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404
from .forms import RegistrationForm,BookAddForm
from .models import Book,User

from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'login.html')

def add_book(request):
    msg = ""
    if request.method=="POST":
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Book Added"
    return render(request,'book_add.html',{'form':BookAddForm(),"msg":msg})

def booklist(request):
    bl = Book.objects.filter(available=True)
    count = len(bl)
    return render(request,"list_book.html",{"bl":bl,"count":count})


def reviewuser(request):
    qs = User.objects.filter(verified=False)
    return render(request,'reviewuser.html',{'qs':qs})


def bookdue(request):
    qs = Book.objects.filter(borrow_date__lt=timezone.now()-timezone.timedelta(days=-1))
    print(qs)
    return render(request,'bookdue.html',{'qs':qs})


def aproveuser(request,pk):
    q = User.objects.get(pk=pk)
    q.verified = True
    q.save()
    return HttpResponseRedirect(reverse(reviewuser))

def deleteuser(request,pk):
    q = User.objects.get(pk=pk)
    q.delete()
    return HttpResponseRedirect(reverse(reviewuser))

def searchuser(request):
    roll = request.GET.get("roll",'')
    msg = ""
    if roll:
        try:
            u = User.objects.get(roll=roll)
        except: msg = "No user found belonging the roll"
        return render(request,'searchuser.html',{'u':u,'msg':msg})
    return render(request,'searchuser.html')

        
        




def searchbook(request):
    qs = {}
    q = request.GET.get('q','')
    try:
        pk = int(q)
        qs = Book.objects.filter(pk=pk)
    except ValueError:
        pass
    if not qs:
        qs = Book.objects.filter(name__contains=q)
    return render(request,'searchbook.html',{'qs':qs})


def renewbook(request,pk):
    q = get_object_or_404(Book,pk=pk)
    q.borrow_date = timezone.now()
    q.available = False
    q.save()
    return HttpResponse("Book Has Been Renewed")


def allotbook(request,pk):
    q = get_object_or_404(Book,pk=pk)
    msg = ""
    if request.method == "POST":
        roll = request.POST.get("roll","")
        try:
            u = User.objects.get(roll=roll)
            if not u.verified: return HttpResponse("Given User is not Verified yet.")
            q.borrower = u
            q.available = False
            q.borrow_date = timezone.datetime.date(timezone.now())
            q.save()
            msg = "Book Alloted SuccessFully"
        except:
            msg = "No user found belonging that roll number"
        return render(request,'allotbook.html',{"msg":msg,"q":q})
    return render(request,'allotbook.html',{"q":q})


def makeavailable(request,pk):
    q = get_object_or_404(Book,pk=pk)
    q.borrower = None
    q.available = True
    q.save()
    return HttpResponse("Book Successfully Returned And Marked As Availble")