from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.myhome, name="home"),
    path('product/<int:id>',views.Product, name="product"),
    path('login/',views.login,name="login"),
    path('addcart',views.addcart,name="addcart"),
    # path('buynow/',views.buynow,name="buynow"),
    path('category/<int:id>',views.category,name="category"),
    path('profile/',views.profile,name="profile"),
    path('search/',views.search,name="search"),
    path('offer',views.offer,name="offer"),
    path('brand',views.brand),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
