from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Tasks

def home(request):
    listaTasks = Tasks.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'listaTasks': listaTasks,
    }
    return HttpResponse(template.render(context,request))

def adicionar(request):
    template = loader.get_template('adicionar.html')
    return HttpResponse(template.render({},request))

def addtarefa(request):
    tarefa = request.POST["tarefa"]
    descricao = request.POST["descricao"]
    prioridade = request.POST["prioridade"]
    data = request.POST["data"]
    status = request.POST["status"]
    task = Tasks(tarefa=tarefa,descricao=descricao,prioridade=prioridade,data=data,status=status)
    task.save()
    return HttpResponseRedirect(reverse('home'))

def apagar(request, id):
  task = Tasks.objects.get(id=id)
  task.delete()
  return HttpResponseRedirect(reverse('home'))

def editar(request, id):
  task = Tasks.objects.get(id=id)
  template = loader.get_template('editar.html')
  context = {
    'task': task,
  }
  return HttpResponse(template.render(context, request))

def editartarefa(request, id):
  tarefa = request.POST["tarefa"]
  descricao = request.POST["descricao"]
  prioridade = request.POST["prioridade"]
  sobrenome = request.POST['sobrenome']
  data = request.POST["data"]
  status = request.POST["status"]
  task = Tasks.objects.get(id=id)
  task.tarefa = tarefa
  task.descricao = descricao
  task.prioridade = prioridade
  task.data = data
  task.status = status
  task.save()
  return HttpResponseRedirect(reverse('home'))
# Create your views here.
