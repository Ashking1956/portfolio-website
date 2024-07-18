from django.shortcuts import render
# Create your views here.


def MainScreen(request):
    return render(request, 'index.html')


def TuneMoodScreen(request):
    return render(request, 'TuneMood.html')


def CareerExplorerScreen(request):
    return render(request, 'CareerExplorer.html')


def ExplorerInnsScreen(request):
    return render(request, 'ExplorerInns.html')


def EsevaScreen(request):
    return render(request, 'E-Seva.html')
