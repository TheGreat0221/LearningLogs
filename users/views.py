from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process compelted form.
        form = UserCreationForm(data=request.POST)
    #username has the appropriate characters, the passwords match,
    # and the user isn't trying to do anythign malicous in their submission
        if form.is_valid():
        #The save() method returns the newly created user object,
        # which we assign to new_user/
            new_user = form.save()
        # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

# Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)