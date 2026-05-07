import pytest
import requests

BASE_URL = "https://www.freetogame.com/api"

GENEROS = [
    "mmorpg",
    "shooter",
    "strategy",
    "moba",
    "racing",
    "sports",
    "social",
    "sandbox",
    "survival",
]

PLATAFORMAS = [
    "pc",
    "browser",
]


class TestFilters:
    """
    Tests para los filtros de la API.
    Verifica que cada género y plataforma retorne resultados válidos.
    """

    @pytest.mark.parametrize("genero", GENEROS)
    def test_filtro_por_genero(self, genero):
        """Cada género debe retornar una lista no vacía de juegos"""
        response = requests.get(
            f"{BASE_URL}/games",
            params={"category": genero}
        )
        assert response.status_code == 200, \
            f"❌ Género '{genero}' retornó status {response.status_code}"

        data = response.json()
        assert isinstance(data, list), \
            f"❌ Género '{genero}' no retornó una lista"
        assert len(data) > 0, \
            f"❌ Género '{genero}' retornó lista vacía"

    @pytest.mark.parametrize("plataforma", PLATAFORMAS)
    def test_filtro_por_plataforma(self, plataforma):
        """Cada plataforma debe retornar juegos válidos"""
        response = requests.get(
            f"{BASE_URL}/games",
            params={"platform": plataforma}
        )
        assert response.status_code == 200, \
            f"❌ Plataforma '{plataforma}' retornó status {response.status_code}"

        data = response.json()
        assert isinstance(data, list) and len(data) > 0, \
            f"❌ Plataforma '{plataforma}' no retornó resultados"

    def test_combinacion_genero_y_plataforma(self):
        """Debe poder filtrar por género Y plataforma al mismo tiempo"""
        response = requests.get(
            f"{BASE_URL}/games",
            params={"category": "shooter", "platform": "pc"}
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list) and len(data) > 0, \
            "❌ La combinación de filtros no retornó resultados"

    def test_genero_invalido_no_explota(self):
        """Un género que no existe no debe romper la API"""
        response = requests.get(
            f"{BASE_URL}/games",
            params={"category": "genero_inventado_xyz"}
        )
        assert response.status_code in [200, 404], \
            f"❌ La API explotó con un género inválido: {response.status_code}"