# 🎬 MovieFlix - Site de Filmes e Séries

## 📋 Visão Geral

O **MovieFlix** é uma plataforma completa de gerenciamento de catálogo de filmes e séries, desenvolvida com Django. O projeto inclui um sistema de autenticação moderno e um painel administrativo totalmente personalizado com recursos avançados de visualização e gerenciamento de dados.

## 🚀 Funcionalidades Principais

### 🎭 **Sistema de Autenticação**
- **Login/Registro**: Interface moderna inspirada no Disney+ e HBO Max
- **Logout**: Funcionalidade completa com redirecionamento automático
- **Sessões**: Gerenciamento seguro de sessões de usuário
- **Mensagens**: Sistema de feedback para o usuário

### 🎨 **Design da Interface de Login**
- **Gradientes modernos**: Inspirado no Disney+ e HBO Max
- **Glassmorphism**: Efeito de vidro fosco com backdrop-filter
- **Animações**: Efeitos de entrada, hover e interatividade
- **Responsividade**: Design adaptável para todos os dispositivos
- **Validação visual**: Feedback em tempo real para o usuário

### 🛠️ **Painel Administrativo Personalizado**

#### **Dashboard Interativo**
- **Estatísticas Visuais**: Cards coloridos com métricas em tempo real
- **Métricas de Qualidade**: Médias de classificação e conteúdo recente
- **Design Responsivo**: Interface adaptável para diferentes telas

#### **Filtros Avançados**
- **Data de Lançamento**: Últimos 30 dias, mês passado, este ano, etc.
- **Classificação**: Excelente (9.0+), Muito Bom (8.0-8.9), etc.
- **Duração**: Curto, Médio, Longo, Muito Longo
- **Gêneros**: Filtros por categoria de conteúdo

#### **Listas de Exibição Otimizadas**
- **Filmes**: Preview de imagem, duração formatada, classificação com estrelas
- **Séries**: Temporadas/episódios, classificação visual
- **Usuários**: Total de usuários criados, data de criação, último acesso
- **Gêneros**: Contadores de filmes e séries por categoria

#### **Ações em Lote**
- **Marcar como recente**: Atualiza datas de lançamento
- **Atualizar classificação**: Adiciona avaliações padrão
- **Exportar para CSV**: Exportação de dados
- **Duplicar registros**: Criação de cópias
- **Limpar dados antigos**: Remoção de conteúdo antigo

## 🎨 **Tema Cinematográfico**

### **Paleta de Cores**
- **Primária**: #1a1a2e (Azul escuro)
- **Secundária**: #16213e (Azul médio)
- **Destaque**: #e94560 (Vermelho vibrante)
- **Sucesso**: #00d4aa (Verde)
- **Aviso**: #ffa726 (Laranja)
- **Erro**: #ef5350 (Vermelho)

### **Gradientes**
- **Primário**: Linear-gradient(135deg, #667eea 0%, #764ba2 100%)
- **Secundário**: Linear-gradient(135deg, #f093fb 0%, #f5576c 100%)
- **Acento**: Linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)

### **Efeitos Visuais**
- **Animações**: Fade-in, pulse, hover effects
- **Sombras**: Múltiplas camadas de profundidade
- **Transições**: Movimentos fluidos em todos os elementos
- **Glassmorphism**: Efeitos de vidro fosco

## 📊 **Modelos de Dados**

### **LoginUsers**
- `usuario`: Nome do usuário
- `email`: Email único
- `senha`: Senha criptografada
- `data_criacao`: Data de criação automática
- `ultimo_acesso`: Último acesso automático

### **UsersAccount**
- `usuario`: Nome do usuário da conta
- `image`: Imagem de perfil
- `login_user`: Relacionamento com LoginUsers
- `data_criacao`: Data de criação

### **Filmes**
- `titulo`: Título do filme
- `descricao`: Sinopse
- `data_lancamento`: Data de lançamento
- `duracao`: Duração em minutos
- `genero`: Relacionamento ManyToMany com Gêneros
- `diretor`: Nome do diretor
- `elenco`: Lista do elenco
- `classificacao`: Avaliação (0-10)
- `imagem`: Poster do filme
- `linguagem`: Idioma principal
- `pais_de_origem`: País de origem

### **Series**
- `titulo`: Título da série
- `descricao`: Sinopse
- `data_lancamento`: Data de lançamento
- `n_temporadas`: Número de temporadas
- `n_episodios`: Número de episódios
- `genero`: Relacionamento ManyToMany com Gêneros
- `diretor`: Nome do diretor
- `elenco`: Lista do elenco
- `classificacao`: Avaliação (0-10)
- `imagem`: Poster da série
- `linguagem`: Idioma principal
- `pais_de_origem`: País de origem

### **Generos**
- `genero`: Nome do gênero

## 🛠️ **Arquivos Principais**

### **Backend**
- `app/models.py`: Modelos de dados
- `app/views.py`: Lógica de negócio
- `app/urls.py`: Roteamento de URLs
- `app/admin.py`: Configuração do admin personalizado
- `app/admin_actions.py`: Ações personalizadas do admin

### **Frontend**
- `app/templates/login.html`: Interface de login
- `app/templates/home.html`: Página principal
- `app/static/css/login/login.css`: Estilos do login
- `app/static/css/admin_custom.css`: Estilos do admin
- `app/static/js/login.js`: JavaScript do login

### **Templates Admin**
- `app/templates/admin/index.html`: Dashboard personalizado

## 🚀 **Como Usar**

### **Instalação**
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações: `python manage.py migrate`
4. Crie um superusuário: `python manage.py createsuperuser`
5. Execute o servidor: `python manage.py runserver`

### **Acesso**
- **Site Principal**: `http://localhost:8000/`
- **Login**: `http://localhost:8000/login/`
- **Admin**: `http://localhost:8000/admin/`

### **Funcionalidades**
1. **Login/Registro**: Interface moderna com animações
2. **Dashboard**: Visualize estatísticas do catálogo
3. **Gerenciamento**: Use filtros e ações em lote
4. **Exportação**: Exporte dados para análise

## 📱 **Responsividade**

### **Dispositivos Suportados**
- ✅ Desktop (1920px+)
- ✅ Laptop (1366px+)
- ✅ Tablet (768px+)
- ✅ Mobile (480px+)

### **Navegadores Compatíveis**
- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge

## 🎯 **Recursos Avançados**

### **Sistema de Filtros**
- Filtros por data, classificação, duração
- Filtros por gênero, país, idioma
- Filtros personalizados para séries (temporadas)

### **Ações em Lote**
- Seleção múltipla de registros
- Ações personalizadas
- Feedback visual das operações

### **Exportação de Dados**
- Formato CSV
- Dados estruturados
- Filtros aplicados na exportação

### **Estatísticas em Tempo Real**
- Contadores dinâmicos
- Métricas de qualidade
- Conteúdo recente

## 🔧 **Configuração Avançada**

### **Personalização de Cores**
Edite `app/static/css/admin_custom.css`:
```css
:root {
    --primary-color: #1a1a2e;
    --highlight-color: #e94560;
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### **Adicionar Novos Filtros**
Crie classes em `app/admin.py`:
```python
class CustomFilter(SimpleListFilter):
    title = 'Filtro Personalizado'
    parameter_name = 'custom_filter'
    
    def lookups(self, request, model_admin):
        return [('option', 'Opção')]
    
    def queryset(self, request, queryset):
        if self.value() == 'option':
            return queryset.filter(field='value')
```

### **Novas Ações em Lote**
Adicione em `app/admin_actions.py`:
```python
def nova_acao(modeladmin, request, queryset):
    # Lógica da ação
    modeladmin.message_user(request, "Ação executada!")
nova_acao.short_description = "Nova Ação"
```

## 📈 **Benefícios**

### **Para Administradores**
- **Produtividade**: Interface otimizada para gerenciamento eficiente
- **Visualização**: Dados organizados e fáceis de interpretar
- **Flexibilidade**: Filtros e ações para diferentes necessidades
- **Relatórios**: Exportação de dados para análise

### **Para Usuários**
- **Experiência**: Interface moderna e responsiva
- **Usabilidade**: Navegação intuitiva
- **Feedback**: Mensagens claras e informativas
- **Performance**: Carregamento rápido e otimizado

## 🔮 **Próximas Melhorias**

### **Funcionalidades Planejadas**
- [ ] Gráficos interativos no dashboard
- [ ] Sistema de notificações
- [ ] Relatórios automáticos
- [ ] Integração com APIs externas
- [ ] Sistema de backup automático
- [ ] Auditoria de mudanças
- [ ] Sistema de avaliações de usuários
- [ ] Recomendações personalizadas

### **Melhorias Técnicas**
- [ ] Cache Redis para performance
- [ ] API REST para integração
- [ ] Sistema de busca avançada
- [ ] Upload de imagens otimizado
- [ ] Testes automatizados

## 📄 **Licença**

Este projeto é desenvolvido para fins educacionais e de demonstração.

## 👨‍💻 **Desenvolvimento**

Desenvolvido com Django, HTML5, CSS3 e JavaScript, seguindo as melhores práticas de desenvolvimento web moderno.

---

**🎬 MovieFlix** - Transformando a gestão de catálogos de filmes e séries!
