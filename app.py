from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_cors import CORS
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# Mock Data Storage (Replace with database in production)
programs = [
    {
        'id': 1,
        'title': 'Bachelor of Science in Computer Science',
        'degree': 'B.Sc. C.S.',
        'duration': '3 Years',
        'description': 'Comprehensive program covering software development, algorithms, and modern computing technologies.',
        'image': '/static/images/cs.jpg',
        'category': 'UG',
        'faculty': 'Science'
    },
    {
        'id': 2,
        'title': 'Bachelor of Science in Information Technology',
        'degree': 'B.Sc. I.T.',
        'duration': '3 Years',
        'description': 'Industry-focused IT program with hands-on training in latest technologies and tools.',
        'image': '/static/images/it.jpg',
        'category': 'UG',
        'faculty': 'Science'
    },
    {
        'id': 3,
        'title': 'Master of Commerce',
        'degree': 'M.Com.',
        'duration': '2 Years',
        'description': 'Advanced commerce studies with specialization in Accounting, Finance, and Business Management.',
        'image': '/static/images/m-com.jpg',
        'category': 'PG',
        'faculty': 'Commerce'
    },
    {
        'id': 4,
        'title': 'Bachelor of Arts',
        'degree': 'B.A.',
        'duration': '3 Years',
        'description': 'Comprehensive arts program with specializations in English, History, and Economics.',
        'image': '/static/images/B-A.png',
        'category': 'UG',
        'faculty': 'Arts'
    },
    {
        'id': 5,
        'title': 'Bachelor of Multimedia and Mass Communication',
        'degree': 'B.A.M.M.C.',
        'duration': '3 Years',
        'description': 'Media studies and communication program focusing on multimedia production and journalism.',
        'image': '/static/images/bammc.jpg',
        'category': 'UG',
        'faculty': 'Arts'
    },
    {
        'id': 6,
        'title': 'Bachelor of Science (PCM)',
        'degree': 'B.Sc. PCM',
        'duration': '3 Years',
        'description': 'Foundation program in Physics, Chemistry, and Mathematics with modern laboratory facilities.',
        'image': '/static/images/bsc.jpg',
        'category': 'UG',
        'faculty': 'Science'
    },
    {
        'id': 7,
        'title': 'Bachelor of Science in Data Science',
        'degree': 'B.Sc. D.S.',
        'duration': '3 Years',
        'description': 'Cutting-edge program in data analytics, machine learning, and big data technologies.',
        'image': '/static/images/ds.jpg',
        'category': 'UG',
        'faculty': 'Science'
    },
    {
        'id': 8,
        'title': 'Bachelor of Science in Hospitality Studies',
        'degree': 'B.Sc. H.S.',
        'duration': '3 Years',
        'description': 'Comprehensive program in hotel management, tourism, and hospitality services.',
        'image': '/static/images/hosp.png',
        'category': 'UG',
        'faculty': 'Science'
    },
    {
        'id': 9,
        'title': 'Master of Science in Information Technology',
        'degree': 'M.Sc. I.T.',
        'duration': '2 Years',
        'description': 'Advanced IT program with specializations in emerging technologies and research.',
        'image': '/static/images/mit.jpg',
        'category': 'PG',
        'faculty': 'Science'
    },
    {
        'id': 10,
        'title': 'Master of Science in Organic Chemistry',
        'degree': 'M.Sc. O.C.',
        'duration': '2 Years',
        'description': 'Advanced chemical research program focusing on organic chemistry and analysis.',
        'image': '/static/images/oc.jpg',
        'category': 'PG',
        'faculty': 'Science'
    },
    {
        'id': 11,
        'title': 'Bachelor of Commerce',
        'degree': 'B.Com.',
        'duration': '3 Years',
        'description': 'Foundation program in commerce, accounting, and business principles.',
        'image': '/static/images/comm.jpg',
        'category': 'UG',
        'faculty': 'Commerce'
    },
    {
        'id': 12,
        'title': 'Bachelor of Commerce in Accounting and Finance',
        'degree': 'B.Com. A&F',
        'duration': '3 Years',
        'description': 'Specialized program focusing on accounting principles and financial management.',
        'image': '/static/images/baf.jpg',
        'category': 'UG',
        'faculty': 'Commerce'
    },
    {
        'id': 13,
        'title': 'Bachelor of Management Studies',
        'degree': 'B.M.S.',
        'duration': '3 Years',
        'description': 'Business management program covering administration, marketing, and operations.',
        'image': '/static/images/bams.jpg',
        'category': 'UG',
        'faculty': 'Commerce'
    }
]

# Update the faculty data in your Flask app
faculty = [
    {
        'id': 1,
        'name': 'Dr. Lata Menon',
        'designation': 'Professor & Deputy CEO',
        'department': 'PHCASC',
        'image': '/static/images/faculty1.jpg',
        'email': 'latam@mes.ac.in',
        'qualifications': ['Ph.D.', 'M.Tech']
    },
    {
        'id': 2,
        'name': 'Dr. Rinkoo Shantanu',
        'designation': 'Principal Of PHCASC',
        'department': 'PHCASC',
        'image': '/static/images/faculty2.jpg',
        'email': 'rinklees@mes.ac.in',
        'qualifications': ['M.Com', 'Ph.D']
    },
    {
        'id': 3,
        'name': 'Dr. K.M. Vasudevan Pillai',
        'designation': 'Chairman',
        'department': 'Pillai HOCL Educational Campus',
        'image': '/static/images/faculty3.jpg',
        'email': 'kmvasudevanp@mes.ac.in',
        'qualifications': ['Ph.D.', 'M.Sc.']
    }
]

events = [
    {
        'id': 1,
        'title': 'Annual Tech Fest 2025',
        'date': 'March 15, 2025',
        'time': '10:00 AM - 5:00 PM',
        'location': 'Main Auditorium',
        'description': 'Join us for an exciting day of technology showcases, competitions, and networking opportunities.',
        'category': 'Academic'
    },
    {
        'id': 2,
        'title': 'Career Counseling Workshop',
        'date': 'March 20, 2025',
        'time': '2:00 PM - 4:00 PM',
        'location': 'Seminar Hall',
        'description': 'Expert guidance on career planning and placement preparation for final year students.',
        'category': 'Workshop'
    }
]

notices = [
    {
        'id': 1,
        'title': 'Final Examination Timetable - Semester VI',
        'date': 'October 5, 2025',
        'category': 'Examination',
        'isNew': True,
        'fileUrl': '/downloads/timetable.pdf'
    },
    {
        'id': 2,
        'title': 'Admission Notice for Academic Year 2025-26',
        'date': 'October 3, 2025',
        'category': 'Admission',
        'isNew': True
    },
    {
        'id': 3,
        'title': 'Annual Sports Meet Registration Open',
        'date': 'September 28, 2025',
        'category': 'General',
        'isNew': False
    }
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/programs')
def programs_page():
    return render_template('programs.html')

@app.route('/api/programs')
def get_programs():
    return jsonify(programs)

@app.route('/api/faculty')
def get_faculty():
    return jsonify(faculty)

@app.route('/api/events')
def get_events():
    return jsonify(events)

@app.route('/api/notices')
def get_notices():
    return jsonify(notices)

# Admin Routes
@app.route('/admin')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin/dashboard.html')

@app.route('/api/admin/login', methods=['POST'])
def admin_login_post():
    data = request.json
    # Simple authentication (Replace with proper authentication in production)
    if data.get('username') == 'admin' and data.get('password') == 'admin123':
        session['admin_logged_in'] = True
        return jsonify({'success': True, 'message': 'Login successful'})
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/api/admin/logout', methods=['POST'])
def admin_logout():
    session.pop('admin_logged_in', None)
    return jsonify({'success': True})

# CRUD Operations for Programs
@app.route('/api/admin/programs', methods=['POST'])
def add_program():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    new_id = max([p['id'] for p in programs], default=0) + 1
    new_program = {
        'id': new_id,
        'title': data['title'],
        'degree': data['degree'],
        'duration': data['duration'],
        'category': data['category'],
        'description': data['description'],
        'faculty': data['faculty'],
        'image': data.get('image', '/static/images/program-default.jpg')
    }
    programs.append(new_program)
    return jsonify(new_program), 201

@app.route('/api/admin/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    program = next((p for p in programs if p['id'] == program_id), None)
    if program:
        data = request.json
        program.update(data)
        return jsonify(program)
    return jsonify({'error': 'Program not found'}), 404

@app.route('/api/admin/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    global programs
    programs = [p for p in programs if p['id'] != program_id]
    return jsonify({'success': True})

# CRUD Operations for Faculty
@app.route('/api/admin/faculty', methods=['POST'])
def add_faculty():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    new_id = max([f['id'] for f in faculty], default=0) + 1
    new_faculty = {
        'id': new_id,
        'name': data['name'],
        'designation': data['designation'],
        'department': data['department'],
        'email': data['email'],
        'qualifications': data.get('qualifications', []),
        'image': data.get('image', '/static/images/faculty-default.jpg')
    }
    faculty.append(new_faculty)
    return jsonify(new_faculty), 201

@app.route('/api/admin/faculty/<int:faculty_id>', methods=['PUT'])
def update_faculty(faculty_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    faculty_member = next((f for f in faculty if f['id'] == faculty_id), None)
    if faculty_member:
        data = request.json
        faculty_member.update(data)
        return jsonify(faculty_member)
    return jsonify({'error': 'Faculty not found'}), 404

@app.route('/api/admin/faculty/<int:faculty_id>', methods=['DELETE'])
def delete_faculty(faculty_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    global faculty
    faculty = [f for f in faculty if f['id'] != faculty_id]
    return jsonify({'success': True})

# CRUD Operations for Events
@app.route('/api/admin/events', methods=['POST'])
def add_event():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    new_id = max([e['id'] for e in events], default=0) + 1
    new_event = {
        'id': new_id,
        'title': data['title'],
        'date': data['date'],
        'time': data['time'],
        'location': data['location'],
        'category': data['category'],
        'description': data['description'],
        'image': data.get('image', '/static/images/event-default.jpg')
    }
    events.append(new_event)
    return jsonify(new_event), 201

@app.route('/api/admin/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    event = next((e for e in events if e['id'] == event_id), None)
    if event:
        data = request.json
        event.update(data)
        return jsonify(event)
    return jsonify({'error': 'Event not found'}), 404

@app.route('/api/admin/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    global events
    events = [e for e in events if e['id'] != event_id]
    return jsonify({'success': True})

# CRUD Operations for Notices
@app.route('/api/admin/notices', methods=['POST'])
def add_notice():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    new_id = max([n['id'] for n in notices], default=0) + 1
    new_notice = {
        'id': new_id,
        'title': data['title'],
        'date': data['date'],
        'category': data['category'],
        'description': data.get('description', ''),
        'fileUrl': data.get('fileUrl', ''),
        'isNew': data.get('isNew', False)
    }
    notices.append(new_notice)
    return jsonify(new_notice), 201

@app.route('/api/admin/notices/<int:notice_id>', methods=['PUT'])
def update_notice(notice_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    notice = next((n for n in notices if n['id'] == notice_id), None)
    if notice:
        data = request.json
        notice.update(data)
        return jsonify(notice)
    return jsonify({'error': 'Notice not found'}), 404

@app.route('/api/admin/notices/<int:notice_id>', methods=['DELETE'])
def delete_notice(notice_id):
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    global notices
    notices = [n for n in notices if n['id'] != notice_id]
    return jsonify({'success': True})

# Get all data for admin
@app.route('/api/admin/data')
def get_admin_data():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    return jsonify({
        'programs': programs,
        'faculty': faculty,
        'events': events,
        'notices': notices
    })

@app.route('/faculty')
def faculty_page():
    # Full faculty data for the faculty page
    full_faculty = [
        # Leadership
        {'name': 'MR. BINIT KUMAR', 'designation': 'VICE-PRINCIPAL', 'department': 'COMMERCE', 'qualifications': ['UGC-NET', 'MIBA', 'B.A-HONS-ECONOMICS'], 'email': 'binitk@mes.ac.in'},
        {'name': 'MS. NAVNEET SANDHU', 'designation': 'LIBRARIAN', 'department': 'PHCASC', 'qualifications': ['NET', 'M.PHIL', 'M.LIB', 'B.LIB', 'B.COM.'], 'email': 'navneets@mes.ac.in'},
        
        # Arts Faculty
        {'name': 'MR. SUJITH BABU', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['UGC-NET', 'M.A-ENGLISH', 'B.A-ENGLISH'], 'email': 'sujithb@mes.ac.in'},
        {'name': 'MS. PALLAVI SHANTANU PATIL', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['MA-ENGLISH', 'BA-ENGLISH', 'SET-ENGLISH'], 'email': 'pallavip@mes.ac.in'},
        {'name': 'MS. KALAVATI UPADHYAY', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['M.A-ECONOMICS', 'B.A-ECONOMICS'], 'email': 'kalavatiu@mes.ac.in'},
        {'name': 'MS. DISHA CHOTALIYA', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['MJMC', 'B.ED', 'B.M.M.'], 'email': 'dishac@mes.ac.in'},
        {'name': 'MS. RACHANA CHORAGHE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['SET-ECO', 'M.A-ECONOMICS'], 'email': 'rachanac@mes.ac.in'},
        {'name': 'MR. PRATHAMESH C. GOKHALE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['M.A-MASS COMMUNICATION', 'B.A-POLITICAL SCIENCE', 'B.M.M.'], 'email': 'prathameshg@mes.ac.in'},
        {'name': 'MR. KEEKAN PRIYESH RAGHAVAN', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['LLB', 'MA-ENGLISH', 'BA-ENGLISH'], 'email': 'keekanr@mes.ac.in'},
        {'name': 'MR. LINU GEORGE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['MA-ENGLISH', 'BA-ENGLISH'], 'email': 'linug@mes.ac.in'},
        {'name': 'MS. SERAPHIN AMANNA', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['M.A-MASS COMMUNICATION & JOURNALISM'], 'email': 'seraphina@mes.ac.in'},
        {'name': 'MR. AVINASH KUNJU', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['MA-FILM & TELEVISION'], 'email': 'avinashk@mes.ac.in'},
        {'name': 'MS. SAHIMA S.', 'designation': 'ASSISTANT PROFESSOR', 'department': 'ARTS', 'qualifications': ['M.A', 'NET-SET'], 'email': 'sahimas@mes.ac.in'},
        
        # Science Faculty
        {'name': 'DR. JAYANTA KUMAR BEHRA', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['PH.D', 'M.SC-PHYSICS', 'B.SC-PHYSICS'], 'email': 'jayantab@mes.ac.in'},
        {'name': 'DR. VISHAKHA P. BODADE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['PH.D', 'M.SC-PHYSICAL CHEMISTRY', 'B.SC-PHYSICAL CHEMISTRY'], 'email': 'vishakhab@mes.ac.in'},
        {'name': 'DR. SAPANA CHILATE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['PH.D', 'M.SC-CHEMISTRY', 'B.SC-CHEMISTRY'], 'email': 'sapanac@mes.ac.in'},
        {'name': 'DR. ARCHANA ASHOK BHAGWAT', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['PH.D', 'SET', 'M.SC-ORGANIC CHEMISTRY', 'B.SC-CHEMISTRY'], 'email': 'archanab@mes.ac.in'},
        {'name': 'MS. PRIYANKA R. SORTE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['SET-COMPUTER SCIENCE & APPLICATION', 'M.SC-COMPUTER SCIENCE', 'B.SC-COMPUTER SCIENCE'], 'email': 'priyankas@mes.ac.in'},
        {'name': 'MS. NEETHUMOL K.G.', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-MATHEMATICS', 'B.ED.', 'B.SC- MATHEMATICS'], 'email': 'neethumolk@mes.ac.in'},
        {'name': 'MR. RAVI BARI', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-MATHEMATICS', 'B.SC-MATHEMATICS'], 'email': 'ravib@mes.ac.in'},
        {'name': 'MS. PRIYA PRAKASH', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-MATHEMATICS', 'B.ED', 'B.SC-MATHEMATICS'], 'email': 'priyap@mes.ac.in'},
        {'name': 'MS. SULABHA NANDESHWAR', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-IT', 'B.SC-IT'], 'email': 'sulabhan@mes.ac.in'},
        {'name': 'MS. ANITA NILESH MHATRE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['MCA', 'BSC-CS'], 'email': 'anitam@mes.ac.in'},
        {'name': 'MS. SONAM JANGAM', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['ME-COMPUTER'], 'email': 'sonamj@mes.ac.in'},
        {'name': 'MR. PAWAN AJAY GOSAVI', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-IT'], 'email': 'pawang@mes.ac.in'},
        {'name': 'MR. SADIQ SHAIKH', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-IT'], 'email': 'sadiqs@mes.ac.in'},
        {'name': 'MS. PRAGATI PHERWANI', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.Sc Physics'], 'email': 'pragatip@mes.ac.in'},
        {'name': 'MS. PRIYA PADAVE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['MTM', 'DEP. HMCT'], 'email': 'priyap@mes.ac.in'},
        {'name': 'MS. AKANKSHA RAWAT', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-MATHS'], 'email': 'akankshar@mes.ac.in'},
        {'name': 'MS. KRANTI VARTAK', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-IT'], 'email': 'krantiv@mes.ac.in'},
        {'name': 'MR. SHREEJITH NAIR', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-IT'], 'email': 'shreejithn@mes.ac.in'},
        {'name': 'MR. SUSMIT KHEDKAR', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-HOSPITALITY & TOURISM MGMT'], 'email': 'susmitk@mes.ac.in'},
        {'name': 'MS. KOMAL AMAR MAHINDRAKAR', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.SC-IT'], 'email': 'komalm@mes.ac.in'},
        {'name': 'MS. SHRIKALA SAWANT', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['PGDM-MBA-HR'], 'email': 'shrikalas@mes.ac.in'},
        {'name': 'MS. VARSHA S. SIVAN', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['M.Sc.', 'B.Ed.'], 'email': 'varshas@mes.ac.in'},
        {'name': 'MS. MANALI YATISH', 'designation': 'ASSISTANT PROFESSOR', 'department': 'SCIENCE', 'qualifications': ['MBA'], 'email': 'manaliy@mes.ac.in'},
        
        # Commerce Faculty
        {'name': 'DR. BABITA PANDA', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['PH-D - ECONOMICS', 'M.PHIL', 'MA-ECONOMICS', 'BA-ECONOMICS'], 'email': 'babitap@mes.ac.in'},
        {'name': 'MS. REWATI V. SOMAN', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['UGC-NET', 'PGDM', 'B.ED.', 'M.COM.', 'B.COM.'], 'email': 'rewatis@mes.ac.in'},
        {'name': 'MS. REMYA MADANGOPAL', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['GATE', 'UGC-CSIR .NET', 'M.SC-BOTANY', 'B.SC-BOTANY'], 'email': 'remyam@mes.ac.in'},
        {'name': 'MR. SUMEET A. MHATRE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['MMS-FINANCE', 'B.COM.'], 'email': 'sumeetm@mes.ac.in'},
        {'name': 'MR. VINEET MURLI', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['SET-MANAGEMENT', 'MMS-HR', 'B.COM.'], 'email': 'vineetm@mes.ac.in'},
        {'name': 'MS. HARSHITA P. SINGH', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.SC-MATHEMATICS', 'B.ED', 'B.SC-MATHEMATICS'], 'email': 'harshitas@mes.ac.in'},
        {'name': 'MS. SHREEJA JOJI', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['PGDM', 'M.COM.', 'B.COM.'], 'email': 'shreejaj@mes.ac.in'},
        {'name': 'MR. HARDIK DAVE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.COM.', 'B.ED.', 'B.COM-A&F'], 'email': 'hardikd@mes.ac.in'},
        {'name': 'MS. ARUSHI DUBE', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.COM.', 'B.COM-A&F'], 'email': 'arushid@mes.ac.in'},
        {'name': 'MS. PAULAMI RAO', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.COM.'], 'email': 'paulami@mes.ac.in'},
        {'name': 'MS. NISHITA TOTLA', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['LLB', 'M.COM.'], 'email': 'nishitat@mes.ac.in'},
        {'name': 'MS. ADITI MOHOLKAR', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.COM.'], 'email': 'aditim@mes.ac.in'},
        {'name': 'MS. SHARADHA KADAM', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.COM.', 'NET-Commerce'], 'email': 'sharadhak@mes.ac.in'},
        {'name': 'MS. SHEETAL PATARIYA', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.ED.', 'M.COM.', 'NET - COMMERCE', 'SET COMMERCE'], 'email': 'sheetalp@mes.ac.in'},
        {'name': 'DR. AMIT VERMA', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['PHD', 'M.COM.', 'B.COM.'], 'email': 'amitv@mes.ac.in'},
        {'name': 'MS. SWETA ROY CHAUDHARY', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['M.COM.', 'B.COM.'], 'email': 'swetar@mes.ac.in'},
        {'name': 'MS. SINDHUJA JOSHI', 'designation': 'ASSISTANT PROFESSOR', 'department': 'COMMERCE', 'qualifications': ['MBA', 'B.COM', 'NET-COMMERCE'], 'email': 'sindhujaj@mes.ac.in'}
    ]
    
    return render_template('faculty.html', faculty=full_faculty)

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/placements')
def placements():
    return render_template('placements.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/alumni')
def alumni():
    return render_template('alumni.html')

# New API endpoints for additional data
@app.route('/api/placement-stats')
def get_placement_stats():
    return jsonify({
        'placement_rate': 92,
        'companies_visited': 250,
        'highest_package': 8.5,
        'average_package': 4.2,
        'top_companies': ['TCS', 'Infosys', 'Wipro', 'Accenture', 'Capgemini', 'IBM']
    })

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/research-areas')
def get_research_areas():
    return jsonify([
        {
            'id': 1,
            'title': 'Science Research',
            'description': 'Advanced research in Physics, Chemistry, Biotechnology and Computer Science',
            'icon': 'fas fa-atom'
        },
        {
            'id': 2,
            'title': 'Commerce Studies', 
            'description': 'Research in emerging trends in commerce, finance and business management',
            'icon': 'fas fa-chart-line'
        },
        {
            'id': 3,
            'title': 'Arts & Humanities',
            'description': 'Exploring literature, languages, and cultural studies with modern perspectives',
            'icon': 'fas fa-theater-masks'
        }
    ])

@app.route('/api/contact', methods=['POST'])
def contact_form():
    data = request.json
    # Here you would typically save to database or send email
    print(f"Contact form submission: {data}")
    return jsonify({'success': True, 'message': 'Thank you for your message. We will get back to you soon!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)