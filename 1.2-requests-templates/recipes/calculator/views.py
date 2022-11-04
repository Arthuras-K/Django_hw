from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def index(request):
    context = {
        'DATA': DATA,
    }
    return render(request, 'calculator/index.html', context)

def omlet(request):
    serv_number = int(request.GET.get('servings', 1))    
    dish = {}
    for item in DATA['omlet']:
        dish[item] = DATA['omlet'][item] * serv_number
    context = {
        'dish': dish,
        'serv_number': serv_number,
    }
    return render( request, 'calculator/omlet.html', context)

def pasta(request):
    serv_number = int(request.GET.get('servings', 1))    
    dish = {}
    for item in DATA['pasta']:
        dish[item] = DATA['pasta'][item] * serv_number
    context = {
        'dish': dish,
        'serv_number': serv_number,
    }
    return render( request, 'calculator/pasta.html', context)

def buter(request):
    serv_number = int(request.GET.get('servings', 1))    
    dish = {}
    for item in DATA['buter']:
        dish[item] = DATA['buter'][item] * serv_number
    context = {
        'dish': dish,
        'serv_number': serv_number,
    }
    return render( request, 'calculator/buter.html', context)


