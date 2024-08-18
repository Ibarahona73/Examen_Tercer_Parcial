"""
Ivan Barahona
#201930010221

En este programa, se decidio utilizar los siguientes métodos y enfoques:

1. Interfaz gráfica con Tkinter:
   Se eligió Tkinter por ser una biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI) 
   de manera rápida y sencilla.

2. Conversión de números a palabras con num2words:
   Se utilizó la biblioteca num2words para convertir números a su representación en palabras. 
   Esta biblioteca ofrece soporte para múltiples idiomas, incluyendo el español,
   para instalar la biblioteca se debe ejecutar el siguiente comando en la terminal:
   pip install num2words.

3. Manejo de errores con try-except:
   Se implementó un manejo de errores para asegurar que el usuario ingrese un número entero válido, 
   mejorando así la robustez del programa.

4. Diseño de interfaz amigable:
   Se creó una interfaz con un diseño oscuro, etiquetas claras y un botón de acción destacado para mejorar 
   la experiencia del usuario.

5. Limitación de tamaño de ventana:
   Se estableció un tamaño fijo para la ventana (500x400 píxeles) y se deshabilitó la opción de redimensionar 
   para mantener una presentación consistente.

6. Uso de etiquetas para mostrar resultados:
   Se empleó una etiqueta (Label) para mostrar el resultado de la conversión, permitiendo una presentación clara 
   y legible del número convertido a palabras.
"""
#Limite de CienCuatrillones
import tkinter as tk
from tkinter import messagebox
from num2words import num2words

# Función para convertir el número a palabras
def convertir_numero():
    entrada = numero_entry.get()
    
    try:
        numero = int(entrada)
        palabras = num2words(numero, lang='es').upper()
        resultado_label.config(text=f"El número {numero} en palabras es:\n{palabras}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Conversor de Números a Palabras")
root.geometry("500x400+600+300")
root.resizable(False, False)
root.configure(bg="#2b2b2b")  # Fondo oscuro

icono_path = "math.ico"
root.iconbitmap(icono_path)

# Título del programa
titulo_label = tk.Label(root, text="Conversor de Números a Palabras", font=("Helvetica", 18, "bold"), fg="#ffcc00", bg="#2b2b2b")
titulo_label.pack(pady=20)

# Marco para contener la entrada y el botón
frame = tk.Frame(root, bg="#2b2b2b")
frame.pack(pady=10)

# Entrada para el número
numero_label = tk.Label(frame, text="Ingrese un número entero:", font=("Helvetica", 14), fg="#ffffff", bg="#2b2b2b")
numero_label.grid(row=0, column=0, padx=5)

numero_entry = tk.Entry(frame, font=("Helvetica", 14), justify='center', width=15)
numero_entry.grid(row=0, column=1, padx=5)

# Botón para convertir el número
convertir_button = tk.Button(root, text="Convertir", command=convertir_numero, font=("Helvetica", 14, "bold"), bg="#007acc", fg="white", relief="flat", width=12)
convertir_button.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#ffcc00", bg="#2b2b2b", wraplength=450, justify="center")
resultado_label.pack(pady=20)

# Ejecutar el loop principal de la interfaz
root.mainloop()

#Copyright 2024 Ivan Barahona