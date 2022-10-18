import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from oc_lettings_site.profiles.models import Profile


@pytest.mark.django_db
def test_index_view():
    """ Test of profiles.views.index """

    # GIVEN - path to profiles:index
    uri = 'profiles:index'
    path = reverse(uri)

    # WHEN - making get request to path
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    # WHAT - look for valid title and valid response status
    assert '<h1>Profiles</h1>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view():
    """ Test of profiles.views.profile """

    # GIVEN - path to profiles:profile and a username
    uri = 'profiles:profile'
    user_test = User.objects.create(username='user_test', password='user_test_password')
    profile_test = Profile.objects.create(user=user_test, favorite_city='city_test')
    path = reverse(uri, kwargs={'username': user_test.username})

    # WHEN - making get request to path
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    # WHAT - look for valid title and valid response status
    assert f'<h1>{profile_test.user.username}</h1>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
