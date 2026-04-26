||: CS 317 Course Project: Whipping It:||
=========================================
👨‍💻 Author
Sebastian Osick
Embry-Riddle Aeronautical University
B.S. Computer Science (Applied Mathematics Minor)

📘 CookBook – “Whipping It” Web Application

A full-stack web application built with Django that allows users to create, manage, and share recipes within a structured cookbook system.

🚀 Overview

The digitized cookBook (“Whipping It”) is a dynamic recipe-sharing platform where users can:
    Create and manage recipe posts
    Organize recipes by categories and tags
    Browse recipes through a clean, modern UI
    Interact with recipes through a comment system

This project emphasizes database design, full-stack development, and user interaction features.

✨ Features:
    🧾 Recipe Management
    - Create, edit, and delete recipe posts
    - Upload images for recipes
    - Rich recipe content display
    🗂️ Organization
    - Categorize recipes (Breakfast, Dinner, Dessert, etc.)
    - Tag recipes (quick, healthy, easy, etc.)
    -  Filter recipes by category7
    - Search recipes by content/title
    🖥️ User Interface
    - Responsive grid-based layout
    - Consistent card-based design system
    - Placeholder images for missing content
    💬 Comments System
    - View comments on each recipe
    - Authenticated users can post comments
    - Comments are linked to both user and recipe
    - Chronological comment display
    🔐 Authentication
    - User registration and login
    - Personalized user content
    - Protected actions (create/edit/delete/comment)

Implementation Overview: 
- clone project repo
- create virtual environment
- install project dependencies
    pip install -r requirements.txt
- migrate database
    python manage.py migrate
- create superuser
    python manage.py createsuperuser
- start Django local server
    python manage.py runserver 

    
