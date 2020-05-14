from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import UserProfile
from product.models import Category, CommentForm
from property.models import Properties, PropertyForm, PropetyComment, Galeri, GaleriForm


def index(request):
    form = PropertyForm(request.POST, request.FILES)
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'category': category,
        'profile': profile,
        'form': form,
    }
    return render(request, 'user_property.html', context)

@login_required(login_url='/login')
def addproperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Properties()
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
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
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
    return HttpResponse("Addproperty Failed")

@login_required(login_url='/login')
def propertycomment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = PropetyComment()
            data.user_id = current_user.id
            data.property_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks for your comment!")
            url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
    return HttpResponse("Comment Failed")

@login_required(login_url='/login')
def addgaleri(request, id):
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES)
        if form.is_valid():
            data = Galeri()
            data.property_id = id
            data.image = form.cleaned_data['image']
            data.title = form.cleaned_data['title']
            data.save()
            messages.success(request, "Picture succesfully uploaded!")
            url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
        return HttpResponse("Upload Failed")
