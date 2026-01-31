# Energy_Bot

Proyecto basado en pagina web en HTML,CSS y JavaScript sobre analisis en consumo energetico de las maquinas en pequeñas empresas. 

CHATBOT 
Modo Local: son respuestas fundamentadas en la base de conocimiento local de acuerdo a  reglas, palabras claves. En Modo API envia el mensaje a un endpoint de app.js

- **Modo Local (interno):** respuestas por reglas / palabras clave (no requiere internet).
- **Modo API (externo):** envía el mensaje a un endpoint configurable en `app.js`.

## Estructura
- `index.html`
- `styles.css`
- `app.js`

## Cómo usar
1. Abre `index.html` en tu navegador. e interactua con el bot en boton flotante
2. empiezas ha realizar preguntas sobre el consumo energetico de cada maquina.  Haz preguntas como:
   - "Cual es su funcion principal en la empresa,
   Cuanto consume en promedio por hora
   Cual es su costo energetico de  operación  por hora
   Horas de operacion en un tiempo determinado

## Conectar tu API
En `app.js`, cambia:

- `API_CONFIG.endpoint`
- `API_CONFIG.headers` (si necesitas token)
- `API_CONFIG.buildBody(...)` (si tu API espera campos distintos)
- `API_CONFIG.parseResponse(...)` (si tu API retorna un formato diferente)

> Nota: Si tu API está en otro dominio, debe permitir CORS (Access-Control-Allow-Origin).
