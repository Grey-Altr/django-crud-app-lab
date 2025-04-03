from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def synth_index(request):
    return render(request, 'synths/synth-index.html')

def synth_detail(request, synth_id):
    return render(request, 'synths/detail.html')

def synth_create(request):
    return render(request, 'synths/create.html')

def synth_update(request, synth_id):
    return render(request, 'synths/detail.html')

def synth_delete(request, synth_id):
    return render(request, 'synths/delete.html')