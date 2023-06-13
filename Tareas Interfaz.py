import sqlite3
import tkinter as tk
from tkinter import messagebox

# Función para crear la tabla de tareas si no existe
def crear_tabla():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarea TEXT NOT NULL,
            completada INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Función para agregar una tarea
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea:
        conn = sqlite3.connect('tareas.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO tareas (tarea) VALUES (?)', (tarea,))

        conn.commit()
        conn.close()
        messagebox.showinfo("Tarea agregada", "La tarea ha sido agregada exitosamente.")
        entry_tarea.delete(0, tk.END)
        mostrar_tareas()

# Función para mostrar todas las tareas
def mostrar_tareas():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()

    tarea_text.delete(1.0, tk.END)

    for tarea in tareas:
        tarea_id, tarea_texto, completada = tarea
        estado = 'Completada' if completada else 'Pendiente'
        tarea_text.insert(tk.END, f'Tarea {tarea_id}: {tarea_texto} ({estado})\n')

    conn.close()

# Función para marcar una tarea como completada
def completar_tarea():
    tarea_id = entry_tarea_id.get()
    if tarea_id:
        conn = sqlite3.connect('tareas.db')
        cursor = conn.cursor()

        cursor.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (tarea_id,))

        conn.commit()
        conn.close()
        messagebox.showinfo("Tarea completada", "La tarea ha sido marcada como completada.")
        entry_tarea_id.delete(0, tk.END)
        mostrar_tareas()

# Función para eliminar una tarea
def eliminar_tarea():
    tarea_id = entry_tarea_id.get()
    if tarea_id:
        conn = sqlite3.connect('tareas.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))

        conn.commit()
        conn.close()
        messagebox.showinfo("Tarea eliminada", "La tarea ha sido eliminada.")
        entry_tarea_id.delete(0, tk.END)
        mostrar_tareas()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Tareas")

# Crear la etiqueta y el campo de entrada para agregar una tarea
label_tarea = tk.Label(ventana, text="Nueva tarea:")
label_tarea.pack()
entry_tarea = tk.Entry(ventana)
entry_tarea.pack()
btn_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
btn_agregar.pack()

# Crear la etiqueta y el campo de entrada para completar o eliminar una tarea
label_tarea_id = tk.Label(ventana, text="ID de la tarea:")
label_tarea_id.pack()
entry_tarea_id = tk.Entry(ventana)
entry_tarea_id.pack()
btn_completar = tk.Button(ventana, text="Marcar como completada", command=completar_tarea)
btn_completar.pack()
btn_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
btn_eliminar.pack()

# Crear el área de texto para mostrar las tareas
tarea_text = tk.Text(ventana)
tarea_text.pack()

# Mostrar las tareas al iniciar la aplicación
crear_tabla()
mostrar_tareas()

# Ejecutar la aplicación
ventana.mainloop()
