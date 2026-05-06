# 🎮 Gaming API Tests

Framework de automatización de pruebas para la API pública de [FreeToGame](https://www.freetogame.com/api-doc).

## 🛠️ Stack
- Python 3.14
- pytest
- requests
- pytest-html

## 📁 Estructura
gaming-api-tests/
├── tests/
│   └── test_games_list.py
├── conftest.py
├── requirements.txt
└── README.md
## 🚀 Cómo ejecutar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Correr los tests
pytest tests/ -v

# Generar reporte HTML
pytest tests/ -v --html=reports/reporte.html --self-contained-html
```

## ✅ Tests actuales

| Test | Descripción |
|---|---|
| `test_status_code_es_200` | La API responde con HTTP 200 |
| `test_respuesta_es_una_lista` | La respuesta es una lista válida |
| `test_lista_no_esta_vacia` | La lista contiene juegos |
| `test_juego_tiene_campos_requeridos` | Cada juego tiene id, title, genre, platform, thumbnail |
| `test_filtrar_por_genero_mmorpg` | El filtro por categoría funciona correctamente |