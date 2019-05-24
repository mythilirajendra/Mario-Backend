from django.shortcuts import render
from .forms import UserForm


def signup_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'index.html',
                          {'registered': registered, 'user_form': user_form, 'errors': user_form.errors})
