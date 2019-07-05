from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Details
from .forms import NewDetailForm

def landing(request):
    return render(request, 'landing.html')

def add_detail(request):
    if request.method == 'POST':
        form = NewDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.created_at = timezone.now()
            detail.save()
            
            return redirect('list_details')
    else:
        form = NewDetailForm()

    return render(request, 'add_detail.html', {'form': form})

def list_details(request):
    details = Details.objects.all()
    return render(request, 'list_details.html', {'details': details})