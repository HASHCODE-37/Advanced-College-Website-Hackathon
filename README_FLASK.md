# Pillai HOC College Website - Flask Version

A modern, responsive college website built with HTML, CSS, JavaScript, and Flask backend.

## 📁 Project Structure

```
.
├── app.py                      # Flask application (main backend)
├── static/
│   ├── css/
│   │   └── style.css          # All CSS styles
│   ├── js/
│   │   └── main.js            # JavaScript functionality
│   └── images/                # Store your images here
│       ├── campus.jpg
│       ├── library.jpg
│       ├── science-lab.jpg
│       ├── computer-lab.jpg
│       ├── faculty1.jpg
│       ├── faculty2.jpg
│       └── faculty3.jpg
├── templates/
│   ├── index.html             # Homepage
│   └── admin/
│       ├── login.html         # Admin login page
│       └── dashboard.html     # Admin dashboard
└── README_FLASK.md            # This file
```

## 🚀 Installation & Setup

### 1. Install Python Dependencies

```bash
pip install Flask Flask-CORS
```

### 2. Add Images

Place your college images in the `static/images/` folder:
- `campus.jpg` - College campus/building exterior
- `library.jpg` - Library interior
- `science-lab.jpg` - Science laboratory
- `computer-lab.jpg` - Computer lab
- `faculty1.jpg`, `faculty2.jpg`, `faculty3.jpg` - Faculty photos

### 3. Run the Application

```bash
python app.py
```

The website will be available at: **http://localhost:5000**

## 🔐 Admin Login Credentials

- **Username:** `admin`
- **Password:** `admin123`

Access admin panel at: **http://localhost:5000/admin**

## ✨ Features

### Public Website
- ✅ Responsive navbar with dropdown menus
- ✅ Hero section with campus image and stats
- ✅ Featured programs showcase
- ✅ Faculty directory
- ✅ Events and notices section
- ✅ Dark/Light theme toggle
- ✅ Mobile-responsive design

### Admin Dashboard
- ✅ Secure login system
- ✅ Dashboard with statistics
- ✅ Manage programs (CRUD operations)
- ✅ Manage faculty members
- ✅ Manage events
- ✅ Manage notices
- ✅ Recent activities tracking

## 📡 API Endpoints

### Public Endpoints
- `GET /` - Homepage
- `GET /api/programs` - Get all programs
- `GET /api/faculty` - Get all faculty
- `GET /api/events` - Get all events
- `GET /api/notices` - Get all notices

### Admin Endpoints (Requires Authentication)
- `POST /api/admin/login` - Admin login
- `POST /api/admin/logout` - Admin logout
- `POST /api/admin/programs` - Add new program
- `PUT /api/admin/programs/<id>` - Update program
- `DELETE /api/admin/programs/<id>` - Delete program
- `POST /api/admin/faculty` - Add faculty member
- `POST /api/admin/events` - Add event
- `POST /api/admin/notices` - Add notice

## 🎨 Customization

### Colors
Edit `static/css/style.css` and modify the CSS variables in `:root`:

```css
:root {
  --primary-color: #2563eb;      /* Primary blue */
  --secondary-color: #f97316;    /* Secondary orange */
  --background: #fafafa;         /* Light background */
  /* ... more colors */
}
```

### Content
1. **Programs:** Edit the `programs` array in `app.py`
2. **Faculty:** Edit the `faculty` array in `app.py`
3. **Events:** Edit the `events` array in `app.py`
4. **Notices:** Edit the `notices` array in `app.py`

## 🗄️ Database Integration (Optional)

To use a real database instead of in-memory storage:

1. Install SQLAlchemy:
```bash
pip install Flask-SQLAlchemy
```

2. Replace the arrays in `app.py` with database models
3. Create database tables and migrate data

## 📱 Mobile Responsive

The website is fully responsive and works on:
- 📱 Mobile phones (320px+)
- 📱 Tablets (768px+)
- 💻 Desktops (1024px+)
- 🖥️ Large screens (1280px+)

## 🔒 Security Notes

**Important for Production:**
1. Change the admin credentials
2. Use environment variables for secrets
3. Implement proper password hashing (bcrypt)
4. Add CSRF protection
5. Use HTTPS
6. Implement rate limiting
7. Add input validation and sanitization
8. Use a real database (PostgreSQL/MySQL)

## 📝 File Descriptions

### `app.py`
Main Flask application with:
- Route definitions
- API endpoints
- Session management
- CRUD operations
- Mock data storage

### `static/css/style.css`
Complete styling including:
- CSS variables for theming
- Responsive layouts
- Card designs
- Navigation styles
- Dark mode support

### `static/js/main.js`
JavaScript functionality:
- Theme toggle
- Data fetching from API
- Dynamic content rendering
- Mobile menu

### `templates/index.html`
Homepage with:
- Hero section
- Programs showcase
- Faculty directory
- Events and notices
- Footer

### `templates/admin/login.html`
Admin login interface

### `templates/admin/dashboard.html`
Admin panel with:
- Sidebar navigation
- Statistics cards
- Data management tables

## 🚀 Production Deployment

For production deployment:

1. **Use a production WSGI server:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **Use environment variables:**
```python
import os
app.secret_key = os.environ.get('SECRET_KEY')
```

3. **Configure database connection**
4. **Set up reverse proxy (Nginx)**
5. **Enable HTTPS with SSL certificate**

## 📞 Support

For issues or questions:
- Email: info@phcasc.ac.in
- Phone: +91 22 2745 xxxx

## 📄 License

© 2025 Pillai HOC College. All rights reserved.
