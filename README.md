- Gestor Táctico de Sustituciones (Estructuras de Datos Aplicadas)
- Descripción General
Esta aplicación de escritorio es un simulador de gestión táctica para partidos de fútbol. Permite al usuario actuar como el director técnico, administrando los jugadores que se encuentran en la zona de calentamiento, realizando sustituciones en el campo de juego y ofreciendo la posibilidad de revertir decisiones (simulando una intervención del VAR). El proyecto destaca por implementar estructuras de datos lineales desde cero, prescindiendo de las colecciones predeterminadas del lenguaje.

- Características Principales
Zona de Calentamiento (FIFO): Los jugadores ingresan a la zona de calentamiento y esperan su turno para entrar al campo, respetando estrictamente el orden de llegada.

Gestión de Sustituciones: Sistema intuitivo para seleccionar a un jugador activo en la cancha e intercambiarlo por el próximo jugador disponible en el banquillo.

Sistema de Reversión (VAR): Capacidad para deshacer la última sustitución realizada, restaurando la alineación exacta que estaba en el campo justo antes del cambio.

- Arquitectura y Estructuras de Datos
El núcleo de la aplicación fue desarrollado construyendo Nodos y referencias de memoria (Listas Enlazadas) para dar vida a las estructuras de datos fundamentales, todo bajo el paradigma de la Programación Orientada a Objetos:

Colas (Queues): Implementadas para gestionar la zona de calentamiento bajo el principio FIFO (First In, First Out). El primer jugador en empezar a calentar es el primero en ingresar a la cancha.

Pilas (Stacks): Utilizadas para el historial de sustituciones operando bajo el principio LIFO (Last In, First Out). El último cambio registrado es el primero en ser deshecho cuando se activa la función del VAR.

Interfaz Gráfica (GUI): Construida con la librería Tkinter de Python, utilizando componentes como Listbox para representar visualmente el estado de la cola y de la cancha en tiempo real.
