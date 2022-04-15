from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Students

# Create your views here.
def index(request):
    student = Students.objects.all().values()
    params = { 'student': student}
    return render(request,'index.html',params)
def add(request):
    if request.method == "POST":
        firstname = request.POST['first']
        lastname = request.POST['last']
        params = {'success':'Information Upload Successfully'}
        ins = Students(firstname = firstname , lastname = lastname)
        ins.save()
        return render(request,'add.html',params)

    return render(request,'add.html')

def delete(request,del_id):
    ins = Students.objects.get(id=del_id)
    ins.delete()
    index = redirect('/')
    return index

def update(request , upd_id):
    if request.method == "POST":
        firstname = request.POST['first']
        lastname = request.POST['last']
        success_msg = "Your Data Has been Updated Successfully!!"
        params = { "success":success_msg}
        ins = Students.objects.get(id=upd_id)
        ins.firstname = firstname
        ins.lastname = lastname
        ins.save()
        return render(request,'update.html',params)
    params2 = {'upd_id':upd_id}
    return render(request,'update.html',params2)