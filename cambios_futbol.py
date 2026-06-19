import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def desapilar(self):
        if self.tope is None:
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        return self.tope is None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.frente is None:
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def esta_vacia(self):
        return self.frente is None

class GestorCambiosFutbol:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Táctica - Cambios y VAR")
        self.root.geometry("500x550")
        
        self.pila_historial = Pila()
        self.cola_banquillo = Cola()
        self.jugadores_cancha = ["Portero", "Defensa Izq", "Defensa Der", "Medio", "Delantero"]
        
        tk.Label(root, text="Jugadores en el Campo (Selecciona uno para sacar):").pack(pady=5)
        self.listbox_cancha = tk.Listbox(root, height=5, selectmode=tk.SINGLE)
        self.listbox_cancha.pack(fill=tk.X, padx=20)
        
        tk.Label(root, text="Añadir jugador a la zona de calentamiento (Cola):").pack(pady=5)
        self.entry_calentamiento = tk.Entry(root)
        self.entry_calentamiento.pack(fill=tk.X, padx=20)
        
        tk.Button(root, text="Añadir a Calentamiento", command=self.añadir_calentamiento).pack(pady=5)
        
        tk.Label(root, text="Zona de Calentamiento:").pack(pady=5)
        self.listbox_cola = tk.Listbox(root, height=4)
        self.listbox_cola.pack(fill=tk.X, padx=20)
        
        tk.Button(root, text=" Realizar Sustitución", command=self.realizar_cambio, bg="#bae6fd").pack(pady=10)
        tk.Button(root, text=" VAR: Deshacer Último Cambio", command=self.deshacer_cambio, bg="#fecaca").pack(pady=5)
        
        self.actualizar_pantalla()

    def añadir_calentamiento(self):
        jugador = self.entry_calentamiento.get()
        if jugador.strip():
            self.cola_banquillo.encolar(jugador)
            self.entry_calentamiento.delete(0, tk.END)
            self.actualizar_pantalla()

    def realizar_cambio(self):
        seleccion = self.listbox_cancha.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un jugador en el campo para sustituir.")
            return
        
        if self.cola_banquillo.esta_vacia():
            messagebox.showwarning("Atención", "No hay jugadores calentando.")
            return

        indice_sale = seleccion[0]
        jugador_sale = self.jugadores_cancha[indice_sale]
        jugador_entra = self.cola_banquillo.desencolar()
        
        self.pila_historial.apilar((indice_sale, jugador_sale, jugador_entra))
        
        self.jugadores_cancha[indice_sale] = jugador_entra
        self.actualizar_pantalla()

    def deshacer_cambio(self):
        if self.pila_historial.esta_vacia():
            messagebox.showwarning("Atención", "No hay cambios registrados en el historial.")
            return
        
        indice, salio, entro = self.pila_historial.desapilar()
        
        self.jugadores_cancha[indice] = salio
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.listbox_cancha.delete(0, tk.END)
        for jugador in self.jugadores_cancha:
            self.listbox_cancha.insert(tk.END, jugador)
        
        self.listbox_cola.delete(0, tk.END)
        actual = self.cola_banquillo.frente
        while actual:
            self.listbox_cola.insert(tk.END, actual.dato)
            actual = actual.siguiente

if __name__ == "__main__":
    ventana = tk.Tk()
    app = GestorCambiosFutbol(ventana)
    ventana.mainloop()