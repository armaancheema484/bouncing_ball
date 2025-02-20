import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in a Spinning Hexagon")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Hexagon properties
HEX_RADIUS = 200  # Radius of the hexagon
HEX_CENTER = (WIDTH // 2, HEIGHT // 2)  # Center of the hexagon
HEX_ROTATION_SPEED = 1  # Rotation speed in degrees per frame

# Ball properties
BALL_RADIUS = 10
BALL_POS = [HEX_CENTER[0], HEX_CENTER[1] - HEX_RADIUS + BALL_RADIUS]  # Start at top of hexagon
BALL_VEL = [0, 0]  # Initial velocity
GRAVITY = 0.2  # Gravity effect
FRICTION = 0.99  # Friction effect

# Function to calculate hexagon vertices
def calculate_hexagon_vertices(center, radius, rotation):
    vertices = []
    for i in range(6):
        angle_deg = 60 * i + rotation
        angle_rad = math.radians(angle_deg)
        x = center[0] + radius * math.cos(angle_rad)
        y = center[1] + radius * math.sin(angle_rad)
        vertices.append((x, y))
    return vertices

# Function to check if a point is inside a polygon
def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if y > min(y1, y2):
            if y <= max(y1, y2):
                if x <= max(x1, x2):
                    if y1 != y2:
                        xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if y1 == y2 or x <= xinters:
                        inside = not inside
    return inside

# Function to reflect velocity off a wall
def reflect_velocity(velocity, normal):
    dot = velocity[0] * normal[0] + velocity[1] * normal[1]
    reflection = [velocity[0] - 2 * dot * normal[0], velocity[1] - 2 * dot * normal[1]]
    return reflection

# Main loop
rotation = 0
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation
    rotation += HEX_ROTATION_SPEED
    if rotation >= 360:
        rotation -= 360

    # Calculate hexagon vertices
    hexagon = calculate_hexagon_vertices(HEX_CENTER, HEX_RADIUS, rotation)

    # Apply gravity
    BALL_VEL[1] += GRAVITY

    # Update ball position
    BALL_POS[0] += BALL_VEL[0]
    BALL_POS[1] += BALL_VEL[1]

    # Check for collisions with hexagon walls
    if not point_in_polygon(BALL_POS, hexagon):
        # Find the closest wall and reflect the ball's velocity
        closest_dist = float('inf')
        closest_normal = None
        for i in range(6):
            x1, y1 = hexagon[i]
            x2, y2 = hexagon[(i + 1) % 6]
            dx = x2 - x1
            dy = y2 - y1
            length = math.hypot(dx, dy)
            normal = (-dy / length, dx / length)  # Perpendicular to the wall
            # Calculate distance from ball to wall
            dist = abs((x2 - x1) * (y1 - BALL_POS[1]) - (x1 - BALL_POS[0]) * (y2 - y1)) / length
            if dist < closest_dist:
                closest_dist = dist
                closest_normal = normal
        # Reflect velocity
        BALL_VEL = reflect_velocity(BALL_VEL, closest_normal)
        # Move ball back inside the hexagon
        BALL_POS[0] += closest_normal[0] * (BALL_RADIUS - closest_dist)
        BALL_POS[1] += closest_normal[1] * (BALL_RADIUS - closest_dist)

    # Apply friction
    BALL_VEL[0] *= FRICTION
    BALL_VEL[1] *= FRICTION

    # Clear screen
    screen.fill(BLACK)

    # Draw hexagon
    pygame.draw.polygon(screen, WHITE, hexagon, 2)

    # Draw ball
    pygame.draw.circle(screen, RED, (int(BALL_POS[0]), int(BALL_POS[1])), BALL_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
