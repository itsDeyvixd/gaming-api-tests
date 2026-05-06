import pytest
import requests

BASE_URL = "https://www.freetogame.com/api"

@pytest.fixture
def api():
    """
    Fixture base: retorna una sesión HTTP reutilizable
    con la URL base de la API de videojuegos.
    """
    session = requests.Session()
    session.base_url = BASE_URL
    return session