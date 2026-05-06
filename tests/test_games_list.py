import requests

BASE_URL = "https://www.freetogame.com/api"

class TestGamesList:
    """
    Tests para el endpoint /games
    Verifica que la API retorna una lista válida de videojuegos.
    """

    def test_status_code_es_200(self):
        """La API debe responder con HTTP 200 OK"""
        response = requests.get(f"{BASE_URL}/games")
        assert response.status_code == 200, \
            f"Se esperaba 200 pero llegó {response.status_code}"

    def test_respuesta_es_una_lista(self):
        """La respuesta debe ser una lista de juegos"""
        response = requests.get(f"{BASE_URL}/games")
        data = response.json()
        assert isinstance(data, list), \
            "Se esperaba una lista pero llegó otro tipo de dato"

    def test_lista_no_esta_vacia(self):
        """La lista no debe estar vacía"""
        response = requests.get(f"{BASE_URL}/games")
        data = response.json()
        assert len(data) > 0, \
            "La lista de juegos está vacía"

    def test_juego_tiene_campos_requeridos(self):
        """Cada juego debe tener los campos esenciales"""
        response = requests.get(f"{BASE_URL}/games")
        data = response.json()
        primer_juego = data[0]

        campos_requeridos = ["id", "title", "genre", "platform", "thumbnail"]

        for campo in campos_requeridos:
            assert campo in primer_juego, \
                f"El campo '{campo}' no existe en el juego"

    def test_filtrar_por_genero_mmorpg(self):
        """Debe poder filtrar juegos por género"""
        response = requests.get(f"{BASE_URL}/games", params={"category": "mmorpg"})
        data = response.json()
        assert isinstance(data, list) and len(data) > 0, \
            "El filtro por género no retornó resultados"