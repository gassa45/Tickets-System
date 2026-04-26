# ---------------------------------------------------------
# Datei: languages.py
# Sprachsystem für das Revolution Ticket-System
# ---------------------------------------------------------

import os
import streamlit as st

# ---------------------------------------------------------
# AUTOMATISCHER BROWSER-MÜLL-SCHUTZ
# ---------------------------------------------------------
def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean = []
    for line in lines:
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean.append(line)

    if len(clean) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean)
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# TRANSLATIONS
# ---------------------------------------------------------

translations = {
    "de": {
        # Startseite
        "home_title": "Revolution Ticket-System",
        "home_sub": "Willkommen! Hier erfahren Sie, wer wir sind und was unser System besonders macht.",
        "about_title": "Über uns",
        "about_text": (
            "Wir entwickeln moderne, digitale Lösungen für Warte- und Ticketsysteme. "
            "Unser Ziel ist es, Abläufe zu vereinfachen, Wartezeiten transparent zu machen "
            "und sowohl Kunden als auch Mitarbeitern ein angenehmes, effizientes Erlebnis zu bieten."
        ),
        "mission_title": "Unsere Mission",
        "mission_text": (
            "Wir glauben an klare Prozesse, intuitive Bedienung und moderne Technologie. "
            "Das Revolution Ticket-System wurde entwickelt, um Organisationen jeder Größe "
            "eine einfache, zuverlässige und flexible Lösung zu bieten."
        ),
        "why_title": "Warum unser System?",
        "why_1": "✔ Intuitive Bedienung für Kunden und Mitarbeiter",
        "why_2": "✔ Klare Struktur und moderne Benutzeroberfläche",
        "why_3": "✔ Mehrsprachige Unterstützung",
        "why_4": "✔ Echtzeit-Informationen über Wartezeiten",
        "why_5": "✔ Flexibel anpassbar für jede Branche",
        "contact_title": "Kontakt",
        "contact_email": "📧 E-Mail: support@revolution-ticketsystem.com",
        "contact_phone": "📞 Telefon: +49 123 456 789",
        "contact_location": "📍 Standort: Hessen, Deutschland",

        # Navigation
        "nav_home": "Startseite",
        "nav_customers": "Kunden",
        "nav_waiting": "Warteraum",
        "nav_agent": "Sachbearbeiter",
        "logout": "Abmelden",

        # Kundenbereich
        "pull_title": "🎫 Nummer ziehen",
        "pull_info": "Bitte drücken Sie auf den Button, um Ihre Wartenummer zu erhalten.",
        "pull_button": "Nummer ziehen",
        "pull_wait": "Bitte warten Sie, bis Ihre Nummer aufgerufen wird.",
        "your_number": "Ihre Nummer",

        # Warteraum
        "waiting_room": "📢 Warteraum",
        "current_ticket": "Aktuelles Ticket",
        "queue_position": "Ihre Position in der Warteschlange:",
        "almost_called": "🎉 Sie sind gleich dran oder werden bereits aufgerufen!",
        "waiting_numbers": "Wartende Nummern",
        "no_more_tickets": "Keine weiteren Tickets.",
        "called_now": "🎉 Ihre Nummer wird jetzt aufgerufen!",

        # Login
        "login_title": "🔐 Sachbearbeiter Login",
        "username": "Benutzername",
        "password": "Passwort",
        "login": "Login",
        "login_error": "Falscher Benutzername oder Passwort",

        # Sachbearbeiter
        "agent_title": "🧑‍💼 Sachbearbeiter",
        "waiting_tickets": "Wartende Tickets",
        "no_waiting": "Keine wartenden Tickets.",
        "call_next": "➡️ Nächstes Ticket aufrufen",
        "in_progress": "Aktuell in Bearbeitung",
        "none_in_progress": "Kein Ticket in Bearbeitung.",
        "finish": "Fertig",
        "finished": "Ticket abgeschlossen.",
        "no_description": "Keine Beschreibung angegeben",
        "no_ticket_called": "Noch kein Ticket aufgerufen.",
        "ticket_called": "Ticket aufgerufen:",
        "ticket_finished": "Ticket abgeschlossen:",
        "no_ticket_in_progress": "Kein Ticket in Bearbeitung.",
        "finish_ticket": "✔️ Ticket abschließen",
        "description": "Kurzbeschreibung",
    },

    "en": {
        # Homepage
        "home_title": "Revolution Ticket System",
        "home_sub": "Welcome! Learn who we are and what makes our system special.",
        "about_title": "About Us",
        "about_text": (
            "We develop modern, digital solutions for queue and ticket systems. "
            "Our goal is to simplify processes, make waiting times transparent, "
            "and provide both customers and staff with an efficient and pleasant experience."
        ),
        "mission_title": "Our Mission",
        "mission_text": (
            "We believe in clear processes, intuitive usability, and modern technology. "
            "The Revolution Ticket System was created to offer organizations of any size "
            "a simple, reliable, and flexible solution."
        ),
        "why_title": "Why our system?",
        "why_1": "✔ Intuitive for customers and staff",
        "why_2": "✔ Clear structure and modern interface",
        "why_3": "✔ Multilingual support",
        "why_4": "✔ Real-time waiting information",
        "why_5": "✔ Flexible for any industry",
        "contact_title": "Contact",
        "contact_email": "📧 Email: support@revolution-ticketsystem.com",
        "contact_phone": "📞 Phone: +49 123 456 789",
        "contact_location": "📍 Location: Hesse, Germany",

        # Navigation
        "nav_home": "Home",
        "nav_customers": "Customers",
        "nav_waiting": "Waiting Room",
        "nav_agent": "Agent",
        "logout": "Logout",

        # Customers
        "pull_title": "🎫 Pull a Number",
        "pull_info": "Please press the button to receive your waiting number.",
        "pull_button": "Pull Number",
        "pull_wait": "Please wait until your number is called.",
        "your_number": "Your Number",

        # Waiting Room
        "waiting_room": "📢 Waiting Room",
        "current_ticket": "Current Ticket",
        "queue_position": "Your position in the queue:",
        "almost_called": "🎉 You are next or already being called!",
        "waiting_numbers": "Waiting Numbers",
        "no_more_tickets": "No more tickets.",
        "called_now": "🎉 Your number is being called now!",

        # Login
        "login_title": "🔐 Agent Login",
        "username": "Username",
        "password": "Password",
        "login": "Login",
        "login_error": "Incorrect username or password",

        # Agent
        "agent_title": "🧑‍💼 Agent",
        "waiting_tickets": "Waiting Tickets",
        "no_waiting": "No waiting tickets.",
        "call_next": "➡️ Call next ticket",
        "in_progress": "Currently in Progress",
        "none_in_progress": "No ticket in progress.",
        "finish": "Finish",
        "finished": "Ticket completed.",
        "no_description": "No description provided",
        "no_ticket_called": "No ticket has been called yet.",
        "ticket_called": "Ticket called:",
        "ticket_finished": "Ticket finished:",
        "no_ticket_in_progress": "No ticket in progress.",
        "finish_ticket": "✔️ Finish ticket",
        "description": "Description",
    },

    "fr": {
        # Page d'accueil
        "home_title": "Système de Tickets Révolutionnaire",
        "home_sub": "Bienvenue ! Découvrez qui nous sommes et ce qui rend notre système unique.",
        "about_title": "À propos de nous",
        "about_text": (
            "Nous développons des solutions modernes et numériques pour les systèmes de file d'attente. "
            "Notre objectif est de simplifier les processus, rendre les temps d'attente transparents "
            "et offrir une expérience agréable et efficace aux clients comme au personnel."
        ),
        "mission_title": "Notre mission",
        "mission_text": (
            "Nous croyons en des processus clairs, une utilisation intuitive et une technologie moderne. "
            "Le système de tickets Révolution a été conçu pour offrir une solution simple, fiable "
            "et flexible aux organisations de toute taille."
        ),
        "why_title": "Pourquoi notre système ?",
        "why_1": "✔ Utilisation intuitive pour clients et personnel",
        "why_2": "✔ Interface moderne et structure claire",
        "why_3": "✔ Support multilingue",
        "why_4": "✔ Informations en temps réel",
        "why_5": "✔ Flexible pour tous les secteurs",
        "contact_title": "Contact",
        "contact_email": "📧 Email : support@revolution-ticketsystem.com",
        "contact_phone": "📞 Téléphone : +49 123 456 789",
        "contact_location": "📍 Localisation : Hesse, Allemagne",

        # Navigation
        "nav_home": "Accueil",
        "nav_customers": "Clients",
        "nav_waiting": "Salle d'attente",
        "nav_agent": "Agent",
        "logout": "Déconnexion",

        # Clients
        "pull_title": "🎫 Prendre un numéro",
        "pull_info": "Veuillez appuyer sur le bouton pour recevoir votre numéro.",
        "pull_button": "Prendre un numéro",
        "pull_wait": "Veuillez attendre que votre numéro soit appelé.",
        "your_number": "Votre numéro",

        # Salle d'attente
        "waiting_room": "📢 Salle d'attente",
        "current_ticket": "Ticket actuel",
        "queue_position": "Votre position dans la file :",
        "almost_called": "🎉 Vous êtes le prochain ou déjà appelé !",
        "waiting_numbers": "Numéros en attente",
        "no_more_tickets": "Plus aucun ticket.",
        "called_now": "🎉 Votre numéro est appelé maintenant !",

        # Connexion
        "login_title": "🔐 Connexion Agent",
        "username": "Nom d'utilisateur",
        "password": "Mot de passe",
        "login": "Connexion",
        "login_error": "Nom d'utilisateur ou mot de passe incorrect",

        # Agent
        "agent_title": "🧑‍💼 Agent",
        "waiting_tickets": "Tickets en attente",
        "no_waiting": "Aucun ticket en attente.",
        "call_next": "➡️ Appeler le prochain ticket",
        "in_progress": "En traitement",
        "none_in_progress": "Aucun ticket en traitement.",
        "finish": "Terminer",
        "finished": "Ticket terminé.",
        "no_description": "Aucune description fournie",
        "no_ticket_called": "Aucun ticket n’a encore été appelé.",
        "ticket_called": "Ticket appelé :",
        "ticket_finished": "Ticket terminé :",
        "no_ticket_in_progress": "Aucun ticket en cours.",
        "finish_ticket": "✔️ Terminer le ticket",
        "description": "Description",
    },

    "cn": {
        # 首页
        "home_title": "革命票务系统",
        "home_sub": "欢迎！了解我们是谁，以及我们的系统为何与众不同。",
        "about_title": "关于我们",
        "about_text": (
            "我们开发现代化的数字排队与票务系统解决方案。"
            "我们的目标是简化流程，使等待时间透明化，"
            "并为客户和工作人员提供高效、舒适的体验。"
        ),
        "mission_title": "我们的使命",
        "mission_text": (
            "我们相信清晰的流程、直观的操作和现代技术。"
            "革命票务系统旨在为各种规模的组织提供简单、可靠、灵活的解决方案。"
        ),
        "why_title": "为什么选择我们的系统？",
        "why_1": "✔ 客户与工作人员都能轻松使用",
        "why_2": "✔ 清晰结构与现代界面",
        "why_3": "✔ 多语言支持",
        "why_4": "✔ 实时等待信息",
        "why_5": "✔ 适用于各行业的灵活方案",
        "contact_title": "联系方式",
        "contact_email": "📧 邮箱：support@revolution-ticketsystem.com",
        "contact_phone": "📞 电话：+49 123 456 789",
        "contact_location": "📍 地点：德国黑森州",

        # 导航
        "nav_home": "首页",
        "nav_customers": "客户",
        "nav_waiting": "候诊室",
        "nav_agent": "工作人员",
        "logout": "退出登录",

        # 客户区
        "pull_title": "🎫 取号",
        "pull_info": "请按下按钮获取您的排队号码。",
        "pull_button": "取号",
        "pull_wait": "请等待您的号码被叫到。",
        "your_number": "您的号码",

        # 候诊室
        "waiting_room": "📢 候诊室",
        "current_ticket": "当前号码",
        "queue_position": "您在队列中的位置：",
        "almost_called": "🎉 您马上就要被叫到！",
        "waiting_numbers": "等待中的号码",
        "no_more_tickets": "没有更多号码。",
        "called_now": "🎉 您的号码正在被叫到！",

        # 登录
        "login_title": "🔐 工作人员登录",
        "username": "用户名",
        "password": "密码",
        "login": "登录",
        "login_error": "用户名或密码错误",

        # 工作人员
        "agent_title": "🧑‍💼 工作人员",
        "waiting_tickets": "等待中的票号",
        "no_waiting": "没有等待中的票号。",
        "call_next": "➡️ 呼叫下一个号码",
        "in_progress": "正在处理",
        "none_in_progress": "没有正在处理的号码。",
        "finish": "完成",
        "finished": "号码已完成。",
        "no_description": "没有提供描述",
        "no_ticket_called": "尚未叫号。",
        "ticket_called": "已叫号：",
        "ticket_finished": "已完成：",
        "no_ticket_in_progress": "当前没有正在处理的号码。",
        "finish_ticket": "✔️ 完成号码",
        "description": "描述",
    }
}
