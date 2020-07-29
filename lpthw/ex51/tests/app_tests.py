from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects = True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'FILL OUT THIS FORM', rv.data)

    data = {'name': 'COCONUT', 'greet': 'TUALE'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_equal(rv.status_code, 200)
    assert_in(b'COCONUT', rv.data)
    assert_in(b'TUALE', rv.data)

def test_hello2():
    rv = web.get('/hello2', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"SHAKABULA", rv.data)
