# Mediapolis

A complex multimedia platform built with Django, consisting of multiple apps (blog, music, videos) and a gateway to navigate between them.

![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Apps](#apps)
	* [Blog App](#blog-app)
	* [Music App](#music-app)
	* [Videos App](#videos-app)
5. [Gateway App](#gateway-app)
6. [Getting Started](#getting-started)
7. [Requirements](#requirements)

## Introduction

---

This project is a complex multimedia platform built with Django, consisting of multiple apps and a gateway to navigate between them.

## Features

---

* User authentication with login and logout functionality
* Multiple content management systems for creating, editing, and deleting articles, music files, and video uploads
* Basic article, music file, and video models with title, content, artist/author fields, etc.
* Support for HTML formatting in article content
* Gateway app to navigate between multiple apps

## Architecture

---

Mediapolis is a single Django project consisting of multiple apps:

* Blog App: handles blog-related functionality
* Music App: handles music-related functionality
* Videos App: handles video-related functionality
* Gateway App: serves as an entry point for users to navigate between other apps

## Getting Started

---

### Clone the Repository

Clone this repository to your local machine using:
```bash
git clone https://github.com/your-username/mediapolis.git
```

### Create a Virtual Environment (Optional)

Create a new virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows
```

### Install Dependencies

Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Requirements

---------------

* Python 3.9+
* Django 4.2+
* Postgresql 13

## Installation

---

Run database migrations to create tables for user, article, music file, video models:
```bash
python manage.py migrate
```

Create an admin account using:
```bash
python manage.py createsuperuser
```

Start the development server using:
```bash
python manage.py runserver
```

You can now access your multimedia platform at `http://localhost:8000/`.

## Contributing

---

Contributions are welcome! If you'd like to contribute, please fork this repository and submit a pull request.

## License

---

This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.

