from django.shortcuts import render
from .forms import TestForm
from .models import Tasks


def test(request):
    val = ''
    data = Tasks.objects.order_by('name')
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            val = 'OK'
    else:
        form = TestForm()
    return render(request, 'test.html', {'val': val, 'data': data})
