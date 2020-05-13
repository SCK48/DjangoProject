import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormMessage, ContactFormu, UserProfile, FAQ
from product.models import Product, Category, Images, Comment
from property.models import Properties, PropetyComment, Galeri


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Properties.objects.all().order_by('?')[:4]
    category = Category.objects.all()
    randomproducts = Properties.objects.all().order_by('?')[:6]
    relatedproducts = Product.objects.all().order_by('-id')[:3]
    newproperties = Properties.objects.filter(status='True').order_by('-id')[:3]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'randomproducts': randomproducts,
               'relatedproducts': relatedproducts,
               'newproperties': newproperties
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()

    context = {'setting': setting, 'category': category, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()

    context = {'setting': setting, 'category': category, 'page': 'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkürler")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'form': form}
    return render(request, 'iletisim.html', context)



def category_products(request,id,slug):
    sliderdata = Properties.objects.all()[:4]
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id, status='True')
    propertys = Properties.objects.filter(category_id=id, status='True')
    context = {'products': products,
               'category': category,
               'sliderdata': sliderdata,
               'categorydata': categorydata,
               'propertys':propertys,
               }
    return render(request, 'products.html', context)




def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    relatedproducts = Product.objects.all().order_by('-id')[:3]
    comments = Comment.objects.filter(product_id = id, status ='True')
    context = {'category': category,
               'product': product,
               'images': images,
               'relatedproducts': relatedproducts,
               'comments': comments,
               }
    return render(request, 'product_detail.html', context)


def product_search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            sliderdata = Properties.objects.all()[:4]
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Properties.objects.filter(title__icontains=query)
            else:
                products = Properties.objects.filter(title__icontains=query, category_id=catid)
            #return HttpResponse(products)
            context = { 'products': products,
                        'category': category,
                        'sliderdata': sliderdata,
                        }
            return render(request, 'products_search.html', context)
    return HttpResponseRedirect('/')


def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Properties.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Kullanıcı adı veya Şifre yanlış!")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category':category,
                }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    context = {'category':category,
               'form': form,
               }
    return render(request, 'signup.html', context)

#def property(request):
    #category = Category.objects.all()
    #current_user = request.user
    #profile = UserProfile.objects.get(user_id=current_user.id)
    #context = {
        #'category': category,
        #'profile': profile,
    #}
    #return render(request, 'user_property.html', context)


def property_detail(request,id,slug):
    category = Category.objects.all()
    property = Properties.objects.get(pk=id)
    images = Galeri.objects.filter(property_id=id)
    newproperties = Properties.objects.filter(status='True').order_by('-id')[:3]
    comments = PropetyComment.objects.filter(property_id=id, status='True')
    context = {'category': category,
               'property': property,
               'images': images,
               'newproperties': newproperties,
               'comments': comments,
               }
    return render(request, 'property_detail.html', context)


def faq(request):
    category = Category.objects.all()
    newproperties = Properties.objects.filter(status='True').order_by('-id')[:3]
    faq = FAQ.objects.all().order_by('ordernumber')
    context = {'category': category,
               'newproperties': newproperties,
               'faq': faq,
               }
    return render(request, 'faq.html', context)