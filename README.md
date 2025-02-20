# Bouncing Ball in a Spinning Hexagon

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.x-green) ![GitHub](https://img.shields.io/badge/GitHub-Open%20Source-brightgreen)

A Python simulation of a small red ball bouncing inside a spinning hexagon. The ball is affected by gravity and friction, and it bounces off the rotating walls realistically. Built using the `pygame` library.

---

## Demo

![Bouncing Ball Simulation Demo](./images/demo.gif)

---

## Features
- **Spinning Hexagon**: The hexagon rotates at a constant speed.
- **Realistic Physics**: The ball is affected by gravity and friction.
- **Collision Detection**: The ball bounces off the hexagon's walls realistically.
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
3. Run the simulation
   ```bash
   python bouncing_ball.py
   ```

## How it works

### Key Components

1. Hexagon Rotation:

- The hexagon rotates around its center using a rotation angle that increments each frame.
- The vertices of the hexagon are recalculated based on the current rotation.

2. Ball Physics:

- The ball is affected by gravity, which increases its vertical velocity over time.
- Friction gradually reduces the ball's velocity.

3. Collision Detection:

- The program checks if the ball is outside the hexagon using a point-in-polygon algorithm.
- If a collision is detected, the ball's velocity is reflected off the closest wall.

4. Rendering:

- The hexagon and ball are drawn on the screen using Pygame's drawing functions.
