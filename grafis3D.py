import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definisi simbol
z, y = sp.symbols('z y')

st.title("Aplikasi Turunan Parsial dan Visualisasi 3D")

# Input fungsi
func_input = st.text_input("Masukkan fungsi f(z, y):", "z**2 + y**2")
point_z = st.number_input("Nilai z (misalnya 20):", value=20)
point_y = st.number_input("Nilai y (misalnya 5):", value=5)

try:
    f = sp.sympify(func_input)
    f_z = sp.diff(f, z)
    f_y = sp.diff(f, y)

    # Evaluasi
    f_val = f.subs({z: point_z, y: point_y})
    fz_val = f_z.subs({z: point_z, y: point_y})
    fy_val = f_y.subs({z: point_z, y: point_y})

    st.write(f"Turunan parsial terhadap z: {f_z}")
    st.write(f"Turunan parsial terhadap y: {f_y}")
    st.write(f"Nilai f({point_z}, {point_y}) = {f_val}")
    st.write(f"f_z({point_z}, {point_y}) = {fz_val}")
    st.write(f"f_y({point_z}, {point_y}) = {fy_val}")

    # Visualisasi
    z_vals = np.linspace(point_z - 10, point_z + 10, 50)
    y_vals = np.linspace(point_y - 10, point_y + 10, 50)
    Z, Y = np.meshgrid(z_vals, y_vals)
    f_lambda = sp.lambdify((z, y), f, 'numpy')
    F = f_lambda(Z, Y)

    # Bidang singgung
    tangent_plane = float(f_val) + float(fz_val)*(Z - point_z) + float(fy_val)*(Y - point_y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(Z, Y, F, alpha=0.5, cmap='viridis')
    ax.plot_surface(Z, Y, tangent_plane, alpha=0.6, color='red')
    ax.scatter(point_z, point_y, f_val, color='black', s=50)

    ax.set_xlabel("z")
    ax.set_ylabel("y")
    ax.set_zlabel("f(z, y)")

    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
