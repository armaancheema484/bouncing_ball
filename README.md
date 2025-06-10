# Bouncing Balls in a Spinning Hexagon

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.x-green) ![GitHub](https://img.shields.io/badge/GitHub-Open%20Source-brightgreen)

A Python simulation of two balls (basketball and soccer ball) bouncing inside a spinning hexagon. The balls are affected by gravity and friction, with different physical properties for each ball type. Built using the `pygame` library.

---

## Demo

<div align="center">
[![Video](https://www.youtube.com/watch?v=jZo-7a75fYw)](https://www.youtube.com/watch?v=jZo-7a75fYw)
</div>

---

## Features
- **Spinning Hexagon**: The hexagon rotates at a constant speed.
- **Multiple Balls**: 
  - Basketball (orange, larger, more bouncy)
  - Soccer ball (white, smaller, less bouncy)
- **Realistic Physics**: Each ball has unique properties:
  - Gravity effect
  - Custom bounce coefficients
  - Friction
- **Collision Detection**: Advanced collision detection keeps balls within the hexagon.
- **Visual Labels**: Each ball is labeled ('B' for basketball, 'S' for soccer ball).
- **Interactive Visualization**: The simulation runs in a graphical window powered by `pygame`.

---

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/bouncing-ball-simulation.git
   cd bouncing-ball-simulation
   ```
2. **Install Pygame**
   ```bash
   pip install pygame
   ```

## Usage
1. Navigate to project directory
   ```bash
   cd bouncing_ball
   ```
2. Run the simulation
   ```bash
   python bouncing_ball.py
   ```

## How it works

### Key Components

1. Hexagon Rotation:
- The hexagon rotates around its center using a rotation angle that increments each frame.
- The vertices of the hexagon are recalculated based on the current rotation.

2. Ball Physics:
- Each ball has unique properties:
  - Basketball: radius=15, bounce=1.2
  - Soccer ball: radius=12, bounce=0.9
- Gravity affects both balls (constant: 0.2)
- Friction gradually reduces velocity (coefficient: 0.99)

3. Collision Detection:
- Advanced point-in-polygon algorithm checks ball positions
- Precise collision response with wall normals
- Balls are kept within hexagon boundaries
- Each ball's bounce coefficient affects its collision response

4. Rendering:
- The hexagon and balls are drawn using Pygame
- Each ball has a distinct color and label
- Smooth animation at 60 FPS

## Ball Properties

### Basketball
- Color: Orange
- Radius: 15 pixels
- Bounce coefficient: 1.2
- Label: 'B'

### Soccer Ball
- Color: White
- Radius: 12 pixels
- Bounce coefficient: 0.9
- Label: 'S'
