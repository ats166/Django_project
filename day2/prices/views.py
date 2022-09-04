from django.shortcuts import render

# Create your views here.
items = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

def items(request,count):
    

    return render(request, 'prices/detail.html' ,count)

def main(request):

    return render(request, 'prices/main.html')