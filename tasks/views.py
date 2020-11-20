from django.shortcuts import render

from .models import Task
from .serializer import TaskSerializer

from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


#def createTask(request):
#    if request.method == 'POST':
#        form = StudentForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('/data')
#    else:
#        form =StudentForm()
#        context = {
#            'form':form
#        }
#        return render(request,'create.html',context)


def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many =True)
        return JsonResponse(serializer.data, safe =False)
