from django.shortcuts import render

def vote1(request):
    
    # title, num, multi
    items = [
            ['Best Speaker', range(6), False],
            ['Best Table Topic', range(8), False],
            ['Best Role Taker', range(8), False],
    ]
    
    print request
    
    return render(request, 'polls/vote.html', {'items' : items})




