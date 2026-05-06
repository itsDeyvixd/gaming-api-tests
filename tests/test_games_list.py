import requests

BASE_URL = "https://www.freetogame.com/api"


class TestGamesList:

    def test_status_code_es_200(self):
        response = requests.get(f"{BASE_URL}/games")
        assert response.status_code == 200, f"Se esperaba 200 pero llego {response.status_code}"

    def test_respuesta_es_una_lista(self):
        response = requests.get(f"{BASE_URL}/games")
        data = response.json()
        assert isinstance(data, list), "Se esperaba una lista pero llego otro tipo de dato"

    def test_lista_no_esta_vacia(self):
        response = requests.get(f"{BASE_URL}/games")
        data = response.json()
        assert len(data) > 0, "La lista de juegos esta vacia"

    def test_juego_tiene_campos_requeridos(self):
        response = requests.get(f"{BASE_URL}/games")
        data = response.json()
        primer_juego = data[0]
        campos_requeridos = ["id", "title", "genre", "platform", "thumbnail"]
        for campo in campos_requeridos:
            assert campo in primer_juego, f"El campo {campo} no existe en el juego"

    def test_filtrar_por_genero_mmorpg(self):
        response = requests.get(f"{BASE_URL}/games", params={"category": "mmorpg"})
        data = response.json()
        assert isinstance(data, list) and len(data) > 0, "El filtro por genero no retorno resultados"
