import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls in a Spinning Hexagon")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)  # Basketball color
SOCCER_BALL = (255, 255, 255)  # Soccer ball color

# Hexagon properties
HEX_RADIUS = 200  # Radius of the hexagon
HEX_CENTER = (WIDTH // 2, HEIGHT // 2)  # Center of the hexagon
HEX_ROTATION_SPEED = 1  # Rotation speed in degrees per frame

# Ball properties
BASKETBALL_RADIUS = 15
SOCCER_BALL_RADIUS = 12
GRAVITY = 0.2  # Gravity effect
FRICTION = 0.99  # Friction effect

class Ball:
    def __init__(self, x, y, color, radius, bounce=1.0, label=''):
        self.pos = [x, y]
        self.vel = [0, 0]
        self.color = color
        self.radius = radius
        self.bounce = bounce  # Bounce coefficient (1.0 = normal bounce, >1.0 = more bouncy)
        self.label = label

    def update(self, hexagon):
        # Apply gravity
        self.vel[1] += GRAVITY

        # Update position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # Check for collisions with hexagon walls
        if not point_in_polygon(self.pos, hexagon):
            # Find the closest wall and reflect the ball's velocity
            closest_dist = float('inf')
            closest_normal = None
            closest_point = None
            
            for i in range(6):
                x1, y1 = hexagon[i]
                x2, y2 = hexagon[(i + 1) % 6]
                dx = x2 - x1
                dy = y2 - y1
                length = math.hypot(dx, dy)
                normal = (-dy / length, dx / length)  # Perpendicular to the wall
                
                # Calculate distance from ball to wall
                dist = abs((x2 - x1) * (y1 - self.pos[1]) - (x1 - self.pos[0]) * (y2 - y1)) / length
                
                if dist < closest_dist:
                    closest_dist = dist
                    closest_normal = normal
                    # Calculate the closest point on the wall
                    t = max(0, min(1, ((self.pos[0] - x1) * dx + (self.pos[1] - y1) * dy) / (dx * dx + dy * dy)))
                    closest_point = (x1 + t * dx, y1 + t * dy)

            if closest_normal and closest_point:
                # Move ball back inside the hexagon
                self.pos[0] = closest_point[0] + closest_normal[0] * self.radius
                self.pos[1] = closest_point[1] + closest_normal[1] * self.radius
                
                # Reflect velocity and apply bounce coefficient
                self.vel = reflect_velocity(self.vel, closest_normal)
                self.vel[0] *= self.bounce
                self.vel[1] *= self.bounce

        # Apply friction
        self.vel[0] *= FRICTION
        self.vel[1] *= FRICTION

    def draw(self, screen):
        # Draw the ball
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
        # Draw the label
        font = pygame.font.Font(None, self.radius * 2)  # Font size proportional to ball radius
        text = font.render(self.label, True, BLACK)
        text_rect = text.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        screen.blit(text, text_rect)

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

# Create balls
start_x = HEX_CENTER[0]
start_y = HEX_CENTER[1] - HEX_RADIUS + BASKETBALL_RADIUS  # Start at top of hexagon

balls = [
    Ball(start_x, start_y, ORANGE, BASKETBALL_RADIUS, bounce=1.2, label='B'),  # Basketball
    Ball(start_x, start_y, SOCCER_BALL, SOCCER_BALL_RADIUS, bounce=0.9, label='S')  # Soccer ball
]

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

    # Update and draw balls
    for ball in balls:
        ball.update(hexagon)

    # Clear screen
    screen.fill(BLACK)

    # Draw hexagon
    pygame.draw.polygon(screen, WHITE, hexagon, 2)

    # Draw balls
    for ball in balls:
        ball.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
