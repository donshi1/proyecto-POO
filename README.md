Mafia de los Peluches: Apuestas de Alto Riesgo

Descripción del Proyecto
Este proyecto es una simulación de azar desarrollada en Python. El usuario asume el papel de un "Manager" que debe competir en lanzamientos de dados contra una jerarquía de peluches vivientes.

El objetivo es demostrar conceptos fundamentales de la Programación Orientada a Objetos (POO) en un contexto divertido y surrealista, alejándose de los ejemplos típicos de gestión de bancos o bibliotecas.

 Alcance del Proyecto
Qué hace: Simula enfrentamientos numéricos aleatorios entre un jugador humano y enemigos generados por código.
Público: Personas que buscan una resolución rápida de conflictos mediante el azar (similares a lanzar una moneda) pero con una narrativa de humor.
Límites: No cuenta con interfaz gráfica (funciona en consola) y no guarda persistencia de datos (partidas guardadas).

## 🔧 Diseño Técnico (UML)
El sistema utiliza **Herencia** para reutilizar la lógica de lanzamiento de dados.

```mermaid
classDiagram
    class manager {
        +nombre
        +color
        +lanzar()
    }
    class contrincante {
        +nombre
        +color
        +lanzar()
    }
    class jefe1 {
        +__init__()
    }
    class jefe2 {
        +__init__()
    }
    jefe1 --|> contrincante : Hereda
    jefe2 --|> contrincante : Hereda
