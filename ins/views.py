from django.shortcuts import render
from .models import User
from django.http import HttpResponse
# Create your views here.
def userreg(request):
    return render(request,'userreg.html')
    
def insertuser(request):
    varuid=request.POST['tuid']
    varuname=request.POST['tuname']
    varuemail=request.POST['tuemail']
    ok=User(uid=varuid,uname=varuname,uemail=varuemail)
    ok.save()
    return HttpResponse("<h1>Page is working</h1>")
def read(request):
    userdatadb=User.objects.all()
    return render(request,'viewusers.html',{'userdata':userdatadb})
def deletecrud(id):
    # User.objects.delete(id)
    us=User.objects.get(uid=id)
    us.delete()
    return HttpResponse("<h1>Delete Successfully</h1>")
def update(request,id):
    findbyid=User.objects.get(uid=id)
    return render(request,'updateuser.html',{'findbyid':findbyid})
def updatedatapost(request,id):
    
    usid=request.POST['tuid']
    usname=request.POST['tuname']
    usemail=request.POST['tuemail']
    us=User.objects.get(uid=id)
    us.uid=usid
    us.uname=usname
    us.uemail=usemail
    us.save()
    return HttpResponse("<h1>updated</h1>")