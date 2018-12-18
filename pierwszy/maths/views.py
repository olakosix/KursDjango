from django.shortcuts import render

# Create your views here.
def operacje( operacja, arg1, arg2):
    if operacja == "add":
        wynik = arg1 + arg2
    elif operacja == "sub":
        wynik = arg1 - arg2
    elif operacja == "mul":
        wynik == arg1 * arg2
    elif operacja == "div":
        if arg2 == 0:
            wynik "Cholero nie dziel przez zero"
        else :
            wynik == arg1/arg2
    return wynik

def operacje (request, operacja, arg1, arg2):
    wynik = obliczenia(operacja, arg1, arg2)

    return HttpResponse(wynik)