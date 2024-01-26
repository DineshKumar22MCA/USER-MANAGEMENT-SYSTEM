from django.shortcuts import render,redirect
from django.http import HttpResponse
from flask import url_for



from app.models import user





def display(request):
    a = user.objects.all()
    return render(request,"display.html", {"a":a} )




# Create your views here.
def insert(request):
    msg=""
    if(request.method=="POST"):
        name = request.POST.get('name')
        role = request.POST.get('role')
        age = request.POST.get('age')
        user.objects.create(name=name,role=role,age=age)
        msg="inserted Successfully"
    
    return render(request, "insert.html",{'msg':msg})



def edit(request, id):
    try:
        instance = user.objects.get(id=id)

        if request.method == "POST":
            name = request.POST.get('name')
            role = request.POST.get('role')
            age = request.POST.get('age')

           
            instance.name = name
            instance.role = role
            instance.age =age
            instance.save()

            return redirect("display")

        return render(request, "edit.html", {'instance': instance})

    except user.DoesNotExist:
        return redirect("display")




def delete(request,id):
    msg = "recoed deleted"
    user.objects.filter(id=id).delete()
    return redirect("display")