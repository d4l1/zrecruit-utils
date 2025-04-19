import requests
import pandas as pd

# 🌍 Usa el endpoint del data center correcto. Si estás en US, usa .com
ACCOUNTS_URL = 'https://accounts.zoho.com/oauth/v2/token'

# 🔐 Obtener access_token desde refresh_token
def get_access_token_from_refresh(client_id, client_secret, refresh_token):
    url = 'https://accounts.zoho.com/oauth/v2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    response = requests.post(url, headers=headers, data=data)

    print('🔍 Respuesta de Zoho (token refresh):\n', response.text)
    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get('access_token')
        api_domain = tokens.get('api_domain')
        if access_token and api_domain:
            return access_token, api_domain
        else:
            raise Exception('❌ No se recibió access_token o api_domain.')
    else:
        raise Exception(f'❌ Error al obtener access_token:\n{response.text}')
      
# 📦 Obtener registros del módulo JobOpenings
def get_job_openings_fields(access_token):
    url = "https://recruit.zoho.com/recruit/v2/settings/fields?module=JobOpenings"
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    print("🔍 Respuesta de Zoho (Job Openings fields):\n", response.text)
    if response.status_code == 200:
        return response.json().get("fields", [])
    else:
        raise Exception(f"❌ Error al obtener campos del módulo Job Openings:\n{response.text}")
    
# 📄 Exportar nombres de campos desde un registro real
def export_fields_to_excel(fields):
    if not fields:
        print("⚠️ No hay campos disponibles.")
        return

    # Extraer nombre visible, nombre interno y tipo de dato
    field_data = [{
        'Etiqueta del Campo': field.get('field_label', 'SinNombre'),
        'Nombre Interno (API)': field.get('api_name', 'SinNombre'),
        'Tipo de Dato': field.get('data_type', 'Desconocido')
    } for field in fields]

    df = pd.DataFrame(field_data)
    df.to_excel('campos_detectados_job_openings.xlsx', index=False)
    print('✅ Archivo generado: campos_detectados_job_openings.xlsx')
    
# 🚀 Flujo principal
if __name__ == '__main__':
    try:
        print('🔐 Obteniendo access_token...')
        access_token, api_domain = get_access_token_from_refresh(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
        
        print('📦 Obteniendo registros del módulo Job Openings...')
        fields = get_job_openings_fields(access_token)

        print('📄 Exportando campos desde primer registro...')
        export_fields_to_excel(fields)

    except Exception as e:
        print(e)
