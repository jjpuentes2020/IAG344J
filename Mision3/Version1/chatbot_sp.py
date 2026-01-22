#scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Función de entrenamiento preguntas y respuestas
def build_and_train_model(train_pairs):
    #train_pairs lista de pares(pregunta,respuestas)
    #Ejemplo [("Hola","!Hola¡"),("adiós","¡Hasta luego!")]
    # separamos las preguntas y respuestas en dos listas
    questions =[q for q, _ in train_pairs]# lista de preguntas
    answers =[a for _, a in train_pairs]  # lista de respuestar
    # creamos el vectorizado, que traducirá el texto a números
    vectorizer=CountVectorizer()
    #Entrenamiento
    x = vectorizer.fit_transform(questions)
    # obtenemos una lista de respuestas Únicas
    unique_answers = sorted(set(answers))
    # crear el dicionario con las etiquetas
    answer_to_label={a: i for i, a in enumerate(unique_answers)}
    #creamos una lista
    y=[answer_to_label[a] for a in answers]
    #Modelo clasificación de texto
    model = MultinomialNB()
    #Entrenar el modelo
    model.fit(x,y)
    return model,vectorizer,unique_answers
# función predict_answer
def predict_answer(model,vectorizer,unique_answers,user_text):
    # convertimos el texto a números
    x = vectorizer.transform([user_text])
    # el modelo predice la etiqueta de la respuesta correcta
    label = model.predict(x)[0]
    return unique_answers[label]
# Programa principal
if __name__ == "__main__":
    training_data = [
      
    # Saludos
    ("hola", "¡Hola! Bienvenido al SENA. ¿En qué podemos ayudarte hoy?"),
    ("buenos días", "Buenos días. ¿Te interesa conocer nuestra oferta formativa?"),
    ("buenas tardes", "Buenas tardes. Estoy aquí para ayudarte con información del SENA."),
    ("buenas noches", "Buenas noches. ¿Deseas información sobre programas del SENA?"),

    # Información general
    ("qué es el sena", "El SENA es una institución pública que ofrece formación gratuita para el desarrollo técnico y profesional."),
    ("información del sena", "El SENA ofrece programas de formación técnica, tecnológica y complementaria de manera gratuita."),

    # Oferta formativa
    ("oferta formativa", "El SENA ofrece programas técnicos, tecnológicos, cursos cortos y formación virtual y presencial."),
    ("qué programas ofrece el sena", "El SENA ofrece programas técnicos, tecnológicos, especializaciones y cursos complementarios."),
    ("programas disponibles", "Puedes encontrar programas en áreas como tecnología, industria, salud, comercio y agro."),

    # Modalidades
    ("modalidad virtual", "El SENA ofrece programas en modalidad virtual para que estudies desde cualquier lugar."),
    ("modalidad presencial", "La formación presencial se imparte en los centros de formación del SENA."),
    ("modalidad mixta", "Algunos programas del SENA combinan formación virtual y presencial."),

    # Inscripción
    ("cómo inscribirse", "Puedes inscribirte a través de la plataforma Sofia Plus en las fechas establecidas."),
    ("inscripciones sena", "Las inscripciones se realizan en línea mediante Sofia Plus."),
    ("cuándo hay inscripciones", "El SENA publica periódicamente las fechas de inscripción en su oferta formativa."),

    # Requisitos
    ("requisitos", "Los requisitos dependen del programa, pero generalmente incluyen documento de identidad y nivel educativo."),
    ("qué necesito para inscribirme", "Necesitas estar registrado en Sofia Plus y cumplir los requisitos del programa."),

    # Certificación
    ("certificado", "Al finalizar y aprobar el programa, el SENA otorga un certificado oficial."),
    ("certificación sena", "Los programas del SENA cuentan con certificación reconocida a nivel nacional."),

    # Costos
    ("cuánto cuesta estudiar en el sena", "La formación en el SENA es completamente gratuita."),
    ("precio", "Los programas del SENA no tienen ningún costo."),

    # Duración
    ("duración de los programas", "La duración varía según el programa, desde cursos cortos hasta programas tecnológicos."),
    ("cuánto dura un técnico", "Un programa técnico suele durar aproximadamente un año."),

    # Soporte y contacto
    ("ayuda", "Con gusto te ayudamos. ¿Qué información necesitas?"),
    ("soporte", "Puedes recibir apoyo a través de los canales de atención del SENA."),
    ("contacto", "Puedes comunicarte con el SENA mediante sus líneas de atención y su sitio web."),

    # Despedida
    ("gracias", "Gracias por tu interés en el SENA. ¡Éxitos en tu proceso de formación!"),
    ("adiós", "Hasta luego. Estamos atentos a cualquier otra consulta sobre el SENA."),

    ("hola", "¡Hola! ¿En qué podemos ayudarte hoy?"),
    ("buenos días", "Buenos días, gracias por contactarnos. ¿Cómo podemos asistirte?"),
    ("buenas tardes", "Buenas tardes, es un gusto atenderte. ¿Qué consulta tienes?"),
    ("buenas noches", "Buenas noches, estamos a tu disposición. ¿En qué podemos ayudarte?"),
    ("información", "Con gusto te brindamos la información que necesitas. ¿Sobre qué tema?"),
    ("soporte", "Nuestro equipo de soporte está listo para ayudarte. Cuéntanos tu inconveniente."),
    ("precio", "Con gusto te compartimos nuestros precios. ¿Qué servicio te interesa?"),
    ("gracias", "Gracias a ti por comunicarte con nosotros. ¡Que tengas un excelente día!")

    ]
    #Entrenar el modelo con la lista
    model,vectorizer,unique_answers=build_and_train_model(training_data)
    #Mostrar un mensaje inicial al usuario
    print("Chatbot supervisado listo,Escribe Salir para terminar.\n")
    while True:
        #Pedimos una frase al usuario
        user =input("Tú: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("Bot: !Hasta pronto¡")
            break
        response=predict_answer(model,vectorizer,unique_answers,user)
        print("Bot: ",response)