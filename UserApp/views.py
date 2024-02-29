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

        if data:
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
    user = 'no user'

    if 'data' in request.session:
        current_user = request.session['data']
        print(current_user)
        user = UserModel.objects.get(Username=current_user)



    return render(request, 'Home.html',{'products': data,'user':user,'categories': dataa, 'girls': girls, 'boys': boys, 'toys': toys, 'accessories': accessories, 'stationary': stationary, 'footwear': footwear})


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

    if request.method == 'POST':
        search = request.POST.get('search')
        if 'selected_price' in request.POST:
            print(int(request.POST['selected_price']))
            data = ProductModel.objects.filter(Price=int(request.POST['selected_price']))
        if 'selected_discount' in request.POST:
            print(int(request.POST['selected_discount']))
            data = OfferModel.objects.filter(Discount=int(request.POST['selected_discount']))
        print(data.values())

    return render(request, "Category.html", {'products': data})


# def category(request, main_category_id):
#
#     if request.method == 'POST':
#         search = request.POST.get('search')
#         if 'selected_price' in request.POST:
#             print(int(request.POST['selected_price']))
#             data = ProductModel.objects.filter(Price__lt=int(request.POST['selected_price']))
#         if 'selected_discount' in request.POST:
#             print(int(request.POST['selected_discount']))
#             data = OfferModel.objects.filter(OfferModel_discount_lt=int(request.POST['selected_discount']))
#         data = data.prefetch_related('images')
#         print(data.values())
#     return render(request, 'category.html', {'category': data,  'products': data, })
#

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

def Address(request):
    if 'data' in request.session:
        username = request.session.get("data")

        if request.method == "POST":
            house_name = request.POST.get("House_Name")
            house_number = request.POST.get("House_Number")
            place = request.POST.get("Place")
            post = request.POST.get("Post")
            pin = request.POST.get("Pincode")
            landmark = request.POST.get("Landmark")
            print(house_name, house_number, place, post, pin, landmark)
            dataa= AddressModel()
            dataa.House_Name = house_name
            dataa.House_Number = house_number
            dataa.Place = place
            dataa.Post = post
            dataa.Pincode = pin
            dataa.Landmark = landmark
            dataa.User_id = UserModel.objects.get(Username=username)
            dataa.save()
            return redirect('/')

        return render(request, "Address.html")
    else:
        return redirect("/")


def address(request):
    return render(request,'Address.html')


def addcart(request,id):
    print("sdfghj")

    if 'data' in request.session:
        print("aaaaaaaaaaaaaaaaaaaaaa")
        username = request.session.get('data')
        data = CartModel.objects.filter(User_id=UserModel.objects.get(Username=username))
        dataa = CartModel.objects.filter(Product_id=ProductModel.objects.get(Product_id=id))
        print(data.values())
        return render(request, 'cart.html', {'cart': data,'cart':dataa})
    else:
        return redirect('/login')


# def myhome(request):
#     return render(request,'hhome.html')

def offer(request):
    events = OfferEventModel.objects.all()

    return render(request, 'offer.html', {'events': events})


def brand(requset):
    data = BrandModel.objects.all()

    return render(requset, 'Brand.html', {'brands': data})

def addressview(request):
    print("sbzxbb")
    if 'data' in request.session:
        print("aaaaaaaaaaaaaaaaaaaaaa")
        user=request.session['data']
        mydata= AddressModel.objects.filter(User_id=UserModel.objects.get(Username=user))
        print(mydata)
        return render(request,'addressview.html',{'mydata':mydata})
    else:
        return redirect('/login')


def editaddress(request,id):
    if 'data' in request.session:
        username = request.session.get("data")
        dataaa=AddressModel.objects.filter()

        if request.method == "POST":
            house_name = request.POST.get("House_Name")
            house_number = request.POST.get("House_Number")
            place = request.POST.get("Place")
            post = request.POST.get("Post")
            pin = request.POST.get("Pincode")
            landmark = request.POST.get("Landmark")
            print(house_name, house_number, place, post, pin, landmark)
            dataa= AddressModel.object.get(Address_id=id)
            dataa.House_Name = house_name
            dataa.House_Number = house_number
            dataa.Place = place
            dataa.Post = post
            dataa.Pincode = pin
            dataa.Landmark = landmark
            dataa.User_id = UserModel.objects.get(Username=username)
            dataa.save()
            return redirect('/')

        return render(request, "Address.html",{'dataaa':dataaa})
    else:
        return redirect("/")


# def view_address(request):
#     print('address Function called')
#
#     if 'user' in request.session:
#         # user = request.session['user ']
#         data = UserAddress.objects.filter(user_id=User.objects.get(email=request.session['user']))
#         return render(request, 'view_address.html', {'data': data})
#     else:
#         return redirect('/login')


def logout(request):
    try:
        del request.session['data']
    except:
        return redirect('login')
    return redirect('login')



def buy(request):

    return render(request,'Buy.html')

