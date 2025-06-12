import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Domicilio, Morador

def run():
    Domicilio.objects.all().delete()
    Morador.objects.all().delete()
    print("Todos os dados apagados.")

if __name__ == "__main__":
    run()