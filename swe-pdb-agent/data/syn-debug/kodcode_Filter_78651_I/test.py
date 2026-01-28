from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from flask import Flask
from solution import app

# A helper to create a test client
@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    rv = client.get('/')
    assert b'You are not logged in' in rv.data

def test_login_logout(client):
    rv = client.post('/login', data=dict(
        username='admin', password='adminpass'
    ))
    assert rv.status_code == 302  # Redirect to home
    rv = client.get('/')
    assert b'Logged in as admin with role admin' in rv.data

    rv = client.get('/logout')
    assert rv.status_code == 302  # Redirect to home
    rv = client.get('/')
    assert b'You are not logged in' in rv.data

def test_invalid_login(client):
    rv = client.post('/login', data=dict(
        username='admin', password='wrongpass'
    ))
    assert b'Invalid credentials' in rv.data

def test_session_priority(client):
    with client:
        client.post('/login', data=dict(
            username='member', password='memberpass'
        ))
        rv = client.get('/')
        assert b'Logged in as member with role member' in rv.data
        assert 'priority' in session
        assert session['priority'] == 2