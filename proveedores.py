import streamlit as st
from config.conexion import obtener_conexion

def mostrar_proveedores():
    st.title("Proveedores")
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        st.dataframe(cursor.fetchall())
        conexion.close()
