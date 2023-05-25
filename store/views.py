from django.shortcuts import render,redirect
from .models import Product
from .models import Candidate

# Create your views here.

def index(requests):
    if requests.method=="GET":
        prod=Product.objects.all()
        context={
            'product':prod
        }
        return render(requests,'index.html',context)
    elif requests.method=="POST":
        product=requests.POST.get('product')
        cart=requests.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                cart[product]=quantity+1
            else:
                cart[product]=1

        else:
            cart={}
            cart[product]=1
        requests.session['cart']=cart
        print(requests.session['cart'])
        return redirect('index')


def signup(requests):
    if requests.method=="POST":
        user_name=requests.POST.get('user_name')
        contact=requests.POST.get('phone')
        image=requests.POST.get('image')
        email=requests.POST.get('email')
        password=requests.POST.get('password')

        ob1=Candidate.objects.create(user_name=user_name,contact=contact,image=image,email=email,password=password)
        if ob1:
            ob1.save() 
            return render(requests,'login.html')
        else:
            return render(requests,'signup.html')
    elif requests.method=='GET':
        return render(requests,'signup.html')

def login(requests):
    if requests.method=='POST':
        prod=Product.objects.all()
        context={
            'product':prod
        }
        email=requests.POST.get('email')
        password=requests.POST.get('password')
        ob1=Candidate.objects.get(email=email)
        if ob1:
            flag=ob1.password
            if flag==password:
                requests.session['user_id']=ob1.id
                requests.session['email']=ob1.email
                return render(requests,'index.html',context)
            else:
                return render(requests,'login.html')
        else:
            return render(requests,'login.html')
    elif requests.method=='GET':
        return render(requests,'login.html')
    

def cart(requests):
    data=requests.session.get('cart')
    context={
        'cart':data
    }
    return render(requests,'cart.html',context)