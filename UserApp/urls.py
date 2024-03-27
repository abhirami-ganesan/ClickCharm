from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.myhome, name="home"),
    path('product/<int:id>',views.Product, name='product'),
    path('login/',views.login,name="login"),
    path('sign/',views.sign,name="sign"),
    # path('buynow/',views.buynow,name="buynow"),
    path('category/<int:id>',views.category,name="category"),
    path('profile/',views.profile,name="profile"),
    path('search/',views.search,name="search"),
    path('offer',views.offer,name="offer"),
    path('brand',views.brand),
    path('logout/',views.logout),
    path('address/',views.address,name="address"),
    path('addressview/',views.addressview,name="addressview"),
    path('deleteaddress/<int:Address_id>',views.dlt_address,name="deleteaddress"),
    path('mycart',views.mycart,name="mycart"),
    path('deletecart/<int:id>',views.deletecart,name="deletecart"),
    path('edit_address/<int:Address_id>', views.edit_address, name="edit_address"),
    path('viewaddress',views.view_address),
    path('view_brand/<int:id>',views.View_brand,name="view_brand"),


    path('buy',views.buy, name="buy"),
    path('payment',views.payment,name="payment"),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
