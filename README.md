# Base Frontend-Backend Project Template

[🇹🇭 อ่านเป็นภาษาไทย](README_TH.md)

A modern, full-stack web application template with Nuxt 3 frontend and Flask backend, featuring TailwindCSS for beautiful, responsive design.

## 🚀 Features

### Frontend (Nuxt 3)
- **Modern Vue.js Framework** - Built with Nuxt 3 for optimal performance
- **TailwindCSS Integration** - Beautiful, responsive design system
- **Component-Based Architecture** - Reusable components with proper layout structure
- **TypeScript Support** - Full TypeScript integration for better development experience
- **Hot Module Replacement** - Fast development with instant updates
- **SEO Optimized** - Built-in SEO features and meta tag management

### Backend (Flask)
- **RESTful API** - Clean, scalable API architecture
- **Authentication System** - User authentication and authorization
- **Database Models** - SQLAlchemy ORM with proper model structure
- **Configuration Management** - Environment-based configuration
- **Route Organization** - Modular route structure for scalability

## 📁 Project Structure

```
base-frontend-backend/
├── frontend/                 # Nuxt 3 Frontend Application
│   ├── components/          # Vue Components
│   │   ├── Header.vue      # Navigation component
│   │   └── Footer.vue      # Footer component
│   ├── layouts/            # Page Layouts
│   │   └── default.vue     # Default layout with nav/footer
│   ├── pages/              # Application Pages
│   │   └── index.vue       # Home page with beautiful design
│   ├── assets/             # Static Assets
│   │   └── css/
│   │       └── main.css    # TailwindCSS imports
│   ├── public/             # Public Assets
│   ├── nuxt.config.ts      # Nuxt Configuration
│   ├── tailwind.config.js  # TailwindCSS Configuration
│   └── package.json        # Frontend Dependencies
├── backend/                # Flask Backend Application
│   ├── routes/             # API Routes
│   │   └── auth.py         # Authentication routes
│   ├── app.py              # Main Flask application
│   ├── config.py           # Configuration settings
│   ├── models.py           # Database models
│   └── requirements.txt    # Python dependencies
└── README.md              # This file
```

## 🛠️ Technology Stack

### Frontend
- **Nuxt 3** - Vue.js framework for modern web applications
- **Vue 3** - Progressive JavaScript framework
- **TailwindCSS 3** - Utility-first CSS framework
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool and dev server

### Backend
- **Flask** - Lightweight Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Python 3.8+** - Modern Python runtime
- **RESTful API** - Clean API design principles

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Git

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend will be available at: http://localhost:3000

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Backend API will be available at: http://localhost:5000

## 📝 Available Scripts

### Frontend (in frontend/ directory)
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run generate` - Generate static site
- `npm run preview` - Preview production build

### Backend (in backend/ directory)
- `python app.py` - Start Flask development server
- `flask run` - Alternative way to start server

## 🎨 Design Features

The template includes a beautiful, modern design with:

- **Responsive Navigation** - Sticky header with backdrop blur
- **Hero Section** - Eye-catching landing area with gradient text
- **Feature Cards** - Hover animations and modern styling
- **Statistics Section** - Gradient background with key metrics
- **Call-to-Action** - Engaging buttons with hover effects
- **Professional Footer** - Organized links and branding

## 🔧 Configuration

### Frontend Configuration
- **TailwindCSS**: Configured in `tailwind.config.js`
- **Nuxt**: Settings in `nuxt.config.ts`
- **PostCSS**: Integrated for TailwindCSS processing

### Backend Configuration
- **Environment Variables**: Use `.env` file for sensitive data
- **Database**: Configure in `config.py`
- **CORS**: Set up for frontend-backend communication

## 📦 Dependencies

### Frontend Dependencies
- `nuxt`: ^3.18.1
- `vue`: ^3.5.18
- `tailwindcss`: ^3.4.0
- `postcss`: Latest
- `autoprefixer`: Latest

### Backend Dependencies
- `flask`: Latest
- `flask-sqlalchemy`: Latest
- `flask-cors`: Latest
- `python-dotenv`: Latest

## 🎯 Use Cases

This template is perfect for:
- **Web Applications** - Full-stack web apps
- **API Services** - Backend API with frontend client
- **Portfolio Projects** - Showcase your development skills
- **MVP Development** - Rapid prototyping
- **Learning Projects** - Modern web development practices

## 🔄 Reusing This Template

1. **Clone or Copy** this project folder
2. **Rename** the project directory
3. **Update** package.json and requirements.txt with your project name
4. **Customize** the design and functionality
5. **Add** your specific features and requirements

## 📚 Next Steps

After setting up this template, consider adding:
- **Database Integration** - Connect to PostgreSQL, MySQL, or MongoDB
- **Authentication** - JWT tokens, OAuth, or session-based auth
- **State Management** - Pinia for Vue 3 state management
- **Testing** - Unit and integration tests
- **Deployment** - Docker configuration, CI/CD pipelines
- **Monitoring** - Logging and error tracking

## 🤝 Contributing

Feel free to enhance this template by:
- Adding new features
- Improving the design
- Optimizing performance
- Adding more documentation

## 📄 License

This template is open source and available under the MIT License.

---

**Happy Coding! 🚀**
