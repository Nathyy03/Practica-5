import streamlit as st
from config.conexion import obtener_conexion

def mostrar_inventario():
    st.title("Inventario")
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inventario")
        st.dataframe(cursor.fetchall())
        conexion.close()
