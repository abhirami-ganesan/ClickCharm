from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from .models import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        data = UserModel.objects.filter(Username=username, Password=password)

        if data is not None:
            print(username)
            request.session['data'] = username
            print('login successfully..............')
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def myhome(request):
    print(request.method)
    data = ProductModel.objects.prefetch_related('images').all()
    girls = ProductModel.objects.prefetch_related('images').filter(
        Main_category_id=MainCategoryModel.objects.get(Main_category='Girls Clothing'))
    boys = ProductModel.objects.prefetch_related('images').filter(
        Main_category_id=MainCategoryModel.objects.get(Main_category='Boys Clothing'))
    toys = ProductModel.objects.prefetch_related('images').filter(
        Main_category_id=MainCategoryModel.objects.get(Main_category='Toys & Games'))
    accessories = ProductModel.objects.prefetch_related('images').filter(
        Main_category_id=MainCategoryModel.objects.get(Main_category='Kids Accessories'))
    stationary = ProductModel.objects.prefetch_related('images').filter(
        Main_category_id=MainCategoryModel.objects.get(Main_category='Stationary'))
    footwear = ProductModel.objects.prefetch_related('images').filter(
        Main_category_id=MainCategoryModel.objects.get(Main_category='Footwear'))

    dataa = MainCategoryModel.objects.all()

    return render(request, 'Home.html',
                  {'products': data, 'categories': dataa, 'girls': girls, 'boys': boys, 'toys': toys,
                   'accessories': accessories, 'stationary': stationary, 'footwear': footwear})


def search(request):
    print("rrrrrrrrr")
    data = ProductModel.objects.prefetch_related('images').all()
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            data = ProductModel.objects.filter(
                Q(Product_title__icontains=search) | Q(Product_description__icontains=search) | Q(
                    Quantity__icontains=search) | Q(Price__icontains=search))
            print(search)
            return render(request, 'search.html', {'products': data})


def Product(request, id):
    data = ProductModel.objects.prefetch_related('images').filter(Product_id=id)
    print(data.values())
    dataa = ReviewRatingModel.objects.filter(Review_id=id)

    return render(request, "Product.html", {'products': data, 'review': dataa})


def category(request, id):
    data = ProductModel.objects.prefetch_related('images').filter(Main_category_id=id)
    print(data.values())
    return render(request, "Category.html", {'products': data})


# def addcart(request,id):
#     if 'data' in request.session:
#         data = ProductModel.objects.filter(Product_id=id)
#         return render(request,"Cart.html",{'data':data})
#     else:
#         return redirect('/login')


# def buynow(request):
#     if 'data' in request.session:
#         return HttpResponse("This is for buy data")
#     else:
#         return redirect('/login')


def profile(request):
    if 'data' in request.session:
        print(request.session["data"])
        username = request.session["data"]
        dataa = UserModel.objects.filter(Username=username)
        image = UserImageModel.objects.filter(User_id=UserModel.objects.get(Username=username)).first()

        print(dataa.values())

        return render(request, "Profile.html", {'profile': dataa, 'image': image})
    else:
        return redirect('/login')


def addcart(request):
    print("sdfghj")

    if 'data' in request.session:
        print("aaaaaaaaaaaaaaaaaaaaaa")
        username = request.session.get('data')
        data = CartModel.objects.filter(User_id=UserModel.objects.get(Username=username))
        print(data.values())
        return render(request, 'cart.html', {'cart': data})
    else:
        return redirect('/login')


# def myhome(request):
#     return render(request,'hhome.html')

def offer(request):
    data = OfferEventModel.objects.filter(Offer_Name='Holi')
    dataa = OfferModel.objects.filter(Offer_id=OfferEventModel.objects.get(Offer_Name='Holi'))
    print(data.values())

    return render(request, 'offer.html', {'events': data, 'offer': dataa})


def brand(requset):
    data = BrandModel.objects.all()

    return render(requset, 'Brand.html', {'brands': data})
