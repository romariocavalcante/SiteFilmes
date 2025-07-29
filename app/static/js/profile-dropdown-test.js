// Profile Dropdown Test Script
console.log('Profile dropdown test script loaded');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, checking for profile elements...');
    
    // Find the profile elements
    const userProfile = document.getElementById('userProfile');
    const profileDropdown = document.getElementById('profileDropdown');
    
    console.log('User Profile Element:', userProfile);
    console.log('Profile Dropdown Element:', profileDropdown);
    
    if (userProfile && profileDropdown) {
        console.log('✅ Both elements found! Setting up dropdown...');
        
        // Add click event to user profile
        userProfile.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('🎯 Profile clicked!');
            
            // Toggle the dropdown
            profileDropdown.classList.toggle('show');
            userProfile.classList.toggle('active');
            
            console.log('Dropdown show class:', profileDropdown.classList.contains('show'));
            console.log('Profile active class:', userProfile.classList.contains('active'));
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!userProfile.contains(e.target)) {
                console.log('🔄 Clicking outside, closing dropdown...');
                profileDropdown.classList.remove('show');
                userProfile.classList.remove('active');
            }
        });
        
        // Test dropdown visibility
        console.log('Testing dropdown visibility...');
        profileDropdown.style.border = '2px solid red';
        profileDropdown.style.background = 'rgba(255, 0, 0, 0.3)';
        
        setTimeout(() => {
            console.log('Removing test styling...');
            profileDropdown.style.border = '';
            profileDropdown.style.background = '';
        }, 2000);
        
    } else {
        console.error('❌ Elements not found!');
        
        // List all elements with similar IDs
        const allElements = document.querySelectorAll('*');
        const profileElements = Array.from(allElements).filter(el => 
            el.id && (el.id.includes('profile') || el.id.includes('user'))
        );
        
        console.log('Elements with profile/user in ID:', profileElements);
        
        // Try alternative selectors
        const alternativeProfile = document.querySelector('.user-profile');
        const alternativeDropdown = document.querySelector('.profile-dropdown');
        
        console.log('Alternative selectors:');
        console.log('.user-profile:', alternativeProfile);
        console.log('.profile-dropdown:', alternativeDropdown);
    }
});

// Also run when window loads
window.addEventListener('load', function() {
    console.log('Window loaded, checking again...');
    
    const userProfile = document.getElementById('userProfile');
    const profileDropdown = document.getElementById('profileDropdown');
    
    if (userProfile && profileDropdown) {
        console.log('✅ Elements found on window load!');
    } else {
        console.log('❌ Elements still not found on window load');
    }
}); 