import pytest
from django.test import Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed


def test_home_index_url():
    """Test of home:index """

    # GIVEN - path to home:index
    uri = 'home:index'
    path = reverse(uri)

    # WHEN - resolving path
    result = resolve(path)

    # WHAT - check for valid path and view_name
    assert path == '/'
    assert result.view_name == uri


@pytest.mark.django_db
def test_home_index_view():
    """ Test of letting.views.index """

    # GIVEN - path to home:index
    uri = 'home:index'
    path = reverse(uri)

    # WHEN - making get request to path
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    # WHAT - look for valid title and valid response status
    assert '<h1>Welcome to Holiday Homes</h1>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "web_site/index.html")
