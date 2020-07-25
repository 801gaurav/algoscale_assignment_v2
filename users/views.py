from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from users.forms import UserForm,AllUsersForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()


            registered = True
            return render(request, 'login.html', {})

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'registered': registered} )




def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'dashboard.html', {})
            else:
                return HttpResponse("Your account is disabled")
        else:
            return render(request, 'register.html', {})


    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/login/')

def get_all_users(request):
    form = AllUsersForm()
    context = {'all_users':all_users}	
    return render(request,'/dashboard.html',context)




def del_user(request, username):    
    try:
        u = User.objects.get(username = username)
        u.delete()
        messages.success(request, "The user is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return render(request, 'dashboard.html')

    except Exception as e: 
        return render(request, 'dashboard.html',{'err':e.message})

    return render(request, 'dashboard.html') 
