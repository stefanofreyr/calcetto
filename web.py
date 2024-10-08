import streamlit as st

st.title("⚽️ Calcetto")
st.subheader("Prenota il tuo campetto!")

cities = ("Agrigento", "Alessandria", "Ancona", "Aosta", "Arezzo")

city = st.selectbox(label="Città", options=cities, index=None, placeholder="Seleziona")

pitches = {
    "Agrigento": ["Bellavia", "Bernini", "Kokko"],
    "Alessandria": [],
    "Ancona": [],
    "Aosta": [],
    "Arezzo": []
}

if city:
    pitch = st.selectbox(label="Campo", options=pitches[city], index=None, placeholder="Seleziona")
    if pitch:
        date = st.date_input(label="Data", value=None)
        if date:
            search = st.button("Cerca orari disponibili", icon=":material/search:")

