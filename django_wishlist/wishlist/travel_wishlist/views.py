from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    # if statement if a post is done on the page to save and update
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')

    # prints out the names of places that visited equal false
    places = Place.objects.filter(visited=False).order_by('name')
    # used the forms.py to create new items for the list
    new_place_form = NewPlaceForm()
    # this sends the information to the database
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

# this is the route to visited places
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

# this is if a item isn't in the db
def place_is_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')
