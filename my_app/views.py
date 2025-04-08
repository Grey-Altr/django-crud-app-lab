from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Synth, SynthLog
from .forms import SynthLogForm


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('synth_list')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class SynthListView(LoginRequiredMixin, ListView):
    model = Synth
    template_name = 'synths/synth_list.html'
    
    def get_queryset(self):
        return Synth.objects.filter(user=self.request.user)

class SynthCreateView(LoginRequiredMixin, CreateView):
    model = Synth
    fields = '__all__'
    template_name = 'synths/synth_form.html'
    success_url = reverse_lazy('synth_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SynthUpdateView(LoginRequiredMixin, UpdateView):
    model = Synth
    fields = '__all__'
    template_name = 'synths/synth_form.html'
    success_url = reverse_lazy('synth_list')

class SynthDeleteView(LoginRequiredMixin, DeleteView):
    model = Synth
    template_name = 'synths/synth_confirm_delete.html'
    success_url = reverse_lazy('synth_list')
    
@login_required
def synth_detail(request, pk):
    synth = get_object_or_404(Synth, pk=pk)
    
    if request.method == 'POST':
        form = SynthLogForm(request.POST)
        if form.is_valid():
            new_log = form.save(commit=False)
            new_log.synth = synth
            new_log.user = request.user
            new_log.save()
            return redirect ('synth_detail', pk=synth.pk)
    else:
        form = SynthLogForm()
        
    return render(request, 'synths/synth_detail.html', {
        'object': synth,
        'log_form': form
    })
    
class SynthLogUpdateView(LoginRequiredMixin, UpdateView):
    model = SynthLog
    form_class = SynthLogForm
    template_name = 'synths/synthlog_form.html'
    
    def get_success_url(self):
        return reverse_lazy('synth_detail', kwargs={'pk': self.object.synth.pk})
    
class SynthLogDeleteView(LoginRequiredMixin, DeleteView):
    model = SynthLog
    template_name = 'synths/synthlog_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('synth_detail', kwargs={'pk': self.object.synth.pk})