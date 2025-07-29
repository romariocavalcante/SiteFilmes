document.addEventListener("DOMContentLoaded", function() {
    // Elementos do DOM
    const form = document.querySelector('form');
    const inputs = document.querySelectorAll('input');
    const submitButton = document.querySelector('button[type="submit"]');
    const messages = document.querySelectorAll('.message');
    
    // Elementos das abas
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    const switchTabLinks = document.querySelectorAll('.switch-tab');
    
    // Inicializar funcionalidade das abas
    initializeTabs();
    
    // Animação de entrada dos elementos
    animateElements();
    
    // Efeitos nos inputs
    setupInputEffects();
    
    // Efeitos no botão
    setupButtonEffects();
    
    // Auto-hide das mensagens
    setupMessageAutoHide();
    
    // Efeitos de parallax no background
    setupParallaxEffect();
    
    // Função para inicializar as abas
    function initializeTabs() {
        tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                const targetTab = button.getAttribute('data-tab');
                switchTab(targetTab);
            });
        });
        
        switchTabLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetTab = link.getAttribute('data-tab');
                switchTab(targetTab);
            });
        });
    }
    
    // Função para trocar de aba
    function switchTab(targetTab) {
        // Remover classe active de todos os botões e conteúdos
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        
        // Adicionar classe active ao botão e conteúdo selecionado
        const activeButton = document.querySelector(`[data-tab="${targetTab}"]`);
        const activeContent = document.getElementById(`${targetTab}-tab`);
        
        if (activeButton && activeContent) {
            activeButton.classList.add('active');
            activeContent.classList.add('active');
            
            // Animar entrada do novo conteúdo
            animateTabContent(activeContent);
        }
    }
    
    // Função para animar entrada do conteúdo da aba
    function animateTabContent(content) {
        const elements = content.querySelectorAll('.form-section h1, .subtitle, .form-row, button, .footer-links, .terms-checkbox');
        
        elements.forEach((element, index) => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                element.style.transition = 'all 0.6s ease';
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }, 100 + (index * 100));
        });
    }
    
    // Função para animar elementos na entrada
    function animateElements() {
        const elements = document.querySelectorAll('.logo, .tagline, .tabs-navigation, .form-section h1, .subtitle, .form-row, button, .footer-links');
        
        elements.forEach((element, index) => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                element.style.transition = 'all 0.6s ease';
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }, 100 + (index * 100));
        });
    }
    
    // Função para configurar efeitos nos inputs
    function setupInputEffects() {
        inputs.forEach(input => {
            const wrapper = input.closest('.input-wrapper');
            const icon = wrapper ? wrapper.querySelector('i') : null;
            
            // Efeito de foco
            input.addEventListener('focus', () => {
                if (wrapper) wrapper.style.transform = 'scale(1.02)';
                if (icon) icon.style.transform = 'scale(1.1)';
            });
            
            input.addEventListener('blur', () => {
                if (wrapper) wrapper.style.transform = 'scale(1)';
                if (icon) icon.style.transform = 'scale(1)';
            });
            
            // Validação em tempo real
            input.addEventListener('input', () => {
                if (input.value.length > 0) {
                    input.classList.add('has-content');
                } else {
                    input.classList.remove('has-content');
                }
            });
            
            // Efeito de digitação
            input.addEventListener('keydown', (e) => {
                if (e.key !== 'Backspace' && e.key !== 'Delete') {
                    input.style.transform = 'scale(1.01)';
                    setTimeout(() => {
                        input.style.transform = 'scale(1)';
                    }, 100);
                }
            });
        });
    }
    
    // Função para configurar efeitos no botão
    function setupButtonEffects() {
        const submitButtons = document.querySelectorAll('button[type="submit"]');
        
        submitButtons.forEach(submitButton => {
            // Efeito de hover com partículas
            submitButton.addEventListener('mouseenter', () => {
                createParticles(submitButton);
            });
            
            // Efeito de loading no submit
            submitButton.addEventListener('click', (e) => {
                if (!submitButton.classList.contains('loading')) {
                    submitButton.classList.add('loading');
                    const span = submitButton.querySelector('span');
                    const icon = submitButton.querySelector('i');
                    
                    if (span) {
                        span.innerHTML = '<span class="loading-spinner"></span> Processando...';
                    }
                    
                    if (icon) {
                        icon.style.display = 'none';
                    }
                }
            });
        });
    }
    
    // Função para criar partículas
    function createParticles(element) {
        const rect = element.getBoundingClientRect();
        // Cores do tema Disney+/HBO Max
        const colors = ['#6c2bd9', '#8b5cf6', '#3b82f6', '#ffffff'];
        
        for (let i = 0; i < 8; i++) {
            const particle = document.createElement('div');
            particle.style.position = 'fixed';
            particle.style.width = '6px';
            particle.style.height = '6px';
            particle.style.background = colors[Math.floor(Math.random() * colors.length)];
            particle.style.borderRadius = '50%';
            particle.style.pointerEvents = 'none';
            particle.style.zIndex = '1000';
            particle.style.boxShadow = '0 0 10px rgba(108, 43, 217, 0.5)';
            
            const startX = rect.left + rect.width / 2;
            const startY = rect.top + rect.height / 2;
            
            particle.style.left = startX + 'px';
            particle.style.top = startY + 'px';
            
            document.body.appendChild(particle);
            
            const angle = (Math.PI * 2 * i) / 8;
            const velocity = 80 + Math.random() * 60;
            const endX = startX + Math.cos(angle) * velocity;
            const endY = startY + Math.sin(angle) * velocity;
            
            particle.animate([
                {
                    transform: 'translate(0, 0) scale(1)',
                    opacity: 1
                },
                {
                    transform: `translate(${endX - startX}px, ${endY - startY}px) scale(0)`,
                    opacity: 0
                }
            ], {
                duration: 1200,
                easing: 'cubic-bezier(0.4, 0, 0.2, 1)'
            }).onfinish = () => {
                particle.remove();
            };
        }
    }
    
    // Função para auto-hide das mensagens
    function setupMessageAutoHide() {
        messages.forEach(message => {
            // Adicionar animação de entrada
            message.style.animation = 'slideInRight 0.5s ease-out';
            
            setTimeout(() => {
                message.style.animation = 'slideOutRight 0.5s ease-out';
                setTimeout(() => {
                    message.style.display = 'none';
                }, 500);
            }, 4000);
        });
        
        // Auto-hide para mensagens do container de mensagens
        const messageContainer = document.querySelector('.messages-container');
        if (messageContainer) {
            const containerMessages = messageContainer.querySelectorAll('.message');
            containerMessages.forEach(message => {
                setTimeout(() => {
                    message.style.animation = 'slideOutRight 0.5s ease-out';
                    setTimeout(() => {
                        message.remove();
                    }, 500);
                }, 5000);
            });
        }
    }
    
    // Função para efeito parallax
    function setupParallaxEffect() {
        const main = document.querySelector('main');
        let ticking = false;
        
        function updateParallax() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            
            if (main) {
                main.style.transform = `translateY(${rate}px)`;
            }
            
            ticking = false;
        }
        
        function requestTick() {
            if (!ticking) {
                requestAnimationFrame(updateParallax);
                ticking = true;
            }
        }
        
        window.addEventListener('scroll', requestTick);
    }
    
    // Adicionar estilos CSS dinâmicos
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }
        
        .input-wrapper {
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .input-wrapper i {
            transition: transform 0.3s ease, color 0.3s ease;
        }
        
        input.has-content {
            border-color: #8b5cf6 !important;
        }
        
        input.has-content + i {
            color: #8b5cf6 !important;
        }
        
        input.error {
            border-color: #ef4444 !important;
            animation: shake 0.5s ease-in-out;
        }
        
        input.error + i {
            color: #ef4444 !important;
        }
        
        .logo i {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
        }
        
        .tab-btn {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .tab-content {
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .loading-spinner {
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: #ffffff;
            animation: spin 1s ease-in-out infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(style);
    
    // Efeito de digitação no tagline
    const tagline = document.querySelector('.tagline');
    if (tagline) {
        const originalText = tagline.textContent;
        tagline.textContent = '';
        
        let i = 0;
        const typeWriter = () => {
            if (i < originalText.length) {
                tagline.textContent += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        };
        
        setTimeout(typeWriter, 1000);
    }
    
    // Validação de senha no formulário de cadastro
    const regPassword = document.getElementById('reg-password');
    const regConfirmPassword = document.getElementById('reg-confirm-password');
    
    if (regPassword && regConfirmPassword) {
        function validatePasswords() {
            if (regPassword.value && regConfirmPassword.value) {
                if (regPassword.value !== regConfirmPassword.value) {
                    regConfirmPassword.classList.add('error');
                    regConfirmPassword.classList.remove('success');
                    regConfirmPassword.style.boxShadow = '0 0 0 4px rgba(239, 68, 68, 0.1)';
                } else {
                    regConfirmPassword.classList.remove('error');
                    regConfirmPassword.classList.add('success');
                    regConfirmPassword.style.boxShadow = '0 0 0 4px rgba(139, 92, 246, 0.1)';
                }
            } else {
                regConfirmPassword.classList.remove('error', 'success');
                regConfirmPassword.style.boxShadow = 'none';
            }
        }
        
        regPassword.addEventListener('input', validatePasswords);
        regConfirmPassword.addEventListener('input', validatePasswords);
    }
    
    // Validação de email
    const regEmail = document.getElementById('reg-email');
    if (regEmail) {
        regEmail.addEventListener('input', () => {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (regEmail.value && emailRegex.test(regEmail.value)) {
                regEmail.classList.add('success');
                regEmail.classList.remove('error');
            } else if (regEmail.value) {
                regEmail.classList.add('error');
                regEmail.classList.remove('success');
            } else {
                regEmail.classList.remove('error', 'success');
            }
        });
    }
    
    // Efeito de ripple nos botões
    function createRipple(event) {
        const button = event.currentTarget;
        const ripple = document.createElement('span');
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');
        
        button.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    }
    
    // Adicionar efeito ripple aos botões
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', createRipple);
    });
});