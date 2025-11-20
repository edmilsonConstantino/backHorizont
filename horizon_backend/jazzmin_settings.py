# horizon_backend/jazzmin_settings.py

JAZZMIN_SETTINGS = {
    # === BRANDING ===
    "site_title": "Horizon Dashboard",
    "site_header": "Horizon Global Consulting",
    "site_brand": "HORIZON",
    "site_logo": None,  # Adicione o caminho se tiver logo: "images/logo.png"
    "login_logo": None,
    "login_logo_dark": None,
    
    # === WELCOME ===
    "welcome_sign": "Bem-vindo ao Painel Administrativo",
    "copyright": "© 2025 Horizon Global Consulting — Todos os direitos reservados",
    
    # === SEARCH ===
    "search_model": ["auth.User", "auth.Group", "mensagens.Mensagem"],
    
    # === USER MENU ===
    "user_avatar": None,
    
    # === TOP MENU ===
    "topmenu_links": [
        {"name": "Início", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Ver Site", "url": "/", "new_window": True},
        {"model": "auth.User"},
        {"app": "mensagens"},
    ],
    
    # === USERMENU ===
    "usermenu_links": [
        {"name": "Ver Site", "url": "/", "new_window": True},
        {"model": "auth.user"},
    ],
    
    # === SIDEBAR ===
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "mensagens"],
    
    # === ICONS ===
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "mensagens.Mensagem": "fas fa-envelope",
    },
    
    # === DEFAULT ICON PARENTS ===
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    # === RELATED MODAL ===
    "related_modal_active": False,
    
    # === CUSTOM CSS/JS ===
    "custom_css": "css/jazzmin_custom.css",
    "custom_js": None,
    
    # === SHOW UI BUILDER ===
    "show_ui_builder": False,
    
    # === CHANGEFORM TEMPLATES ===
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    
    # === LANGUAGE CHOOSER ===
    "language_chooser": False,
}

# === UI TWEAKS - IMPORTANTE: Esta variável estava faltando ===
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "cyborg",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}