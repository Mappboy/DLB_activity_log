from django.db import models
class Person():
    pass

class Linker(Person):
    pass

class Client(Person):
    pass

class Organisation():
    members = models.ManytoOneField(Client)
    pass


