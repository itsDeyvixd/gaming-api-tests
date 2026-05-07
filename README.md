# 🎮 Gaming API Tests
![Gaming API Tests](https://github.com/itsDeyvixd/gaming-api-tests/actions/workflows/tests.yml/badge.svg)

Framework de automatización de pruebas para la API pública de [FreeToGame](https://www.freetogame.com/api-doc).

## 🛠️ Stack
- Python 3.14
- pytest
- requests
- pytest-html

## 📁 Estructura
```
gaming-api-tests/
├── tests/
│   ├── test_games_list.py
│   └── test_game_detail.py
├── conftest.py
├── requirements.txt
└── README.md
```
## 🚀 Cómo ejecutar

# Instalar dependencias
pip install -r requirements.txt

# Correr todos los tests
pytest tests/ -v

# Generar reporte HTML
pytest tests/ -v --html=reports/reporte.html --self-contained-html

## ✅ Tests — ¿Qué verifica cada uno?

### 📋 test_games_list.py — Catálogo general `/api/games`
| Test | Pregunta que responde | Por qué importa |
|---|---|---|
| `test_status_code_es_200` | ¿La API está viva y responde? | Si no es 200, el servidor está caído o roto |
| `test_respuesta_es_una_lista` | ¿Los datos tienen el formato correcto? | Podría responder 200 pero devolver basura |
| `test_lista_no_esta_vacia` | ¿Hay datos reales? | Una lista vacía rompe cualquier app que dependa de esto |
| `test_juego_tiene_campos_requeridos` | ¿Cada juego tiene lo mínimo necesario? | Si falta `thumbnail`, la app muestra imágenes rotas |
| `test_filtrar_por_genero_mmorpg` | ¿Los filtros funcionan? | Un filtro roto muestra resultados incorrectos al usuario |

### 🔍 test_game_detail.py — Detalle de juego `/api/game?id=`
| Test | Pregunta que responde | Por qué importa |
|---|---|---|
| `test_detalle_status_200` | ¿El endpoint de detalle responde? | Endpoint diferente, puede fallar independiente |
| `test_detalle_campos_completos` | ¿El juego tiene descripción, desarrollador, etc.? | La vista de detalle necesita más datos que el listado |
| `test_thumbnail_es_url_valida` | ¿La imagen tiene una URL real? | Una URL rota = imagen rota en producción |
| `test_id_inexistente_retorna_error` | ¿Qué pasa con datos inválidos? | La API debe manejar errores, no explotar |
| `test_año_lanzamiento_valido` | ¿El año tiene sentido? | Un juego no puede lanzarse en 1800 |

## 📸 Evidencia de ejecución

### Reporte HTML
<img width="1906" height="891" alt="Captura de pantalla 2026-05-07 172624" src="https://github.com/user-attachments/assets/681e5403-ee2a-4390-8159-5770589ffdbe" />

### Terminal — 24 passed, 1 xfailed
<img width="1565" height="633" alt="Captura de pantalla 2026-05-07 172537" src="https://github.com/user-attachments/assets/420006e0-cdc1-4396-936c-0baf63c2a253" />

### GitHub Actions — CI/CD
<img width="1878" height="837" alt="image" src="https://github.com/user-attachments/assets/0e932503-a946-4a76-902c-127c9fe360fc" />
