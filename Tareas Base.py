import sqlite3

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
def agregar_tarea(tarea):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO tareas (tarea) VALUES (?)', (tarea,))

    conn.commit()
    conn.close()

# Función para mostrar todas las tareas
def mostrar_tareas():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()

    for tarea in tareas:
        tarea_id, tarea_texto, completada = tarea
        estado = 'Completada' if completada else 'Pendiente'
        print(f'Tarea {tarea_id}: {tarea_texto} ({estado})')

    conn.close()

# Función para marcar una tarea como completada
def completar_tarea(tarea_id):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (tarea_id,))

    conn.commit()
    conn.close()

# Función para eliminar una tarea
def eliminar_tarea(tarea_id):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))

    conn.commit()
    conn.close()

# Función principal del programa
def main():
    crear_tabla()

    while True:
        print('\nSistema de Gestión de Tareas')
        print('1. Mostrar tareas')
        print('2. Agregar tarea')
        print('3. Marcar tarea como completada')
        print('4. Eliminar tarea')
        print('5. Salir')

        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            print('\nTAREAS:')
            mostrar_tareas()
        elif opcion == '2':
            tarea = input('Ingrese la tarea a agregar: ')
            agregar_tarea(tarea)
            print('Tarea agregada exitosamente.')
        elif opcion == '3':
            tarea_id = input('Ingrese el ID de la tarea a marcar como completada: ')
            completar_tarea(tarea_id)
            print('Tarea marcada como completada.')
        elif opcion == '4':
            tarea_id = input('Ingrese el ID de la tarea a eliminar: ')
            eliminar_tarea(tarea_id)
            print('Tarea eliminada.')
        elif opcion == '5':
            break
        else:
            print('Opción inválida. Por favor, intente nuevamente.')

if __name__ == '__main__':
    main()
