import streamlit as st



import os

st.set_page_config(page_title="Portafolio de Sostenibilidad", layout="wide")
st.title("Portafolio de Reflexión: Sostenibilidad")

tab1, tab2, tab3 = st.tabs(["Lo que veo", "Lo que ignoro", "Lo que eligo"])

with tab1:
    st.header("Lo que veo")
    st.write("Escenas cotidianas que se han normalizado, pero que reflejan la insostenibilidad del sistema actual. Escenas que he visto," \
    " pero a las que no les daba una reflexión produnda")
    col1, col2 = st.columns(2)

    with col1:
        st.image("gula2.jpg", caption="Sobre consumo de alimentos, innecesario y contaminante", width=500)
    with col2:
        st.image("supermercado.jpg", caption="Los supermercados generalmente contaminan más que las tiendas pequeñas y naturales," \
        " estas tiendas no necesariamente son más caras, animate!", width=500)

# --- TAB 2: Lo que ignoro ---
with tab2:
    st.header("Lo que ignoro")
    st.write("Impactos ocultos en las cadenas de producción: explotación, residuos tóxicos y daño ambiental." \
    " Situaciones que ignoraba, las cuales me parecían normales, desde la ignorancia.")
    col1, col2 = st.columns(2)

    with col1:
        st.image("fabrica.jpg", caption="Condiciones laborales en fábricas textiles", width=500)
    with col2:
        st.image("images.jpg", caption="Explotación labora, incluso infantil, desincentivar esto mediante un consumo responsable de" \
        " productos es necesario; hay que identificar que compañias venden estos productos, y sobre si vale la pena consentirlas al comprarles" \
        , width=500)

# --- TAB 3: Lo que elijo ---
with tab3:
    st.header("Lo que elijo")
    st.write("Iniciativas que muestran que otro camino es posible: colaboración, regeneración y sostenibilidad." \
    " Elijo esto para la posteridad, estas imagenes demuestran mi compromiso para mejorar.")
    col1, col2 = st.columns(2)

    with col1:
        st.image("caminar.jpg", caption="En vez de contaminar al subirse a un vehiculo, hay que considerar caminar, si las condiciones lo permiten claro", width=500)
    with col2:
        st.image("econologia.jpg", caption="la economía ecologica, la cual cumple c" \
        "on el triangulo de la sostenibilidad, cumplir en lo social, en lo económico, pero sin contaminar y mantener una casa común sana.", width=500)