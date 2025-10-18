// Theme Toggle
function initTheme() {
  const themeToggle = document.getElementById('theme-toggle');
  const currentTheme = localStorage.getItem('theme') || 'light';
  
  document.documentElement.classList.toggle('dark', currentTheme === 'dark');
  updateThemeIcon(currentTheme);
  
  themeToggle?.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    const newTheme = isDark ? 'dark' : 'light';
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
  });
}

function updateThemeIcon(theme) {
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.innerHTML = theme === 'dark' 
      ? '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'
      : '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }
}

// Mobile Menu
function initMobileMenu() {
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');
  
  mobileBtn?.addEventListener('click', () => {
    navLinks?.classList.toggle('show');
  });
}

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    target?.scrollIntoView({ behavior: 'smooth' });
  });
});

// Load Programs
async function loadPrograms() {
  try {
    const response = await fetch('/api/programs');
    const programs = await response.json();
    
    const container = document.getElementById('programs-grid');
    if (!container) return;
    
    container.innerHTML = programs.map(program => `
      <div class="card">
        <img src="${program.image}" alt="${program.title}" class="card-img">
        <div class="card-content">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span class="badge badge-${program.category === 'UG' ? 'primary' : 'secondary'}">${program.category}</span>
            <span style="font-size: 0.875rem; color: var(--text-secondary);">${program.duration}</span>
          </div>
          <h3 class="card-title">${program.degree}</h3>
          <p class="card-text">${program.description}</p>
        </div>
      </div>
    `).join('');
  } catch (error) {
    console.error('Error loading programs:', error);
  }
}

// Load Faculty
async function loadFaculty() {
  try {
    const response = await fetch('/api/faculty');
    const faculty = await response.json();
    
    const container = document.getElementById('faculty-grid');
    if (!container) return;
    
    container.innerHTML = faculty.map(member => `
      <div class="card">
        <div class="card-content" style="text-align: center;">
          <div style="width: 80px; height: 80px; border-radius: 50%; overflow: hidden; margin: 0 auto 1rem; border: 2px solid var(--primary-color);">
            <img src="${member.image}" alt="${member.name}" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <h3 style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.25rem;">${member.name}</h3>
          <p style="font-size: 0.875rem; color: var(--text-secondary); margin-bottom: 0.5rem;">${member.designation}</p>
          <span class="badge badge-primary">${member.department}</span>
          ${member.qualifications ? `
            <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
              ${member.qualifications.map(q => `<span class="badge" style="background: var(--background); color: var(--text-primary); border: 1px solid var(--border-color);">${q}</span>`).join('')}
            </div>
          ` : ''}
        </div>
      </div>
    `).join('');
  } catch (error) {
    console.error('Error loading faculty:', error);
  }
}

// Load Events
async function loadEvents() {
  try {
    const response = await fetch('/api/events');
    const events = await response.json();
    
    const container = document.getElementById('events-list');
    if (!container) return;
    
    container.innerHTML = events.map(event => `
      <div class="card">
        ${event.image ? `<img src="${event.image}" alt="${event.title}" class="card-img">` : ''}
        <div class="card-content">
          <span class="badge badge-primary" style="margin-bottom: 0.5rem;">${event.category}</span>
          <h3 class="card-title">${event.title}</h3>
          <p class="card-text">${event.description}</p>
          <div style="font-size: 0.875rem; color: var(--text-secondary); margin-top: 1rem;">
            <div style="margin-bottom: 0.5rem;">📅 ${event.date}</div>
            <div style="margin-bottom: 0.5rem;">🕐 ${event.time}</div>
            <div>📍 ${event.location}</div>
          </div>
        </div>
      </div>
    `).join('');
  } catch (error) {
    console.error('Error loading events:', error);
  }
}

// Load Notices
async function loadNotices() {
  try {
    const response = await fetch('/api/notices');
    const notices = await response.json();
    
    const container = document.getElementById('notices-list');
    if (!container) return;
    
    container.innerHTML = notices.map(notice => `
      <div class="card">
        <div class="card-content">
          <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.75rem;">
            <span class="badge badge-${notice.category === 'Examination' ? 'primary' : 'secondary'}">${notice.category}</span>
            ${notice.isNew ? '<span class="badge" style="background: #f97316; color: white;">New</span>' : ''}
          </div>
          <h3 style="font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem;">${notice.title}</h3>
          <p style="font-size: 0.875rem; color: var(--text-secondary);">${notice.date}</p>
          <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
            <button class="btn btn-outline" style="flex: 1; font-size: 0.875rem;">View</button>
            ${notice.fileUrl ? '<button class="btn btn-outline" style="flex: 1; font-size: 0.875rem;">Download</button>' : ''}
          </div>
        </div>
      </div>
    `).join('');
  } catch (error) {
    console.error('Error loading notices:', error);
  }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  loadPrograms();
  loadFaculty();
  loadEvents();
  loadNotices();
});

// Add these new functions to your existing main.js

// Load Research Areas
async function loadResearchAreas() {
  try {
    const response = await fetch('/api/research-areas');
    const researchAreas = await response.json();
    
    const container = document.getElementById('research-areas');
    if (!container) return;
    
    container.innerHTML = researchAreas.map(area => `
      <div class="research-card">
        <i class="${area.icon}"></i>
        <h3>${area.title}</h3>
        <p>${area.description}</p>
      </div>
    `).join('');
  } catch (error) {
    console.error('Error loading research areas:', error);
  }
}

// Load Placement Stats
async function loadPlacementStats() {
  try {
    const response = await fetch('/api/placement-stats');
    const stats = await response.json();
    
    // Update placement stats in the DOM
    document.querySelectorAll('.placement-stat .stat-number').forEach((el, index) => {
      const values = [stats.placement_rate + '%', stats.companies_visited + '+', '₹' + stats.highest_package + 'L', '₹' + stats.average_package + 'L'];
      if (values[index]) {
        el.textContent = values[index];
      }
    });
    
    // Update companies grid
    const companiesGrid = document.querySelector('.companies-grid');
    if (companiesGrid) {
      companiesGrid.innerHTML = stats.top_companies.map(company => `
        <div class="company-logo">${company}</div>
      `).join('');
    }
  } catch (error) {
    console.error('Error loading placement stats:', error);
  }
}

// Contact Form Handler
function initContactForm() {
  const contactForm = document.getElementById('contactForm');
  if (!contactForm) return;
  
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(contactForm);
    const data = {
      name: contactForm.querySelector('input[type="text"]').value,
      email: contactForm.querySelector('input[type="email"]').value,
      subject: contactForm.querySelectorAll('input[type="text"]')[1].value,
      message: contactForm.querySelector('textarea').value
    };
    
    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      
      const result = await response.json();
      
      if (result.success) {
        alert('Thank you for your message! We will get back to you soon.');
        contactForm.reset();
      } else {
        alert('There was an error sending your message. Please try again.');
      }
    } catch (error) {
      console.error('Error sending contact form:', error);
      alert('There was an error sending your message. Please try again.');
    }
  });
}

// Smooth scrolling for navigation
function initSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Update the initialization function
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  initSmoothScrolling();
  initContactForm();
  loadPrograms();
  loadFaculty();
  loadEvents();
  loadNotices();
  loadResearchAreas();
  loadPlacementStats();
});

// Search functionality
function initSearch() {
    const searchInput = document.getElementById('faculty-search');
    
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase().trim();
        
        if (searchTerm === '') {
            // If search is empty, show filtered results based on current department filter
            const activeFilter = document.querySelector('.filter-btn.active');
            renderFaculty(activeFilter.dataset.department);
            return;
        }
        
        // Filter faculty based on search term
        const activeFilter = document.querySelector('.filter-btn.active');
        const filteredByDepartment = activeFilter.dataset.department === 'all' 
            ? facultyData 
            : facultyData.filter(f => f.department === activeFilter.dataset.department);
        
        const searchResults = filteredByDepartment.filter(member => 
            member.name.toLowerCase().includes(searchTerm) ||
            member.designation.toLowerCase().includes(searchTerm) ||
            member.department.toLowerCase().includes(searchTerm) ||
            member.qualifications.some(qual => qual.toLowerCase().includes(searchTerm)) ||
            member.email.toLowerCase().includes(searchTerm)
        );
        
        renderSearchResults(searchResults, searchTerm);
    });
}

function renderSearchResults(results, searchTerm) {
    const container = document.getElementById('faculty-container');
    
    if (results.length === 0) {
        container.innerHTML = `
            <div class="no-results">
                <i class="fas fa-search" style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.5;"></i>
                <h3>No faculty members found</h3>
                <p>No results found for "${searchTerm}". Try searching with different keywords.</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = results.map(member => `
        <div class="faculty-card">
            <div class="faculty-name">${member.name}</div>
            <div class="faculty-designation">${member.designation}</div>
            <div class="faculty-department">${member.department}</div>
            
            <div class="faculty-qualifications">
                ${member.qualifications.map(q => `
                    <span class="qualification-tag">${q}</span>
                `).join('')}
            </div>
            
            <div class="faculty-email">
                <i class="fas fa-envelope"></i>
                <a href="mailto:${member.email}">${member.email}</a>
            </div>
        </div>
    `).join('');
}
