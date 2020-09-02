from applications.home.models import Home

# este archivo se agrega al base.py en la parte de TEMPLATES

""" proceso para recuperar telefono y email del registro home"""

# de esta forma se escribe una funcion que va a hacer un proceso y pasarle el metodo request
def home_contact(request):
    home= Home.objects.latest('created')
    # siempre se tiene que retornar como un diccionario
    return {
        'phone': home.phone_number,
        'other_email':home.contact_email
    }


