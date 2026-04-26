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
        # Browser-Müll beginnt IMMER mit dieser Zeile
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean.append(line)

    # Wenn Müll gefunden → Datei reparieren
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
        "app_title": "🎫 Revolution Ticket-System",
        "app_choose": "Wähle links: Kunden, Warteraum oder Sachbearbeiter.",

        "pull_title": "🎫 Nummer ziehen",
        "pull_info": "Bitte drücken Sie auf den Button, um Ihre Wartenummer zu erhalten.",
        "pull_button": "Nummer ziehen",
        "pull_wait": "Bitte warten Sie, bis Ihre Nummer aufgerufen wird.",
        "your_number": "Ihre Nummer",

        "waiting_room": "📢 Warteraum",
        "current_ticket": "Aktuelles Ticket",
        "queue_position": "Ihre Position in der Warteschlange:",
        "almost_called": "🎉 Sie sind gleich dran oder werden bereits aufgerufen!",
        "waiting_numbers": "Wartende Nummern",
        "no_more_tickets": "Keine weiteren Tickets.",
        "called_now": "🎉 Ihre Nummer wird jetzt aufgerufen!",

        "login_title": "🔐 Sachbearbeiter Login",
        "username": "Benutzername",
        "password": "Passwort",
        "login": "Login",
        "login_error": "Falscher Benutzername oder Passwort",

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

        # Navigation
        "nav_home": "Startseite",
        "nav_customers": "Kunden",
        "nav_waiting": "Warteraum",
        "nav_agent": "Sachbearbeiter",
        "logout": "Abmelden",
    },

    "en": {
        "app_title": "🎫 Revolution Ticket System",
        "app_choose": "Choose on the left: Customers, Waiting Room or Agent.",

        "pull_title": "🎫 Pull a Number",
        "pull_info": "Please press the button to receive your waiting number.",
        "pull_button": "Pull Number",
        "pull_wait": "Please wait until your number is called.",
        "your_number": "Your Number",

        "waiting_room": "📢 Waiting Room",
        "current_ticket": "Current Ticket",
        "queue_position": "Your position in the queue:",
        "almost_called": "🎉 You are next or already being called!",
        "waiting_numbers": "Waiting Numbers",
        "no_more_tickets": "No more tickets.",
        "called_now": "🎉 Your number is being called now!",

        "login_title": "🔐 Agent Login",
        "username": "Username",
        "password": "Password",
        "login": "Login",
        "login_error": "Incorrect username or password",

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

        # Navigation
        "nav_home": "Home",
        "nav_customers": "Customers",
        "nav_waiting": "Waiting Room",
        "nav_agent": "Agent",
        "logout": "Logout",
    },

    "fr": {
        "app_title": "🎫 Système de Tickets Révolutionnaire",
        "app_choose": "Choisissez à gauche : Clients, Salle d'attente ou Agent.",

        "pull_title": "🎫 Prendre un numéro",
        "pull_info": "Veuillez appuyer sur le bouton pour recevoir votre numéro d'attente.",
        "pull_button": "Prendre un numéro",
        "pull_wait": "Veuillez attendre que votre numéro soit appelé.",
        "your_number": "Votre numéro",

        "waiting_room": "📢 Salle d'attente",
        "current_ticket": "Ticket actuel",
        "queue_position": "Votre position dans la file :",
        "almost_called": "🎉 Vous êtes le prochain ou déjà appelé !",
        "waiting_numbers": "Numéros en attente",
        "no_more_tickets": "Plus aucun ticket.",
        "called_now": "🎉 Votre numéro est appelé maintenant !",

        "login_title": "🔐 Connexion Agent",
        "username": "Nom d'utilisateur",
        "password": "Mot de passe",
        "login": "Connexion",
        "login_error": "Nom d'utilisateur ou mot de passe incorrect",

        "agent_title": "🧑‍💼 Agent",
        "waiting_tickets": "Tickets en attente",
        "no_waiting": "Aucun ticket en attente.",
        "call_next": "➡️ Appeler le prochain ticket",
        "in_progress": "Actuellement en traitement",
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

        # Navigation
        "nav_home": "Accueil",
        "nav_customers": "Clients",
        "nav_waiting": "Salle d'attente",
        "nav_agent": "Agent",
        "logout": "Déconnexion",
    },

    "cn": {
        "app_title": "🎫 革命票务系统",
        "app_choose": "请选择：客户、候诊室或工作人员。",

        "pull_title": "🎫 取号",
        "pull_info": "请按下按钮获取您的排队号码。",
        "pull_button": "取号",
        "pull_wait": "请等待您的号码被叫到。",
        "your_number": "您的号码",

        "waiting_room": "📢 候诊室",
        "current_ticket": "当前号码",
        "queue_position": "您在队列中的位置：",
        "almost_called": "🎉 您马上就要被叫到！",
        "waiting_numbers": "等待中的号码",
        "no_more_tickets": "没有更多号码。",
        "called_now": "🎉 您的号码正在被叫到！",

        "login_title": "🔐 工作人员登录",
        "username": "用户名",
        "password": "密码",
        "login": "登录",
        "login_error": "用户名或密码错误",

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

        # Navigation
        "nav_home": "首页",
        "nav_customers": "客户",
        "nav_waiting": "候诊室",
        "nav_agent": "办理人员",
        "logout": "退出登录",
    }
}
