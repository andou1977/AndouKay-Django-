
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from Andou_Kay.models import Proprietaire

# code Api la
from Andou_Kay.serializers import Ouestserializer


#lister ouest by id essais en attendant

def listouestforid(request):
    polls = Proprietaire.objects.filter(Departement='ouest')
    data = {"results": list(polls.values("Nom", "Prenom", "Telephone", "Nombre_De_Piece", "Adresse", "Cout", "Image", "Description", "Duree", "Departement", "Date_du_jour", "Sexe", "type", "Monnaie", "Nif"))}
    return JsonResponse(data)

def litbyidouest(request, pk):
    idouest = get_object_or_404(Proprietaire, pk=pk)
    data = {"results": {"Nom": idouest.Nom, "Prenom": idouest.Prenom, "Telephone": idouest.Telephone, "Nombre de Piece": idouest.Nombre_De_Piece, "Adresse": idouest.Adresse, "Cout": idouest.Cout, "Image": idouest.Image, "Description": idouest.Description, "Duree": idouest.Duree, "Departement": idouest.Departement, "Date": idouest.Date_du_jour, "Sexe": idouest.Sexe, "Type": idouest.type, "Monnaie": idouest.Monnaie, "Nif": idouest.Nif}}
    return JsonResponse(data)




class OuestView(viewsets.ModelViewSet):
    queryset = Proprietaire.objects.filter(Departement='ouest')
    serializer_class = Ouestserializer



# code projet a
def index(request):
    return render(request, 'index.html')


def pageerror(request):
    return render(request, 'pageerror.html')


def idouest(request, id):
    id = Proprietaire.objects.filter(id=id)
    return render(request, 'view.html', {'id': id})


def ouest(request):
    list = Proprietaire.objects.filter(Departement='ouest')

    if list.exists():
        return render(request, 'ouest.html', {'list': list})
    else:
        messages.error(request, 'pas de maison disponible pour le departement Ouest')
        return render(request, 'pageerror.html')


def searchquest(request):
    search = request.POST['search']
    list = Proprietaire.objects.filter(Q(Adresse__icontains=search, Departement='ouest') |
                                       Q(Cout__istartswith=search, Departement='ouest'))
    # list1 = Proprietaire.objects.filter(Departement='ouest')

    if search == '':
        list = Proprietaire.objects.filter(Departement='ouest')
        messages.error(request, 'le champ ne doit pas etre  vide')
        return render(request, 'ouest.html', {'list': list})

    elif list.exists():
        return render(request, 'ouest.html', {'list': list})
    else:
        list = Proprietaire.objects.filter(Departement='ouest')
        messages.error(request, 'Pas de maison pour cette recherche')
        return render(request, 'ouest.html', {'list': list})


def view(request):
    return render(request, 'view.html', {'id': id})


def sud(request):
    list = Proprietaire.objects.filter(Departement='sud')

    if list.exists():
        return render(request, 'sud.html', {'list': list})
    else:
        messages.error(request, 'pas de maison disponible pour le departement Sud')
        return render(request, 'pageerror.html')


def searchsud(request):
    search = request.POST['search']
    list = Proprietaire.objects.filter(Q(Adresse__icontains=search, Departement='sud') |
                                       Q(Cout__istartswith=search, Departement='sud'))

    if search == '':
        list = Proprietaire.objects.filter(Departement='sud')
        messages.error(request, 'le champ ne doit pas etre  vide')
        return render(request, 'sud.html', {'list': list})

    elif list.exists():
        return render(request, 'sud.html', {'list': list})
    else:
        list = Proprietaire.objects.filter(Departement='sud')
        messages.error(request, 'Pas de maison pour cette recherche')
        return render(request, 'sud.html', {'list': list})


def nord(request):
    list = Proprietaire.objects.filter(Departement='nord')

    if list.exists():
        return render(request, 'nord.html', {'list': list})
    else:
        messages.error(request, 'pas de maison disponible pour le departement Nord')
        return render(request, 'pageerror.html')


def searchnord(request):
    search = request.POST['search']
    list = Proprietaire.objects.filter(Q(Adresse__icontains=search, Departement='nord') |
                                       Q(Cout__istartswith=search, Departement='nord'))

    if search == '':
        list = Proprietaire.objects.filter(Departement='nord')
        messages.error(request, 'le champ ne doit pas etre  vide')
        return render(request, 'nord.html', {'list': list})

    elif list.exists():
        return render(request, 'nord.html', {'list': list})
    else:
        list = Proprietaire.objects.filter(Departement='nord')
        messages.error(request, 'Pas de maison pour cette recherche')
        return render(request, 'nord.html', {'list': list})


def nippes(request):
    list = Proprietaire.objects.filter(Departement='nippes')

    if list.exists():
        return render(request, 'nippes.html', {'list': list})
    else:
        messages.error(request, 'pas de maison disponible pour le departement Nippes')
        return render(request, 'pageerror.html')


def searcnippes(request):
    search = request.POST['search']
    list = Proprietaire.objects.filter(Q(Adresse__icontains=search, Departement='nippes') |
                                       Q(Cout__istartswith=search, Departement='nippes'))

    if search == '':
        list = Proprietaire.objects.filter(Departement='nippes')
        messages.error(request, 'le champ ne doit pas etre  vide')
        return render(request, 'nippes.html', {'list': list})

    elif list.exists():
        return render(request, 'nippes.html', {'list': list})
    else:
        list = Proprietaire.objects.filter(Departement='nippes')
        messages.error(request, 'Pas de maison pour cette recherche')
        return render(request, 'nippes.html', {'list': list})
