# from django.shortcuts import render
from django.http import HttpResponse
from .toy_logic import toysdata, totalbenefit, mostSold, bestProduct, worstProduct


def display_toy_data(request):
    
    toysdata()
    
    response( 
        f"General Benefit: {totalbenefit(toys)}<br>"
        f"Most Sold Product: {mostSold(toys)}<br>"
        f"Best Product: {bestProduct(toys)}<br>"
        f"Worst Product: {worstProduct(toys)}<br>"
            )
    
    return HttpResponse(response)
    
    # return render(request, 'toy_logic.html')