from django.shortcuts import render
from django.shortcuts import HttpResponse

user_list=[]

# Create your views here.
def index(request):
    #return HttpResponse("hello world===========")
    return render(request,'index.html')

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    temp = {'user': username, 'pwd': password}
    user_list.append(temp)
    print(username+",,,"+password)
    return render(request,"welcome.html", {'data': user_list})




