from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'chandu'}
    return render(request,'loop.html',context=d)