from django.http import HttpResponse
def say_hello (req) :
    return HttpResponse ('Hello World')