import socket
import time

# Server details
UDP_IP = "127.0.0.1"
UDP_PORT = 4242

import random

# Canvas size
width, height = 1000, 1000

# Initial snake and apple setup
snake = [(500, 500)]  # Starting position of the snake
apple = (random.randint(0, width), random.randint(0, height))  # Random apple position


def move_snake(snake, apple):
    head_x, head_y = snake[0]
    apple_x, apple_y = apple
    new_head = head_x, head_y

    # Move towards the apple: simplified logic for demonstration
    if head_x < apple_x:
        new_head = (head_x + 10, head_y)
    elif head_x > apple_x:
        new_head = (head_x - 10, head_y)
    elif head_y < apple_y:
        new_head = (head_x, head_y + 10)
    elif head_y > apple_y:
        new_head = (head_x, head_y - 10)

    # Insert new head and remove tail unless eating apple
    snake.insert(0, new_head)
    if new_head == apple:
        # Apple eaten, place a new apple
        apple = (random.randint(0, width), random.randint(0, height))
    else:
        snake.pop()  # Remove tail

    return snake, apple


# Generate messages for the snake game
def generate_messages(snake, apple):
    snake_message = "|".join([f"snake,{x},{y}" for x, y in snake])
    apple_message = f"apple,{apple[0]},{apple[1]}"
    return f"{snake_message}|{apple_message}".encode()


# Example usage
messages = []
for _ in range(100):  # Number of steps or until game over condition
    snake, apple = move_snake(snake, apple)
    message = generate_messages(snake, apple)
    messages.append(message)
    # Here you would send the message using the UDP script

# This is a conceptual representation. The actual implementation
# would depend on integrating with the UDP messaging system and handling game over conditions.


# Interval between each message
INTERVAL = 0.1

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

try:
    while True:
        for message in messages:
            print("Sending message:", message)
            sock.sendto(message, (UDP_IP, UDP_PORT))
            time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("Script interrupted by user. Exiting.")
finally:
    sock.close()