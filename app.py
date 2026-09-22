import streamlit as st
import pandas as pd

# Text
st.title("Überschrift ganz groß")
st.header("Abschnittsüberschrift")
st.subheader("Unterüberschrift")
st.write("write() ist der Allrounder – nimmt fast alles entgegen.")
st.markdown("**Fett**, *kursiv* und `Code` per Markdown.")
st.caption("Kleiner grauer Hinweistext.")

# Code und Formeln
st.code("print('Hallo')", language="python")
#st.latex(r"e^5i\pi + 1 = 0")
st.latex(r"e^{\frac{i\pi}{2}} + 1 = 0")

# Statusmeldungen
st.success("Hat geklappt!")
st.info("Zur Information …")
st.warning("Achtung!")
st.error("Etwas ist schiefgelaufen.")

# Daten
df = pd.DataFrame({"Stadt": ["Berlin", "Hamburg"], "Einwohner": [3_600_000, 1_900_000]})
st.dataframe(df)          # interaktive, sortierbare Tabelle
st.table(df)              # statische Tabelle
st.metric("Umsatz", "12.400 €", "+8 %")

# Diagramme (Schnellvarianten)
st.line_chart(df.set_index("Stadt"))
st.bar_chart(df.set_index("Stadt"))

# Medien

st.header("Medien")
st.image("media/Bildschirmfoto.png")

st.audio("media/r1AlDosari.mp3")

st.video("media/001Welcome.mp4")
#
#st.image("/Users/MacBookPro2012/Library/CloudStorage/GoogleDrive-lessons.mathe@googlemail.com/Meine Ablage/Screenshouts/Bildschirmfoto 2026-09-18.png")
#st.audio("/Users/MacBookPro2012/Library/CloudStorage/GoogleDrive-lessons.mathe@googlemail.com/Meine Ablage/Screenshouts/r1AlDosari.mp3")
#st.video("/Users/MacBookPro2012/Library/CloudStorage/GoogleDrive-lessons.mathe@googlemail.com/Meine Ablage/Screenshouts/001Welcome.mp4")