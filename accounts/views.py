from audioop import reverse
from django.shortcuts import redirect, render
#from django.contrib.auth.forms import UserCreationForm

from accounts.forms import CustomUserCreationform

# Create your views here.
#def register_view(request):
   # form =UserCreationForm()
   # if request.method=="POST":
    ##    form=UserCreationForm(request.POST)
      #  if form.is_valid:
       #     form.save()
        #    print("not valid")
        #    return redirect(reverse('registration/login.html'))
   # return render(request,'registration/register.html',{'form':form})
def register_view(request):
    form=CustomUserCreationform()
    print(CustomUserCreationform())
    if request.method=="POST":
        form=CustomUserCreationform(request.POST)
        if form.is_valid():
            form.save()
            print("successfull")
            return redirect('login')
    return render(request,'registration/register.html',{'form':form})
