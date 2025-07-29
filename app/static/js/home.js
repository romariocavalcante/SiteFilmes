// Netflix-style Home Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Profile Dropdown Functionality
    const userProfile = document.getElementById('userProfile');
    const profileDropdown = document.getElementById('profileDropdown');
    
    console.log('User Profile Element:', userProfile);
    console.log('Profile Dropdown Element:', profileDropdown);
    
    if (userProfile && profileDropdown) {
        console.log('Profile dropdown elements found, setting up functionality...');
        
        // Toggle dropdown on click
        userProfile.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('Profile clicked, toggling dropdown...');
            
            profileDropdown.classList.toggle('show');
            userProfile.classList.toggle('active');
            
            console.log('Dropdown show class:', profileDropdown.classList.contains('show'));
            console.log('Profile active class:', userProfile.classList.contains('active'));
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!userProfile.contains(e.target)) {
                console.log('Clicking outside, closing dropdown...');
                profileDropdown.classList.remove('show');
                userProfile.classList.remove('active');
            }
        });
        
        // Close dropdown on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                console.log('Escape key pressed, closing dropdown...');
                profileDropdown.classList.remove('show');
                userProfile.classList.remove('active');
            }
        });
        
        // Add hover effect for dropdown items
        const dropdownItems = profileDropdown.querySelectorAll('.dropdown-item');
        dropdownItems.forEach(item => {
            item.addEventListener('mouseenter', function() {
                this.style.transform = 'translateX(5px)';
            });
            
            item.addEventListener('mouseleave', function() {
                this.style.transform = 'translateX(0)';
            });
        });
        
        console.log('Profile dropdown functionality setup complete!');
    } else {
        console.error('Profile dropdown elements not found!');
        console.log('Available elements with "userProfile" in ID:', document.querySelectorAll('[id*="userProfile"]'));
        console.log('Available elements with "profileDropdown" in ID:', document.querySelectorAll('[id*="profileDropdown"]'));
    }
    
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.style.backgroundColor = '#141414';
        } else {
            navbar.style.backgroundColor = 'transparent';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Search functionality
    const searchInput = document.querySelector('.search-box input');
    if (searchInput) {
        searchInput.addEventListener('focus', function() {
            this.parentElement.style.transform = 'scale(1.05)';
        });
        
        searchInput.addEventListener('blur', function() {
            this.parentElement.style.transform = 'scale(1)';
        });
        
        searchInput.addEventListener('input', function() {
            // Implement search functionality here
            console.log('Searching for:', this.value);
        });
    }
    
    // Card hover effects
    const contentCards = document.querySelectorAll('.content-card');
    
    contentCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.zIndex = '10';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.zIndex = '1';
        });
    });
    
    // Button interactions
    const playButtons = document.querySelectorAll('.btn-play, .btn-play-small');
    const addButtons = document.querySelectorAll('.btn-add');
    const likeButtons = document.querySelectorAll('.btn-like');
    
    playButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Add play animation
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
            
            // Implement play functionality
            console.log('Playing content...');
        });
    });
    
    addButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Toggle add to list
            if (this.classList.contains('added')) {
                this.classList.remove('added');
                this.innerHTML = '<i class="fas fa-plus"></i>';
                console.log('Removed from list');
            } else {
                this.classList.add('added');
                this.innerHTML = '<i class="fas fa-check"></i>';
                console.log('Added to list');
            }
        });
    });
    
    likeButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Toggle like
            if (this.classList.contains('liked')) {
                this.classList.remove('liked');
                this.innerHTML = '<i class="fas fa-thumbs-up"></i>';
                console.log('Unliked');
            } else {
                this.classList.add('liked');
                this.innerHTML = '<i class="fas fa-thumbs-up"></i>';
                this.style.color = '#e50914';
                console.log('Liked');
            }
        });
    });
    
    // Hero section parallax effect
    const hero = document.querySelector('.hero');
    if (hero) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            hero.style.transform = `translateY(${rate}px)`;
        });
    }
    
    // Smooth scrolling for navigation
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId && targetId !== '#') {
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Content slider auto-scroll (optional)
    const contentSliders = document.querySelectorAll('.content-slider');
    
    contentSliders.forEach(slider => {
        let isDown = false;
        let startX;
        let scrollLeft;
        
        slider.addEventListener('mousedown', (e) => {
            isDown = true;
            slider.style.cursor = 'grabbing';
            startX = e.pageX - slider.offsetLeft;
            scrollLeft = slider.scrollLeft;
        });
        
        slider.addEventListener('mouseleave', () => {
            isDown = false;
            slider.style.cursor = 'grab';
        });
        
        slider.addEventListener('mouseup', () => {
            isDown = false;
            slider.style.cursor = 'grab';
        });
        
        slider.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - slider.offsetLeft;
            const walk = (x - startX) * 2;
            slider.scrollLeft = scrollLeft - walk;
        });
    });
    
    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        switch(e.key) {
            case 'ArrowLeft':
                // Navigate left in content sliders
                const activeSlider = document.querySelector('.content-slider:hover');
                if (activeSlider) {
                    activeSlider.scrollBy({
                        left: -200,
                        behavior: 'smooth'
                    });
                }
                break;
            case 'ArrowRight':
                // Navigate right in content sliders
                const activeSliderRight = document.querySelector('.content-slider:hover');
                if (activeSliderRight) {
                    activeSliderRight.scrollBy({
                        left: 200,
                        behavior: 'smooth'
                    });
                }
                break;
            case 'Enter':
                // Play selected content
                const focusedCard = document.querySelector('.content-card:hover');
                if (focusedCard) {
                    const playButton = focusedCard.querySelector('.btn-play-small');
                    if (playButton) {
                        playButton.click();
                    }
                }
                break;
        }
    });
    
    // Loading animation
    window.addEventListener('load', function() {
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.5s ease-in';
        
        setTimeout(() => {
            document.body.style.opacity = '1';
        }, 100);
    });
    
    // Add some CSS for button states
    const style = document.createElement('style');
    style.textContent = `
        .btn-add.added {
            background-color: #e50914 !important;
            border-color: #e50914 !important;
        }
        
        .btn-like.liked {
            background-color: #e50914 !important;
            border-color: #e50914 !important;
        }
        
        .content-slider {
            cursor: grab;
        }
        
        .content-slider:active {
            cursor: grabbing;
        }
    `;
    document.head.appendChild(style);
    
    console.log('Netflix-style home page loaded successfully!');
}); 