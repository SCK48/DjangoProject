from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from product.models import Category, Comment
from property.models import Properties, Galeri, PropetyComment, PropertyForm
from user.forms import UserUpdateForm, ProfileUpdateForm, PropertyUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'category' : category,
        'profile' : profile,
    }
    return render(request,'user_profile.html',context)

@login_required(login_url='/login')
def user_update(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile has been updated')
            return redirect('/user')
    else:
        category =Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category' : category,
            'user_form' : user_form,
            'profile_form' : profile_form,
            'profile': profile,
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login')
def change_password(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password successfully Changed')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form=PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form,
            'category': category,
            'profile': profile,
        })

@login_required(login_url='/login')
def properties(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    properties = Properties.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'profile': profile,
        'properties': properties,
    }
    return render(request, 'user_properties.html', context)

@login_required(login_url='/login')
def propertydetail(request,id):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    properties = Properties.objects.get(user_id=current_user.id, id=id)
    propertyitem = Properties.objects.filter(id=id)
    images = Galeri.objects.filter(property_id=id)
    context = {
        'category': category,
        'profile': profile,
        'properties': properties,
        'propertyitem': propertyitem,
        'images': images,
    }
    return render(request, 'user_property_detail.html', context)

@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    comments = Comment.objects.filter(user_id=current_user.id)
    propertycomments = PropetyComment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'profile': profile,
        'comments': comments,
        'propertycomments': propertycomments,
    }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login')
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    PropetyComment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Your Comment has been deleted')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login')
def propertyedit(request,id):
    properties = Properties.objects.get(id=id)
    if request.method == 'POST':
        form = PropertyUpdateForm(request.POST, request.FILES,instance=properties)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Property successfully Upated')
            return HttpResponseRedirect('/user/propertydetail/'+str(id))
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/propertyedit/'+str(id))
    else:
        form = PropertyUpdateForm(instance=properties)
        category = Category.objects.all()
        context = {
            'category': category,
            'form': form,
            'properties': properties,
        }
        return render(request, 'user_propertyedit.html', context)

@login_required(login_url='/login')
def propertydelete(request, id):
    current_user = request.user
    Properties.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Property Deleted!')
    return HttpResponseRedirect('/user/properties')