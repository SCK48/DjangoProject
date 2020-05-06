from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from product.models import CommentForm, Comment #PropertyForm, Product


def index(request):
    return HttpResponse("Product Page")

@login_required(login_url='/login')
def addcomment(request,id):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user
            data = Comment()
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks for your comment!")
            url =request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
    return HttpResponse("Comment Failed")


#def addproperty(request,id):

    #if request.method == 'POST':
        #form = PropertyForm(request.POST)
        #if form.is_valid():
            #data = Product()
            #data.description = id
            #data.category = form.cleaned_data['category']
            #data.title = form.cleaned_data['title']
            #data.keywords = form.cleaned_data['keywords']
            #data.image = form.cleaned_data['image']
            #data.price = form.cleaned_data['price']
            #data.amount = form.cleaned_data['amount']
            #data.detail = form.cleaned_data['detail']
            #data.save()
            #messages.success(request, "Konut Eklendi!")
            #return HttpResponseRedirect('/user')
    #return HttpResponse("Addproperty Failed")
