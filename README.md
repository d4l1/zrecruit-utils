# zrecruit-utils

zrecruit-utils es una colección de scripts en Python diseñados para facilitar la interacción con Zoho Recruit mediante su API. El objetivo principal es automatizar tareas comunes como el mapeo de campos, extracción de estructuras de módulos, validaciones y futuras integraciones con otros sistemas de talento humano.

## 📌 Scripts incluidos

| Script              | Descripción |
|---------------------|-------------|
| `get_fields.py`     | Obtiene todos los campos del módulo **Job Openings**, incluyendo etiqueta visible, nombre interno (API) y tipo de dato. Exporta los resultados a un archivo `.xlsx`. |

## ▶️ Requisitos

- Python 3.8+
- Pandas
- Requests

Instalar dependencias:

```bash
pip install -r requirements.txt
