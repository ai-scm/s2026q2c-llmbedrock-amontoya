# AWS AI Practitioner Assistant

Asistente conversacional especializado en conceptos de Generative AI, Large Language Models (LLMs) y Retrieval-Augmented Generation (RAG), desarrollado con Streamlit y Amazon Bedrock.

## Objetivo

Brindar apoyo a estudiantes que se preparan para la certificación AWS AI Practitioner mediante una interfaz de chat que permite:

* Resolver dudas sobre IA generativa.
* Explicar conceptos relacionados con LLMs.
* Enseñar fundamentos de RAG.
* Generar preguntas de práctica.
* Evaluar respuestas y proporcionar retroalimentación.

## Tecnologías utilizadas

* Python 3.11
* Streamlit
* Amazon Bedrock
* Amazon Nova Lite
* Boto3
* Docker
* Docker Compose

## Modelo utilizado

**Amazon Nova Lite**

El modelo es consumido a través de Amazon Bedrock y se utiliza para generar respuestas conversacionales especializadas en temas de IA generativa y preparación para la certificación AWS AI Practitioner.

## Capacidades del asistente

* Explicación de conceptos de IA generativa.
* Explicación de arquitecturas RAG.
* Conceptos fundamentales de Large Language Models.
* Generación de preguntas tipo certificación.
* Evaluación de respuestas del estudiante.
* Mantenimiento del contexto conversacional mediante historial de sesión.

## Estructura del proyecto

```text
s2026q2c-llmbedrock-amontoya/
│
├── app/
│   ├── main.py
│   ├── chatbot.py
│   └── prompts.py
│
├── docker/
│   └── Dockerfile
│
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### Descripción de componentes

| Archivo            | Descripción                                                    |
| ------------------ | -------------------------------------------------------------- |
| main.py            | Interfaz web desarrollada con Streamlit.                       |
| chatbot.py         | Comunicación con Amazon Bedrock y generación de respuestas.    |
| prompts.py         | Definición del comportamiento y especialización del asistente. |
| Dockerfile         | Contenerización de la aplicación.                              |
| docker-compose.yml | Ejecución local mediante Docker Compose.                       |

## Variables de entorno

Crear un archivo `.env` basado en el siguiente ejemplo:

```env
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SESSION_TOKEN=
AWS_REGION=us-east-1

MODEL_ID=amazon.nova-lite-v1:0
```

## Ejecución local

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

### Ejecución con Streamlit

```bash
streamlit run app/main.py
```

La aplicación estará disponible en:

```text
http://localhost:8501
```

## Ejecución con Docker

### Construcción

```bash
docker compose build
```

### Inicio

```bash
docker compose up
```

La aplicación estará disponible en:

```text
http://localhost:8501
```

## Autor

Alejandro Montoya

Semillero - Ejercicio práctico Amazon Bedrock

