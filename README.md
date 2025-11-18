# CLI Pet
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)

A tiny command-line pet simulator written in Python. This was created as a first experiment with object-oriented programming (OOP).

## Features

* Name your virtual pet
* Simple OOP structure with a dedicated `Pet` class
* Play, feed, and give water to your pet
* ASCII art companion
* Basic status system: mood, hunger, thirst, and age

## How It Works

The project contains two files:

* **main.py** – Handles user interaction, menu logic, and the main loop.
* **pet.py** – Defines the `Pet` class and all behavior.

The pet has three changeable stats:

* **Mood** (0–100)
* **Hunger** (100–0)
* **Thirst** (100–0)

Interacting with the pet updates these values.

## Example

```
Name your pet: Biscuit
(\_/)
(•_•)
/>🍪
```

