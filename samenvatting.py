import streamlit as st

def main():
    st.markdown("""
        <style>
            .main-title {
                color: #1bc6f6;
                font-size: 2.5em;
                text-align: center;
                margin-bottom: 0.2em;
                font-family: 'Segoe UI', sans-serif;
            }
            .subtitle {
                color: #fff;
                text-align: center;
                margin-bottom: 2em;
                font-size: 1.2em;
            }
            .samenvatting-box {
                background: #232a36;
                border-radius: 16px;
                padding: 32px 24px;
                box-shadow: 0 0 18px rgba(27,198,246,0.13);
                max-width: 600px;
                margin: 0 auto 2em auto;
            }
            .stTextArea textarea {
                background: #181c24;
                color: #1bc6f6;
                border-radius: 8px;
                font-size: 1.1em;
            }
            .stButton>button {
                background: #1bc6f6;
                color: #181c24;
                font-weight: bold;
                border-radius: 8px;
                font-size: 1.1em;
                padding: 0.5em 2em;
                margin-top: 1em;
            }
            .stButton>button:hover {
                background: #17b0dc;
                color: #fff;
            }
            .help-markdown {
                color: #b0eaff;
                font-size: 0.98em;
                margin-bottom: 1em;
                margin-top: -10px;
            }
            .help-markdown code {
                background: #181c24;
                color: #7fff00;
                border-radius: 4px;
                padding: 2px 6px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">Synthèse de cours</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Rédigez votre synthèse et ajoutez des détails dépliables si besoin.</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="samenvatting-box">', unsafe_allow_html=True)
        titre = st.text_input("Titre de la synthèse", "")
        st.markdown("""
        <div class="help-markdown">
        <b>Astuce mise en forme :</b><br>
        <code>*italique*</code> ou <code>_italique_</code> &nbsp;|&nbsp;
        <code>**gras**</code> ou <code>__gras__</code> &nbsp;|&nbsp;
        <code>&lt;span style="color:#ff5252"&gt;mot coloré&lt;/span&gt;</code>
        </div>
        """, unsafe_allow_html=True)
        synthese = st.text_area("Votre synthèse (partie visible)", height=120)
        detail = st.text_area("Détail (partie cachée, optionnelle)", height=100, help="Ce texte sera affiché en cliquant sur le bouton ci-dessous.")

        if st.button("Enregistrer la synthèse"):
            if synthese.strip():
                st.success("Synthèse enregistrée avec succès !")
            else:
                st.error("Veuillez écrire une synthèse avant d'enregistrer.")

        if synthese.strip():
            st.markdown("---")
            st.subheader(titre if titre else "Aperçu de la synthèse")
            st.markdown(synthese.replace('\n', '  \n'), unsafe_allow_html=True)
            if detail.strip():
                with st.expander("Développer les détails"):
                    st.markdown(detail.replace('\n', '  \n'), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()