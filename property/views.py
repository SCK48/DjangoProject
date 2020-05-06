from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import UserProfile
from product.models import Category
from property.models import Properties, PropertyForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
     'category': category,
     'profile': profile,
     }
    return render(request, 'user_property.html', context)

def addproperty(request):

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Properties()
            data.user_id = current_user.id
            #data.category = form.cleaned_data['category']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.price = form.cleaned_data['price']
            data.address = form.cleaned_data['address']
            data.room = form.cleaned_data['room']
            data.year = form.cleaned_data['year']
            data.sqm = form.cleaned_data['sqm']
            data.detail = form.cleaned_data['detail']
            data.save()
            messages.success(request, "Konut Eklendi!")
            url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
    return HttpResponse("Addproperty Failed")