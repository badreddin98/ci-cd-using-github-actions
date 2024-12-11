import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_positive_numbers(client):
    response = client.post('/add',
                         data=json.dumps({'numbers': [1, 2, 3]}),
                         content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data)['result'] == 6

def test_add_negative_numbers(client):
    response = client.post('/add',
                         data=json.dumps({'numbers': [-1, -2, -3]}),
                         content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data)['result'] == -6

def test_invalid_input(client):
    response = client.post('/add',
                         data=json.dumps({'wrong_key': [1, 2, 3]}),
                         content_type='application/json')
    assert response.status_code == 400

def test_non_numeric_input(client):
    response = client.post('/add',
                         data=json.dumps({'numbers': [1, "2", 3]}),
                         content_type='application/json')
    assert response.status_code == 400
