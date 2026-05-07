
import pytest
import requests

BASE_URL = "https://www.freetogame.com/api"
JUEGO_ID_VALIDO = 452      # Valorant — sabemos que existe
JUEGO_ID_INVALIDO = 99999  # ID que no existe en la API


class TestGameDetail:
    """
    Tests para el endpoint /game?id=
    Verifica que el detalle de un juego específico sea válido y completo.
    """

    def test_detalle_status_200(self):
        """El endpoint de detalle debe responder con HTTP 200"""
        response = requests.get(f"{BASE_URL}/game", params={"id": JUEGO_ID_VALIDO})
        assert response.status_code == 200, \
            f"Se esperaba 200 pero llegó {response.status_code}"

    def test_detalle_campos_completos(self):
        """El juego debe tener todos los campos de detalle"""
        response = requests.get(f"{BASE_URL}/game", params={"id": JUEGO_ID_VALIDO})
        data = response.json()

        campos_requeridos = [
            "id",
            "title",
            "thumbnail",
            "description",
            "game_url",
            "genre",
            "platform",
            "publisher",
            "developer",
            "release_date",
        ]

        for campo in campos_requeridos:
            assert campo in data, \
                f"❌ El campo '{campo}' no existe en la respuesta"

    def test_descripcion_no_esta_vacia(self):
        """La descripción del juego no puede estar vacía"""
        response = requests.get(f"{BASE_URL}/game", params={"id": JUEGO_ID_VALIDO})
        data = response.json()

        assert "description" in data, "❌ No existe el campo description"
        assert len(data["description"]) > 0, \
            "❌ La descripción está vacía"

    def test_thumbnail_es_url_valida(self):
        """La URL del thumbnail debe ser una URL real que comience con http"""
        response = requests.get(f"{BASE_URL}/game", params={"id": JUEGO_ID_VALIDO})
        data = response.json()

        thumbnail = data.get("thumbnail", "")
        assert thumbnail.startswith("http"), \
            f"❌ El thumbnail no es una URL válida: {thumbnail}"

    def test_año_lanzamiento_valido(self):
        """El año de lanzamiento debe ser posterior a 1990"""
        response = requests.get(f"{BASE_URL}/game", params={"id": JUEGO_ID_VALIDO})
        data = response.json()

        release_date = data.get("release_date", "")
        año = int(release_date[:4])  # Los primeros 4 caracteres son el año

        assert año >= 1990, \
            f"❌ Año de lanzamiento inválido: {año}"

    def test_id_inexistente_retorna_error(self):
        """Un ID que no existe debe retornar status 404 o un mensaje de error"""
        response = requests.get(f"{BASE_URL}/game", params={"id": JUEGO_ID_INVALIDO})
        data = response.json()

        # La API retorna status 200 pero con un mensaje de error en el body
        assert "status" in data, \
            "❌ La API no maneja correctamente los IDs inexistentes"

    # 🔴 TEST QUE FALLA A PROPÓSITO — simula un bug detectado
    @pytest.mark.xfail(reason="BUG SIMULADO: título no coincide exactamente")
    def test_titulo_es_exactamente_valorant(self):
        """
        [BUG SIMULADO] Verificamos que el título sea exactamente 'Call of Duty'
        cuando en realidad es 'Valorant'.
        Esto demuestra cómo se ve un bug detectado en el reporte.
        """
        response = requests.get(f"{BASE_URL}/game", params={"id": JUEGO_ID_VALIDO})
        data = response.json()

        assert data["title"] == "Call of Duty", \
            f"❌ BUG DETECTADO: Se esperaba 'Call of Duty' pero el título es '{data['title']}'"