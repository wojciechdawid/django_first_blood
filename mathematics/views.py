from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from mathematics.services.algebra import AlgebraService


# Create your views here.

def hello(request, name="world"):
    return render(
        request=request,
        template_name="mathematics/calculations.html",
        context={
            "text": f"Hello {name}",
            "text2": "Pies je kota"
        }
    )


def calculate(request, calc: str, a: int = 0, b: int = 0) -> HttpResponse:
    try:
        result = AlgebraService.calculate(calc, a, b)
    except ValueError as e:
        return HttpResponse(f"{e}")
    except ZeroDivisionError as e:
        return HttpResponse(f"{e}")
    except KeyError:
        return HttpResponse("Niepoprawna operacja")
    return HttpResponse(result)
