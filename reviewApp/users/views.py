from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Acount created for {username}!')
		return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
	u_form = UserUpdateForm()
	p_form = ProfileUpdateForm()

	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

		if u_form.is_valid():
			u_form.save()
			message.success(request, f'User details have been edited')

			return redirect('profile')

		if p_form.is_valid():
			p_form.save()
			message.success(request, f'Account details have been edited')

			return redirect('profile')
	
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {
			'u_form': u_form,
			'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)