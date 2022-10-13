import pytest
from django.urls import reverse, resolve

from oc_lettings_site.lettings.models import Address, Letting


def test_lettings_index_url():
    """Test of lettings:index """

    # GIVEN - path to lettings:index
    uri = 'lettings:index'
    path = reverse(uri)

    # WHEN - resolving path
    result = resolve(path)

    # WHAT - check for valid path and view_name
    assert path == '/lettings/'
    assert result.view_name == uri


@pytest.mark.django_db
def test_lettings_letting_url():
    """Test of lettings:letting """

    # GIVEN - path to lettings:letting and a new letting
    uri = 'lettings:letting'
    address_test = Address.objects.create(number=10,
                                          street='street_test',
                                          city='city_test',
                                          state='TT',
                                          zip_code='1010',
                                          country_iso_code='TTT')
    Letting.objects.create(title='title_test',
                           address=address_test)
    path = reverse(uri, kwargs={'letting_id': 1})

    # WHEN - resolving path
    result = resolve(path)

    # WHAT - check for valid path and view_name
    assert path == '/lettings/1/'
    assert result.view_name == uri
