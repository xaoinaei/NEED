from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced



# def home(request):
#   return render(request, 'app/home.html')

class ProductView(View):
  def get(self, request):
      party = Product.objects.filter(category="P")
      daily = Product.objects.filter(category="D")
      onesight = Product.objects.filter(category="OS")
      styla = Product.objects.filter(category="S")
      special = Product.objects.filter(category="U")
      heels = Product.objects.filter(category="H")
      return render(request, 'app/home.html',{
        'party': party, 
        'daily': daily,
        'onesight': onesight,
        'styla': styla,
        'special': special,
        'heels': heels
        }
      )




#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product} )


def add_to_cart(request):
  return render(request, 'app/addtocart.html')

def buy_now(request):
  return render(request, 'app/buynow.html')

def profile(request):
  return render(request, 'app/profile.html')

def address(request):
  return render(request, 'app/address.html')

def orders(request):
  return render(request, 'app/orders.html')

def change_password(request):
  return render(request, 'app/changepassword.html')

def partyo(request, data=None):
  if data == None:
    party = Product.objects.filter(category='P')
  elif data == 'Top' or data == 'Set' :
    party = Product.objects.filter(category='P').filter(brand=data)
  elif data =='below':
    party = Product.objects.filter(category='P').filter(discounted_price__lt=1500)
  elif data == 'above':
    party = Product.objects.filter(category='P').filter(discounted_price__gt=1500)
  return render(request,'app/partyo.html', {'party':party} )


def dailyd(request, data=None):
  if data == None:
    daily = Product.objects.filter(category='D')
  elif data == 'des' or data == 'vani' :
    daily = Product.objects.filter(category='D').filter(brand=data)
  elif data =='below':
    daily = Product.objects.filter(category='D').filter(discounted_price__lt=1500)
  elif data == 'above':
    daily = Product.objects.filter(category='D').filter(discounted_price__gt=1500)
  return render(request,'app/dailyd.html', {'daily':daily} )



def onesightf(request, data=None):
  if data == None:
    onesight = Product.objects.filter(category='OS')
  elif data == 'des' or data == 'vani' :
    onesight = Product.objects.filter(category='OS').filter(brand=data)
  elif data =='below':
    onesight = Product.objects.filter(category='OS').filter(discounted_price__lt=1500)
  elif data == 'above':
    onesight = Product.objects.filter(category='OS').filter(discounted_price__gt=1500)
  return render(request,'app/onesightf.html', {'onesight':onesight} )

def stylaf(request, data=None):
  if data == None:
    styla = Product.objects.filter(category='S')
  elif data == 'des' or data == 'vani' :
    styla = Product.objects.filter(category='S').filter(brand=data)
  elif data =='below':
    styla = Product.objects.filter(category='S').filter(discounted_price__lt=1500)
  elif data == 'above':
    styla = Product.objects.filter(category='S').filter(discounted_price__gt=1500)
  return render(request,'app/stylaf.html', {'styla':styla} )

def heelsh(request, data=None):
  if data == None:
    heels = Product.objects.filter(category='H')
  elif data == 'des' or data == 'vani' :
    heels = Product.objects.filter(category='H').filter(brand=data)
  elif data =='below':
    heels = Product.objects.filter(category='H').filter(discounted_price__lt=1500)
  elif data == 'above':
    heels = Product.objects.filter(category='H').filter(discounted_price__gt=1500)
  return render(request,'app/heelsh.html', {'heels':heels} )

def specialf(request, data=None):
  if data == None:
    special = Product.objects.filter(category='U')
  elif data == 'des' or data == 'vani' :
    special = Product.objects.filter(category='U').filter(brand=data)
  elif data =='below':
    special = Product.objects.filter(category='U').filter(discounted_price__lt=1500)
  elif data == 'above':
    special = Product.objects.filter(category='U').filter(discounted_price__gt=1500)
  return render(request,'app/specialf.html', {'special':special} )


def login(request):
  return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')


def checkout(request):
  return render(request, 'app/checkout.html')
