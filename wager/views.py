from django.shortcuts import render
from .models import Wager
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
import requests

# Create your views here.
def detail(request,pk):
    wager = get_object_or_404(Wager, pk=pk)
    event = wager.event
    


    req = requests.get(f"https://api.the-odds-api.com/v4/sports/soccer_epl/events/{event}/odds?apiKey=065f129f65ef12e03137bc35b65e27be&regions=us&markets=h2h&oddsFormat=decimal")

    res = req.json()

    bookmakers = res['bookmakers']


    

    return render(request,'wager/detail.html',{'wager':wager,'bookmakers':bookmakers})

def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('wager:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'wager/form.html', {
        'form': form,
        'title': 'New Wager',
    })

def edit(request, pk):
    wager = get_object_or_404(Wager, pk=pk)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=wager)

        if form.is_valid():
            form.save()

            return redirect('wager:detail', pk=wager.id)
    else:
        form = EditItemForm(instance=wager)

    return render(request, 'wager/form.html', {
        'form': form,
        'title': 'Edit Wager',
    })

def delete(request, pk):
    wager = get_object_or_404(Wager, pk=pk)
    wager.delete()

    wagers = Wager.objects.all()
    return redirect('wager:new')
   

    