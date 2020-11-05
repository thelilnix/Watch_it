from Watch_it.db_config import (
    PANEL_USERNAME,
    PANEL_PASSWORD,
)


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    text = b'This website saves your platform, browser name, IP and country.'
    assert text in response.data


def test_admin_login_without_session(client, wrong_user_pass):
    # Wrong username and password
    response = client.post('/login', data=wrong_user_pass)
    assert response.status_code == 403

    # Correct username and password
    post_data = {
        "username": PANEL_USERNAME,
        "password": PANEL_PASSWORD,
    }

    response = client.post('/login', data=post_data, follow_redirects=True)
    assert b'Dashboard' in response.data


def test_admin_login_with_session(client):
    # Correct session
    with client.session_transaction() as session:
        session["username"] = PANEL_USERNAME
    response = client.get("/login", follow_redirects=True)
    assert b'Dashboard' in response.data

    # Wrong session
    with client.session_transaction() as session:
        session["username"] = "pytest"
    response = client.get("/login")
    assert response.status_code == 200
    assert b'Login' in response.data


def test_dashboard_without_session(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert b'Login' in response.data


def test_dashboard_with_session(client):
    # Correct session
    with client.session_transaction() as session:
        session["username"] = PANEL_USERNAME
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert PANEL_USERNAME.encode('utf8') in response.data

    # Wrong session
    with client.session_transaction() as session:
        session["username"] = "pytest"
    response = client.get('/dashboard', follow_redirects=True)
    assert b'Login' in response.data


def test_logout(client):
    # Testing without session
    response = client.get('/logout', follow_redirects=True)
    assert b'Login' in response.data

    # Testing with session
    with client.session_transaction() as session:
        session["username"] = PANEL_USERNAME
    assert b'Login' in response.data


def test_error_404(client):
    response = client.get('/nothing_is_here_just_test_404')
    assert response.status_code == 404


def test_error_403(client, wrong_user_pass):
    response = client.post('/login', data=wrong_user_pass)
    assert response.status_code == 403


def test_error_429(client, wrong_user_pass):
    for i in range(15):  # 15 times
        client.post('/login', data=wrong_user_pass)

    response = client.post('/login', data=wrong_user_pass)
    assert response.status_code == 429
