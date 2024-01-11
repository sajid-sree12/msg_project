from django.shortcuts import render
from django.contrib import messages
from starbucks.models import Coffee
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    if request.method=="POST":
        res=request.POST.get('password')
        res=res.replace(' ','')
        try:
            num=int(res)
            context={'number':num}
            messages.info(request,f"I changed number into integer {num}")
            return render(request,"home.html",context)
        except Exception as e:
            messages.error(request,f"{e}")
            return render(request,"home.html")
    return render(request,'home.html')

def get_coffees(request):
    c_records=Coffee.objects.all()
    context={'coffees':c_records}
    return render(request,'data.html',context)


def one_coffee(request):
    if request.method=="POST":
        sr=int(request.POST.get("search"))
        try:
            result=Coffee.objects.get(id=sr)
            context={'coffee':result}
            messages.success(request,"Successfully fetched data")
            return render(request,'coffee.html',context)
        except Exception as e:
            messages.error(request,e)
            return render(request,'coffee.html')
    else:
        return render(request,'coffee.html')


"""
def one_coffee(request):
    if request.method=="POST":
        sr=int(request.POST.get("search"))
        if Coffee.objects.filter(id=sr).exists():
            result=Coffee.objects.get(id=sr)
            context={'coffee':result}
        else:
            errr={'name':'Record Not Found','price':0}
            context={'coffee':errr}
        return render(request,'coffee.html',context)
    else:
        return render(request,'coffee.html')"""


def coffee(request,pk):
    result=Coffee.objects.get(id=pk)
    context={'coffee':result}
    return render(request,'coffee.html',context)




def get_users(request):
    result=User.objects.all()
    context={'users':result}
    return render(request,"coffee.html",context)


"""if len(res)>8:
            messages.success(request,"Good Your Passed is Strong")
            return render(request,'home.html')
        else:
            messages.info(request,"Your Password Must Be 8 Characters Long At Least.")
            return render(request,'home.html')
            """