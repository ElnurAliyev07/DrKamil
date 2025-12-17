# Medical Practice Website

A modern, SEO-optimized Django web application for medical practices specializing in cosmetic surgery and rhinoplasty procedures.

## ✨ Features

- **Multilingual Support** - Built-in internationalization with Django Parler
- **SEO Optimized** - Advanced SEO management with custom meta tags and structured data
- **Content Management** - Rich text editing with CKEditor integration
- **Responsive Design** - Mobile-first approach for all devices
- **Admin Dashboard** - Beautiful admin interface with Django Jazzmin
- **Blog System** - Integrated blog for medical articles and updates
- **Contact Forms** - Patient inquiry and appointment booking system
- **Media Management** - Optimized image handling with Pillow

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or pipenv

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-name>
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

## 🏗️ Project Structure

```
├── apps/
│   ├── core/          # Core functionality and settings
│   ├── home/          # Homepage content
│   ├── about/         # About page and doctor information
│   ├── blog/          # Medical articles and news
│   ├── contact/       # Contact forms and information
│   └── rinoplastika/  # Rhinoplasty specific content
├── config/            # Django configuration
├── media/             # User uploaded files
├── static/            # Static assets (CSS, JS, images)
└── templates/         # HTML templates
```

## 🛠️ Technology Stack

- **Backend**: Django 4.x
- **Database**: SQLite (development) / PostgreSQL (production)
- **Admin**: Django Jazzmin
- **Editor**: CKEditor
- **Internationalization**: Django Parler
- **Translation**: Django Rosetta
- **Deployment**: Gunicorn + WhiteNoise

## 🌐 Deployment

### Production Setup

1. **Environment variables**
   ```bash
   DEBUG=False
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=yourdomain.com
   ```

2. **Static files**
   ```bash
   python manage.py collectstatic
   ```

3. **Database migration**
   ```bash
   python manage.py migrate
   ```

## 📱 SEO Features

- Custom meta tags for each page
- Open Graph and Twitter Card support
- Structured data markup
- XML sitemap generation
- Multilingual SEO optimization
- Image optimization and lazy loading

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and inquiries, please contact the development team or create an issue in the repository.

---

*Built with ❤️ for modern medical practices*