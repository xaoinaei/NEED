from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('', views.home),

   path('',views.ProductView.as_view(),name="home"),

   path('product-detail/<int:pk>', views.ProductDetailView.as_view(),name='product-detail'),
  
   path('cart/', views.add_to_cart, name='add-to-cart'),
   path('buy/', views.buy_now, name='buy-now'),
   path('profile/', views.profile, name='profile'),
   path('address/', views.address, name='address'),
   path('orders/', views.orders, name='orders'),
   path('changepassword/', views.change_password, name='changepassword'),
    
   path('party/', views.partyo, name='partyo'),
   path('party/<slug:data>', views.partyo, name='partyodata'),

   path('daily/', views.dailyd, name='dailyd'),
   path('daily/<slug:data>', views.dailyd, name='dailyddata'),

   path('onesight/', views.onesightf, name='onesightf'),
   path('onesight/<slug:data>', views.onesightf, name='onesightfdata'),

   path('styla/', views.stylaf, name='stylaf'),
   path('styla/<slug:data>', views.stylaf, name='stylafdata'),

   path('heels/', views.heelsh, name='heelsh'),
   path('heels/<slug:data>', views.heelsh, name='heelshdata'),

   path('special/', views.specialf, name='specialf'),
   path('special/<slug:data>', views.specialf, name='specialfdata'),

   
   path('registration/', views.customerregistration, name='customerregistration'),
   path('login/', views.login, name='login'),
   path('checkout/', views.checkout, name='checkout'),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
