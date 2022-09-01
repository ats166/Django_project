from email import message
from django.shortcuts import render

# Create your views here.

def index(request):
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]

    context = {
        'fruit_list' : fruit_list,
        'hate' : hate,
    }

    return render(request, 'fruits/index.html', context)

def throw(request):

    return render(request, 'fruits/throw.html')

def catch(request):
    first = request.GET.get('first')
    second = request.GET.get('second')
    minus = int(first) - int(second)
    context = {
        'first' : first,
        'second' : second,
        'minus' : minus,
        # 'minus' : first-second,
    }

    return render(request, 'fruits/catch.html', context)