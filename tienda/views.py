from django.shortcuts import render
from tienda.models import Orden

def v_index(request):
    consulta = Orden.objects.all()
    context = {
        "ordenes": consulta
    }
    return render(request, "index.html", context)
