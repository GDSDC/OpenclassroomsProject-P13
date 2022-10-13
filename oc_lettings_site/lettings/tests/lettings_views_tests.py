import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from oc_lettings_site.lettings.models import Address, Letting


@pytest.mark.django_db
def test_index_view():
    """ Test of letting.views.index """

    # GIVEN - path to lettings:index
    uri = 'lettings:index'
    path = reverse(uri)

    # WHEN - making get request to path
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    # WHAT - look for valid title and valid response status
    assert '<h1>Lettings</h1>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view():
    """ Test of letting.views.letting """

    # GIVEN - path to lettings:letting and a letting_id
    uri = 'lettings:letting'
    address_test = Address.objects.create(number=10,
                                          street='street_test',
                                          city='city_test',
                                          state='TT',
                                          zip_code='1010',
                                          country_iso_code='TTT')
    letting_test = Letting.objects.create(title='title_test',
                                          address=address_test)
    path = reverse(uri, kwargs={'letting_id': 1})

    # WHEN - making get request to path
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    # WHAT - look for valid title and valid response status
    assert f'<h1>{letting_test.title}</h1>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
