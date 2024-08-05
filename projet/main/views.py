from django.shortcuts import render, get_object_or_404, redirect
from .models import Ouvrage
from .forms import OuvrageForm


def liste_ouvrages(request):
    ouvrages = Ouvrage.objects.all()
    return render(request, 'gestion_ouvrages/liste_ouvrages.html', {'ouvrages': ouvrages})


def creer_ouvrage(request):
    if request.method == "POST":
        form = OuvrageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ouvrages')
    else:
        form = OuvrageForm()
    return render(request, 'gestion_ouvrages/creer_ouvrage.html', {'form': form})


def modifier_ouvrage(request, pk):
    ouvrage = get_object_or_404(Ouvrage, pk=pk)
    if request.method == "POST":
        form = OuvrageForm(request.POST, instance=ouvrage)
        if form.is_valid():
            form.save()
            return redirect('liste_ouvrages')
    else:
        form = OuvrageForm(instance=ouvrage)
    return render(request, 'gestion_ouvrages/modifier_ouvrage.html', {'form': form})


def supprimer_ouvrage(request, pk):
    ouvrage = get_object_or_404(Ouvrage, pk=pk)
    ouvrage.delete()
    return redirect('liste_ouvrages')
