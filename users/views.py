from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # You can add a success message or redirect here if needed
            messages.success(request, f'{username} your account sign up was successful! Login to continue.')
            return redirect('login')
    else:
      form = UserRegisterForm()
    
    context = {'form': form, 'title':'Register'}
    return render(request, 'users/register.html', context=context)

@login_required
def profile(request):
    uForm = UserUpdateForm(instance=request.user)
    pForm = ProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)


    context = {'title':'Profile', 'uForm': uForm, 'pForm': pForm}
    return render(request, 'users/profile.html', context=context)



