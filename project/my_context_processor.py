__author__ = 'sendr'

from roof.models import Address, Phone, Email

def put_data(request):
    addresses = Address.objects.all()
    phones = Phone.objects.all()
    emails = Email.objects.all()
    our_data = {'addresses': addresses, 'emails': emails, 'phones': phones}
    return {'our_data': our_data}
