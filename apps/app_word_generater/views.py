
from django.shortcuts import render,HttpResponse
from django.utils.crypto import get_random_string
def index(request):

    contex = {
        "unique_id": get_random_string(length=14)
    }
    if 'number' not in request.session:
        request.session['number'] = 0
    else:
        request.session['number'] += 1
    
    return render(request,'app_word_generater/index.html', contex)


