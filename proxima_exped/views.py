from django.shortcuts import render, get_object_or_404
from .models import Expedition


def detail(request, expedition_id):
    expedition = get_object_or_404(Expedition, pk=expedition_id)
    inclusives = expedition.inclusives.split(",")
    popular = Expedition.objects.all();
    return render(request, 'expeditions/detail.html', {'expedition': expedition, 'popular': popular, 'inclusives': inclusives})
