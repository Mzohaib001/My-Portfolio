# Django Portfolio Website (Dynamic Prototype)

A clean, responsive, and feature-driven personal portfolio website built using Python and the Django framework. This project showcases frontend design competencies alongside structured backend logic for interactive user communication.

## 🚀 Project Overview

This web application serves as a digital portfolio to display my engineering journey, technical skills, and academic projects. While the presentation components are currently static, the backend is actively integrated with a functional user communication system.

### Key Features
- **Dynamic Contact System:** A fully operational 'Contact Me' form powered by Django that processes user input, validates messages, and securely stores data on the local server database.
- **Responsive UI/UX:** Built from scratch using modern semantic HTML5 and custom CSS3 grids/flexbox to ensure seamless cross-device compatibility (mobile, tablet, and desktop).
- **Clean Architecture:** Implemented following strict Model-View-Template (MVT) design patterns in Django for clean code separation and scalability.

---

## 🛠️ Tech Stack & Skills Used

- **Backend Framework:** Django (Python)
- **Frontend Core:** HTML5, CSS3
- **Design Concepts:** Object-Oriented Programming (OOP), Model-View-Template (MVT) Architecture
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

A quick overview of how the backend architecture is set up:
```text
├── portfolio_project/      # Main project configuration
├── core_app/               # Application handling core pages
│   ├── models.py           # Database models for the Contact Form
│   ├── views.py            # Backend logic handling form submissions
│   └── templates/          # HTML files for UI presentation
├── static/                 # CSS stylesheets and media assets
└── manage.py               # Django management script
