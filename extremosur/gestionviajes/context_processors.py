from .forms import BuscarPaqueteForm

def search_form(request):
    return {'buscar_form': BuscarPaqueteForm()}