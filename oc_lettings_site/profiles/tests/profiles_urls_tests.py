import pytest
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from oc_lettings_site.profiles.models import Profile


def test_profiles_index_url():
    """Test of profiles:index """

    # GIVEN - path to profiles:index
    uri = 'profiles:index'
    path = reverse(uri)

    # WHEN - resolving path
    result = resolve(path)

    # WHAT - check for valid path and view_name
    assert path == '/profiles/'
    assert result.view_name == uri


@pytest.mark.django_db
def test_profiles_profile_url():
    """Test of profiles:profile """

    # GIVEN - path to profiles:profile and a username
    uri = 'profiles:profile'
    user_test = User.objects.create(username='user_test', password='user_test_password')
    Profile.objects.create(user=user_test,favorite_city='city_test')
    path = reverse(uri, kwargs={'username': user_test.username})

    # WHEN - resolving path
    result = resolve(path)

    # WHAT - check for valid path and view_name
    assert path == f'/profiles/{user_test.username}/'
    assert result.view_name == uri
