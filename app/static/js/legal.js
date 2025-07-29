// JavaScript para páginas legais (Termos de Uso e Política de Privacidade)

document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scroll para links internos
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    internalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Animação de entrada das seções
    const sections = document.querySelectorAll('.legal-section');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const sectionObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        sectionObserver.observe(section);
    });
    
    // Efeito de hover nos links
    const links = document.querySelectorAll('.legal-section a');
    links.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Botão voltar com animação
    const backButton = document.querySelector('.btn-back');
    if (backButton) {
        backButton.addEventListener('mouseenter', function() {
            this.querySelector('i').style.transform = 'translateX(-3px)';
        });
        
        backButton.addEventListener('mouseleave', function() {
            this.querySelector('i').style.transform = 'translateX(0)';
        });
    }
    
    // Progress bar de leitura
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 3px;
        background: linear-gradient(90deg, #e50914, #ff6b6b);
        z-index: 1000;
        transition: width 0.3s ease;
    `;
    document.body.appendChild(progressBar);
    
    // Atualizar progress bar
    function updateProgressBar() {
        const scrollTop = window.pageYOffset;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        progressBar.style.width = scrollPercent + '%';
    }
    
    window.addEventListener('scroll', updateProgressBar);
    
    // Tooltip para informações de contato
    const contactInfo = document.querySelector('.contact-info');
    if (contactInfo) {
        const contactItems = contactInfo.querySelectorAll('p');
        contactItems.forEach(item => {
            item.addEventListener('mouseenter', function() {
                this.style.background = 'rgba(229, 9, 20, 0.1)';
                this.style.borderRadius = '8px';
                this.style.padding = '8px';
                this.style.transition = 'all 0.3s ease';
            });
            
            item.addEventListener('mouseleave', function() {
                this.style.background = 'transparent';
                this.style.padding = '0';
            });
        });
    }
    
    // Copiar informações de contato
    const contactTexts = document.querySelectorAll('.contact-info p');
    contactTexts.forEach(item => {
        item.style.cursor = 'pointer';
        item.title = 'Clique para copiar';
        
        item.addEventListener('click', function() {
            const text = this.textContent.replace(/^[^:]+:\s*/, ''); // Remove o label
            navigator.clipboard.writeText(text).then(() => {
                // Feedback visual
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check"></i> Copiado!';
                this.style.color = '#4CAF50';
                
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.style.color = '';
                }, 2000);
            });
        });
    });
    
    // Animações de entrada do header
    const header = document.querySelector('.legal-header');
    if (header) {
        header.style.opacity = '0';
        header.style.transform = 'translateY(-30px)';
        
        setTimeout(() => {
            header.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
            header.style.opacity = '1';
            header.style.transform = 'translateY(0)';
        }, 100);
    }
    
    // Efeito de digitação no título
    const title = document.querySelector('.legal-header h1');
    if (title) {
        const originalText = title.textContent;
        title.textContent = '';
        title.style.borderRight = '2px solid #e50914';
        
        let i = 0;
        const typeWriter = () => {
            if (i < originalText.length) {
                title.textContent += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            } else {
                title.style.borderRight = 'none';
            }
        };
        
        setTimeout(typeWriter, 500);
    }
    
    // Adicionar estilos CSS dinâmicos
    const style = document.createElement('style');
    style.textContent = `
        .reading-progress {
            box-shadow: 0 2px 10px rgba(229, 9, 20, 0.3);
        }
        
        .legal-section {
            position: relative;
        }
        
        .legal-section::before {
            content: '';
            position: absolute;
            left: -20px;
            top: 0;
            width: 3px;
            height: 0;
            background: linear-gradient(180deg, #e50914, #ff6b6b);
            transition: height 0.6s ease;
        }
        
        .legal-section.visible::before {
            height: 100%;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .contact-info p:hover {
            animation: pulse 0.3s ease;
        }
    `;
    document.head.appendChild(style);
    
    // Marcar seções como visíveis
    const markSectionVisible = (section) => {
        section.classList.add('visible');
    };
    
    const sectionVisibilityObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                markSectionVisible(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    sections.forEach(section => {
        sectionVisibilityObserver.observe(section);
    });
}); 