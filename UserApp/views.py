from decimal import Decimal
from django.http import JsonResponse


from django.db.models import Q, IntegerField, DecimalField
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.db.models import Sum, F
from django.db.models import Sum
from django.contrib import messages


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def sign(request):
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        exists = UserModel.objects.filter(Username=username).exists()

        if exists:

            return redirect('sign')
        else:
            user = UserModel(Username=username,  Phone_Number=phone, Password=password)
            user.save()

            return redirect('login')
    return render(request, "Signup.html")

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


# def myhome(request):
#     print(request.method)
#     data = ProductModel.objects.prefetch_related('images').all()
#     girls = ProductModel.objects.prefetch_related('images').filter(
#         Main_category_id=MainCategoryModel.objects.get(Main_category='Girls Clothing'))
#     boys = ProductModel.objects.prefetch_related('images').filter(
#         Main_category_id=MainCategoryModel.objects.get(Main_category='Boys Clothing'))
#     toys = ProductModel.objects.prefetch_related('images').filter(
#         Main_category_id=MainCategoryModel.objects.get(Main_category='Toys & Games'))
#     accessories = ProductModel.objects.prefetch_related('images').filter(
#         Main_category_id=MainCategoryModel.objects.get(Main_category='Kids Accessories'))
#     stationary = ProductModel.objects.prefetch_related('images').filter(
#         Main_category_id=MainCategoryModel.objects.get(Main_category='Stationary'))
#     footwear = ProductModel.objects.prefetch_related('images').filter(
#         Main_category_id=MainCategoryModel.objects.get(Main_category='Footwear'))
#
    # dataa = MainCategoryModel.objects.all()
    # user = 'no user'
    #
    # if 'data' in request.session:
    #     current_user = request.session['data']
    #     print(current_user)
    #     user = UserModel.objects.get(Username=current_user)

#
#     return render(request, 'Home.html',
#                   {'products': data, 'user': user, 'categories': dataa, 'girls': girls, 'boys': boys, 'toys': toys,
#                    'accessories': accessories, 'stationary': stationary, 'footwear': footwear})





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
def myhome(request):
    categories = MainCategoryModel.objects.all()
    category_products = []

    # recently_viewed_product_ids = request.session.get('recently_viewed_products')[:4]
    #
    # # Fetch recently viewed products associated with the current user
    # recently_viewed_products = ProductModel.objects.filter(Product_id__in=recently_viewed_product_ids)
    # recently_viewed_ids = request.session.get('recently_viewed', [])
    #
    # # Fetch the recently viewed products from the database
    # recently_viewed_products = ProductModel.objects.filter(Product_id__in=recently_viewed_ids)

    username = request.session.get('data')

    # Fetch the recently viewed product IDs associated with the user from the session or cookie
    recently_viewed_ids = request.session.get(f'recently_viewed_{username}', [])

    # Fetch the recently viewed products from the database
    recently_viewed_products = ProductModel.objects.filter(Product_id__in=recently_viewed_ids)[:4]

    for category in categories:
        products = ProductModel.objects.filter(Main_category_id=category.Main_category_id)[:4]
        category_products.append({'category': category, 'products': products})
        dataa = MainCategoryModel.objects.all()
        user = 'no user'
        if 'data' in request.session:
            current_user = request.session['data']
            print(current_user)
            user = UserModel.objects.get(Username=current_user)




    return render(request, 'Home.html', {'category_products': category_products,'user':user,'categories':dataa,'recently_viewed_products': recently_viewed_products})


def Product(request, id):
    reviews = ReviewRatingModel.objects.filter(Product_id=id)

    data = ProductModel.objects.prefetch_related('images').filter(Product_id=id)
    print(data.values())
    dataa = ReviewRatingModel.objects.filter(Product_id=ProductModel.objects.get(Product_id=id)).first()
    print(dataa)


    if request.method == "POST":
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        dataa = ReviewRatingModel()
        dataa.Review = review
        dataa.Rating = rating

        dataa.User_id = UserModel.objects.get(Username=request.session["data"])
        dataa.Product_id = ProductModel.objects.get(Product_id=id)

        dataa.save()
        return redirect(f'/product/{id}')
    username = request.session.get('data')

    # Retrieve the recently viewed product IDs associated with the user from the session or cookie
    recently_viewed_ids = request.session.get(f'recently_viewed_{username}', [])

    # Add the current product ID to the recently viewed list if not already present
    if id not in recently_viewed_ids:
        recently_viewed_ids.append(id)
        # Limit the recently viewed list to a certain length if needed
        # Ensure you're storing only unique product IDs

    # Update the session or cookies with the updated recently viewed list
    request.session[f'recently_viewed_{username}'] = recently_viewed_ids

    # Render the product page with the product details


    return render(request, "Product.html", {'products': data, 'reviews': reviews})


def category(request, id):
    data = ProductModel.objects.prefetch_related('images').filter(Main_category_id=id)
    dataa = OfferModel.objects.filter(Product_id__in=data.values_list('Product_id', flat=True))


    print(data.values())


    if request.method == 'POST':
        search = request.POST.get('search')
        if 'selected_price' in request.POST:
            selected_price = int(request.POST['selected_price'])
            data = data.filter(Price__lte=selected_price)
            return render(request, "Category.html", {'products': data})
        if 'selected_discount' in request.POST:
            selected_discount = int(request.POST['selected_discount'])
            dataa = dataa.filter(Discount__lte=selected_discount)

            # Calculate discounted price for each product
            discounted_products = []
            for product in data:
                discounted_price = product.Price - (product.Price * selected_discount / 100)
                discounted_products.append({'product': product, 'discounted_price': discounted_price})

            return render(request, "Category.html",
                          {'productss': discounted_products, 'selected_discount': selected_discount})



    return render(request, "Category.html", {'products': data})


# def add_to_wishlist(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         liked = request.POST.get('liked')
#
#         # Convert 'liked' to boolean
#         liked = liked == 'true'
#
#         try:
#             # Check if the product is already in the wishlist
#             existing_entry = WishlistModel.objects.filter(User_id=request.user, Product_id=product_id).exists()
#
#             if liked:
#                 # If the product is not in the wishlist, add it
#                 if not existing_entry:
#                     WishlistModel.objects.create(User_id=request.user, Product_id=product_id)
#             else:
#                 # If the product is in the wishlist, remove it
#                 if existing_entry:
#                     WishlistModel.objects.filter(User_id=request.user, Product_id=product_id).delete()
#
#             return JsonResponse({'success': True})
#         except Exception as e:
#             print(e)
#             return JsonResponse({'success': False, 'error': str(e)})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method'})
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
            house_name = request.POST.get("housename")
            house_number = request.POST.get("houseno")
            place = request.POST.get("place")
            post = request.POST.get("post")
            pin = request.POST.get("pin")
            landmark = request.POST.get("landmark")
            print(house_name, house_number, place, post, pin, landmark)
            dataa = AddressModel()
            dataa.House_Name = house_name
            dataa.House_Number = house_number
            dataa.Place = place
            dataa.Post = post
            dataa.Pincode = pin
            dataa.Landmark = landmark
            dataa.User_id = UserModel.objects.get(Username=username)
            dataa.save()
            # return redirect('/addressview')

        return render(request, "Address.html")
    else:
        return redirect("/")


# def myhome(request):
#     return render(request,'hhome.html')

def offer(request):
    events = OfferEventModel.objects.all()

    return render(request, 'offer.html', {'events': events})

# def myhome(request):
#     home = ProductModel.objects.all()
#     return render(request, 'Home.html', {'home': home})


def brand(requset):
    data = BrandModel.objects.all()

    return render(requset, 'Brand.html', {'brands': data})


def addressview(request):
    print("sbzxbb")
    if 'data' in request.session:
        print("aaaaaaaaaaaaaaaaaaaaaa")
        user = request.session['data']
        mydata = AddressModel.objects.filter(User_id=UserModel.objects.get(Username=user))
        print(mydata)
        return render(request, 'addressview.html', {'mydata': mydata})
    else:
        return redirect('/login')


def editaddress(request, id):
    if 'data' in request.session:
        username = request.session.get("data")
        dataaa = AddressModel.objects.filter()

        if request.method == "POST":
            house_name = request.POST.get("House_Name")
            house_number = request.POST.get("House_Number")
            place = request.POST.get("Place")
            post = request.POST.get("Post")
            pin = request.POST.get("Pincode")
            landmark = request.POST.get("Landmark")
            print(house_name, house_number, place, post, pin, landmark)
            dataa = AddressModel.object.get(Address_id=id)
            dataa.House_Name = house_name
            dataa.House_Number = house_number
            dataa.Place = place
            dataa.Post = post
            dataa.Pincode = pin
            dataa.Landmark = landmark
            dataa.User_id = UserModel.objects.get(Username=username)
            dataa.save()
            return redirect('/addressview')

        return render(request, "Address.html", {'dataaa': dataaa})
    else:
        return redirect("/")


def logout(request):
    try:
        del request.session['data']
    except:
        return redirect('login')
    return redirect('login')


def mycart(request):
    if 'data' in request.session:
        username = request.session.get('data')
        User_id = UserModel.objects.get(Username=username)
        mydata = AddressModel.objects.filter(User_id=UserModel.objects.get(Username=username))
        print(mydata)


        if request.method == "POST":
            print('aaa')

            quantity = request.POST.get('qua')
            Product_id = request.POST.get('id')
            Product_details = ProductModel.objects.get(Product_id=Product_id)
            if not CartModel.objects.filter(Product_id=Product_details, User_id=User_id).exists():

                cartdata = CartModel(Product_id=Product_details, User_id=User_id, Quantity=quantity)
                cartdata.save()
                usercartdetails = CartModel.objects.filter(User_id=User_id)

                return render(request, 'mycart.html', {'user_products': usercartdetails})
            else:
                usercartdetails = CartModel.objects.filter(User_id=User_id)
                total_price = sum(item.Product_id.Price * item.Quantity for item in usercartdetails)

                return render(request, 'mycart.html', {'user_products': usercartdetails,'total_price': total_price,'mydata':mydata})
        else:
            usercartdetails = CartModel.objects.filter(User_id=UserModel.objects.get(Username=username))


            # total_price = usercartdetails.aggregate(
            #     total_price=Sum(F('Product_id__Price') * F('Quantity'), output_field=DecimalField()))['total_price']
            # total_price = total_price or Decimal('0')  # Handle None case

        return render(request, 'mycart.html', {'user_products': usercartdetails})
    else:
        return redirect('/login')




def buy(request):
    if 'data' in request.session:
        print("aaaaaaaaaaaaaaaaaaaaaa")
        user = request.session['data']
        mydata = AddressModel.objects.filter(User_id=UserModel.objects.get(Username=user))
        print(mydata)
        username = request.session.get('data')
        User_id = UserModel.objects.get(Username=username)

        if request.method == "POST":
            print('aaa')

            quantity = request.POST.get('qua')
            Product_id = request.POST.get('id')
            Product_details = ProductModel.objects.get(Product_id=Product_id)
            if not CartModel.objects.filter(Product_id=Product_details, User_id=User_id).exists():

                cartdata = CartModel(Product_id=Product_details, User_id=User_id, Quantity=quantity)

                usercartdetails = CartModel.objects.filter(User_id=User_id)

                return render(request, 'buy.html', {'buy': usercartdetails})
            else:
                usercartdetails = CartModel.objects.filter(User_id=User_id)
                total_price = sum(item.Product_id.Price * item.Quantity for item in usercartdetails)

                return render(request, 'buy.html', {'buy': usercartdetails, 'total_price': total_price,'mydata':mydata})
        else:
            usercartdetails = CartModel.objects.filter(User_id=UserModel.objects.get(Username=username))

            # total_price = usercartdetails.aggregate(
            #     total_price=Sum(F('Product_id__Price') * F('Quantity'), output_field=DecimalField()))['total_price']
            # total_price = total_price or Decimal('0')  # Handle None case

        return render(request, 'buy.html.html', {'buy': usercartdetails})
    else:
        return redirect('/login')

    return render(request, 'Buy.html')


def deletecart(request, id):
    cart = CartModel.objects.filter(Cart_id=id)
    cart.delete()
    return redirect('/mycart')
    # messages.success(request, 'Product deleted from cart successfully.')


def view_address(request):
    print('address Function called')
    if 'data' in request.session:
        data = AddressModel.objects.filter(User_id=UserModel.objects.get(Username=request.session['data']))
        return render(request, 'addressview.html', {'data': data})
    else:
        return redirect('/login')


def address(request):
    if 'data' in request.session:
        username = request.session.get('data')
        print(username)
        if request.method == "POST":
            housename = request.POST.get('housename')
            houseno = request.POST.get('houseno')
            place = request.POST.get('place')
            post = request.POST.get('post')
            pin = request.POST.get('pin')
            landmark = request.POST.get('landmark')
            print(housename)
            print(UserModel.objects.filter(Username=username))
            data = AddressModel()
            data.House_Name = housename
            data.House_Number = houseno
            data.Place = place
            data.Post = post
            data.Pincode = pin
            data.Landmark = landmark
            data.User_id = UserModel.objects.get(Username=username)
            data.save()
            print("Address successfully  added  .............!")
            return redirect('/addressview')
        return render(request, 'Address.html')
    else:
        return redirect('login')


def edit_address(request, Address_id):
    dataa = AddressModel.objects.filter(Address_id=Address_id)
    if 'data' in request.session:
        username = request.session.get('data')
        if request.method == 'POST':
            House_Name = request.POST.get('housename')
            House_Number = request.POST.get('houseno')
            Place = request.POST.get('place')
            Post = request.POST.get('post')
            Pincode = request.POST.get('pin')
            Landmark = request.POST.get('landmark')
            print(Address_id, House_Name, House_Number, Place, Post, Pincode, Landmark)
            data = AddressModel.objects.get(Address_id=Address_id)
            data.House_Name = House_Name
            data.House_Number = House_Number
            data.Place = Place
            data.Post = Post
            data.Pincode = Pincode
            data.Landmark = Landmark
            data.User_id = UserModel.objects.get(Username=username)
            data.save()
            print("Address successfully  added .............!")
            return redirect('/addressview')

        return render(request, 'edit_address.html', {'dataa': dataa})
    else:
        return redirect('login')


def dlt_address(request, Address_id):
    print("rtttttttttttttttttttttttttttttt")
    data = AddressModel.objects.get(Address_id=Address_id)
    data.delete()
    return redirect('/addressview')


# def View_brand(request, id):
#     data = ProductModel.objects.filter(Brand_id=BrandModel.objects.get(Brand_id=id))
#     return render(request, 'View_Brand.html', {'data': data})

def View_brand(request, id):
    data = ProductModel.objects.prefetch_related('images').filter(Brand_id=id)

    print(data.values())
    return render(request, 'View_Brand.html', {'data': data})


# def View_brand(request):
#     events = OfferEventModel.objects.all()
#
#     return render(request, 'offer.html', {'events': events})
#

# def add_to_wishlist(request):
#     if request.method == 'POST' and request.is_ajax():
#         product_id = request.POST.get('product_id')
#         # Assuming the user is authenticated and stored in request.user
#         if 'data' in request.session:
#             wishlist_item = WishlistModel.objects(Userid=UserModel.objects.get(Username=request.session['data']), Product_id=ProductModel.objects.get(Product_id=product_id))
#
#             return JsonResponse({'success': True, 'message': 'Product added to wishlist.'})
#         else:
#
#             return JsonResponse({'success': False, 'message': 'Product already in wishlist.'})
#     return JsonResponse({'success': False, 'message': 'Invalid request.'})
#



def add_to_wishlist(request):
    if request.method == 'POST' and request.is_ajax():
        productId = request.POST.get('productId')
        wishlistStatus = request.POST.get('wishlistStatus')

        # Logic to add/remove the product to/from the wishlist model
        # Example:
        # Check if the product is already in the wishlist and toggle it
        # Add your own logic according to your requirements

        return JsonResponse({'success': True, 'wishlistStatus': 'added/removed'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

def payment(request):
    return render(request,'Payment.html')

