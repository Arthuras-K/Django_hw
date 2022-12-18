import pytest

from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Student, Course



@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get(f'/api/v1/courses/{course[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == course[0].name


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    course = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?id={course[7].id}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == course[7].name


@pytest.mark.django_db
def test_filter_name(client, course_factory):
    course = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?name={course[7].name}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == course[7].name


@pytest.mark.django_db
def test_post_course(client):
    course = {
        'name': 'test_name',
    }

    response_post = client.post('/api/v1/courses/', data=course)
    
    response_get = client.get(f'/api/v1/courses/?name={course["name"]}')
    response = response_get.json()

    assert response_post.status_code == 201
    assert response[0]['name'] == course['name']
    

@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)
    course_update = {
        'name': 'test_name',
    }

    response_update = client.patch(f'/api/v1/courses/{course[0].id}/', data=course_update)
    
    response_get = client.get(f'/api/v1/courses/{course[0].id}/')
    response = response_get.json()

    assert response_update.status_code == 200
    assert response_get.status_code == 200   
    assert response['name'] == course_update['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)

    response_delete = client.delete(f'/api/v1/courses/{course[0].id}/')
    response_get = client.get(f'/api/v1/courses/{course[0].id}/')

    assert response_delete.status_code == 204
    assert response_get.status_code == 404