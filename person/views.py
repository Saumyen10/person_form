from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from person.models import Consumer, Zone, Division, SubDivision


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Consumer, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_division(request):
    zone_id = request.GET.get('zone_id')
    divisions = Division.objects.filter(zone_id=zone_id).all()
    return render(request, 'city_dropdown_list_options.html', {'divisions': divisions})

def load_subdivision(request):
    division_id = request.GET.get('division_id')
    subdivisions = SubDivision.objects.filter(division_id=division_id).all()
    return render(request, 'subdivision_dropdown_list_options.html', {'subdivisions': subdivisions})
    # return JsonResponse(list(divisions.values('id', 'name')), safe=False)

    