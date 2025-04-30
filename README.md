# Catalogue Summarizer

Une API légère développée avec **FastAPI** qui permet de générer automatiquement un résumé concis d’un livre à partir d’un long texte, en utilisant **OpenAI GPT-4o**.

## ✨ Fonctionnalités

- [x] Envoi d’un long texte (extrait ou chapitre de livre)
- [x] Génération automatique d’un résumé avec l'API OpenAI
- [x] API rapide, simple, documentée via Swagger UI
- [x] Déployable facilement avec Docker

---

## 🚀 Lancer le projet en local

```shell
git clone https://github.com/CorentinLeGuen/catalogue-summarizer.git
cd catalogue-summarizer
docker-compose up --build -d
```

[![fastapi](https://img.shields.io/badge/Catalogue%20Summarizer%20API-dodgerblue?style=for-the-badge)](http://127.0.0.1:8011/)
[![fastapi docs](https://img.shields.io/badge/Swagger%20UI-dodgerblue?style=for-the-badge)](http://127.0.0.1:8011/docs)
