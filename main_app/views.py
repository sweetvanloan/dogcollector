from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic  import DetailView, ListView
from .models import Dog, Toy



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', { 'dog': dog })

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/dogs/'

class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

# class ToyCreate(LoginRequiredMixin, CreateView):
#     model = Toy
#     fields = '__all__'

# class ToyDetail(LoginRequiredMixin, DetailView):
#     model = Toy

# class ToyList(LoginRequiredMixin, ListView):
#     model = Toy

# class ToyUpdate(LoginRequiredMixin, UpdateView):
#     model = Toy
#     fields = '__all__'

# class ToyDelete(LoginRequiredMixin, DeleteView):
#     model = Toy
#     success_url = '/toys/'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyDetail(DetailView):
    model = Toy

class ToyList(ListView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'