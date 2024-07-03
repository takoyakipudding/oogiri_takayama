from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Information, Answer, Topic
from .forms import AnswerForm
from django.urls import reverse, reverse_lazy
from django.views import View

def create_view(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user 
            answer.topic = Topic.objects.get(pk=1) 
            answer.save()
            return redirect('create')  
    else:
        form = AnswerForm()

    topic = Topic.objects.get(pk=1) 
    past_answers = Answer.objects.filter(topic=topic) 

    context = {
        'topic': topic,
        'past_answers': past_answers,
        'form': form,
    }
    return render(request, 'create.html', context)

def index_view(request):
    return render(request, 'agendapp/index.html')

class ListInformationView(ListView):
    template_name = 'agendapp/index.html'
    model = Information

class ListFlipView(ListView):
    template_name = 'agendapp/flip.html'
    model = Information
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        if q := query.get('cate'): #python3.8以降
            queryset = queryset.filter(category=q)

        return queryset

class PhotoView(View):
    def get(self, request):
        form = AnswerForm()
        return render(request, 'agendapp/create.html', {'form': form})

    def post(self, request):
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
        return render(request, 'agendapp/create.html', {'form': form})
    