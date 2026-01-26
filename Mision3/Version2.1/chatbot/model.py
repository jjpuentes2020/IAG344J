
#scikit-learn
# Se instala para entrenar modelos propios (como MultinomialNB) usando tus propios datos.
import os
os.environ["GROQ_API_KEY"]=""
from groq import Groq


#import pickle
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import MultinomialNB

MODEL_DIR= "models"
MODEL_PATH =os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH=os.path.join(MODEL_DIR,"vectorizer.pkl")
ANSWERS_PATH=os.path.join(MODEL_DIR,"answers.pkl")

#Función de entrenamiento preguntas y respuestas
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
chat_completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile", #Modelo apropiado para español
    messages=[
        {
            "role":"system",
            "content":(
                "Eres un experto en Microsoft Excel y análisis de datos. "
                "Tu tarea es interpretar instrucciones en lenguaje natural "
                "y extraer la instrucción del usuario. \n\n"
                "Debes identificar: \n"
                "- la acción principal (sumar,filtrar,ordenar,agrupar,etc.)\n"
                "- las columnas involucradas\n"
                " - las condiciones si existen\n"
                "Devuelve SIEMPRE la respuesta en formato JSON con esta estructura: \n"

                "{\n"
                ' "accion": "",\n'
                ' "columnas":[],\n'
                ' "condiciones":[],\n'
                ' "resultado": ""\n'
                "}" 

            ) 
        },
         {
             "role":"user",
             "content": "quiero sumar las ventas por vendedor solo el año 2024 "         
        }
    ],
    
)
print(chat_completion.choices[0].message.content)