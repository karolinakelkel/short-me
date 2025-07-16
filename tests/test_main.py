from fastapi.testclient import TestClient

from app.main import app

VALID_TEST_URL = 'https://github.com/karolinakelkel/'
INVALID_SHORT_CODE = 'miaow'  # P(generating exactly this short code) ≈ 9.31e-10

client = TestClient(app)


def test_create_short_url():
    response_1 = client.post('/shorten', json={'url': VALID_TEST_URL})
    data_1 = response_1.json()

    assert response_1.status_code == 200
    assert 'short_url' in data_1
    assert data_1['short_url'].startswith('http://localhost:8000/')


def test_redirect_to_url():
    response = client.post('/shorten', json={'url': VALID_TEST_URL})
    short_url = response.json()['short_url']
    short_code = short_url.split('/')[-1]
    response = client.get(f'/{short_code}', follow_redirects=False)

    assert response.status_code == 307
    assert response.headers['location'] == VALID_TEST_URL


def test_reuse_existing_short_code():
    response_1 = client.post('/shorten', json={'url': VALID_TEST_URL})
    response_2 = client.post('/shorten', json={'url': VALID_TEST_URL})
    data_1 = response_1.json()
    data_2 = response_2.json()

    assert data_1 == data_2


def test_nonexistent_code_returns_404():
    response = client.get(INVALID_SHORT_CODE)
    assert response.status_code == 404
