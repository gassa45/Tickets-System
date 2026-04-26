import streamlit as st
import os
from languages import translations

# ---------------------------------------------------------
# Browser-Müll-Schutz
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
# Startseite / Über uns
# ---------------------------------------------------------
def show():
    lang = st.session_state.get("lang", "de")
    t = translations[lang]

    # ---------------------------------------------------------
    # CSS für Animationen + Layout
    # ---------------------------------------------------------
    st.markdown("""
        <style>
            /* Fade-in Animation */
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }

            .fade {
                animation: fadeIn 1.2s ease-out;
            }

            /* Hauptkarte */
            .about-card {
                background: linear-gradient(135deg, #1E90FF, #0066CC);
                padding: 50px;
                border-radius: 30px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.25);
                width: 85%;
                margin: auto;
                margin-top: 50px;
                text-align: center;
                color: white;
            }
            .about-title {
                font-size: 48px;
                font-weight: 800;
                margin-bottom: 20px;
            }
            .about-sub {
                font-size: 22px;
                margin-bottom: 40px;
                opacity: 0.95;
            }

            /* Sektionen */
            .about-section {
                background-color: white;
                color: #003A78;
                padding: 30px;
                border-radius: 20px;
                width: 85%;
                margin: 40px auto;
                box-shadow: 0 6px 20px rgba(0,0,0,0.15);
                font-size: 20px;
                line-height: 1.6;
            }
            .about-section h3 {
                color: #002B5B;
                font-weight: 700;
            }

            /* Kontaktbereich */
            .contact-box {
                background-color: #003A78;
                color: white;
                padding: 35px;
                border-radius: 20px;
                width: 85%;
                margin: 40px auto;
                text-align: center;
                box-shadow: 0 6px 20px rgba(0,0,0,0.25);
            }
            .contact-box h3 {
                font-size: 28px;
                margin-bottom: 15px;
            }
            .contact-box p {
                font-size: 20px;
                margin: 5px 0;
            }
        </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Hauptkarte mit Animation
    # ---------------------------------------------------------
    st.markdown(f"""
        <div class="about-card fade">
            <div class="about-title">Revolution Ticket-System</div>
            <div class="about-sub">
                Willkommen! Hier erfahren Sie, wer wir sind und was unser System besonders macht.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Über uns – Abschnitt
    # ---------------------------------------------------------
    st.markdown("""
        <div class="about-section fade">
            <h3>Über uns</h3>
            <p>
                Wir entwickeln moderne, digitale Lösungen für Warte- und Ticketsysteme.
                Unser Ziel ist es, Abläufe zu vereinfachen, Wartezeiten transparent zu machen
                und sowohl Kunden als auch Mitarbeitern ein angenehmes, effizientes Erlebnis zu bieten.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Mission – Abschnitt
    # ---------------------------------------------------------
    st.markdown("""
        <div class="about-section fade">
            <h3>Unsere Mission</h3>
            <p>
                Wir glauben an klare Prozesse, intuitive Bedienung und moderne Technologie.
                Das Revolution Ticket-System wurde entwickelt, um Organisationen jeder Größe
                eine einfache, zuverlässige und flexible Lösung zu bieten.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Vorteile – Abschnitt
    # ---------------------------------------------------------
    st.markdown("""
        <div class="about-section fade">
            <h3>Warum unser System?</h3>
            <ul>
                <li>✔ Intuitive Bedienung für Kunden und Mitarbeiter</li>
                <li>✔ Klare Struktur und moderne Benutzeroberfläche</li>
                <li>✔ Mehrsprachige Unterstützung</li>
                <li>✔ Echtzeit-Informationen über Wartezeiten</li>
                <li>✔ Flexibel anpassbar für jede Branche</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Kontaktbereich – Abschnitt
    # ---------------------------------------------------------
    st.markdown("""
        <div class="contact-box fade">
            <h3>Kontakt</h3>
            <p>📧 E-Mail: support@revolution-ticketsystem.com</p>
            <p>📞 Telefon: +49 123 456 789</p>
            <p>📍 Standort: Hessen, Deutschland</p>
        </div>
    """, unsafe_allow_html=True)
