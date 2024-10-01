import random
import time

import carla

# Connect to the CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# Get the world
world = client.get_world()

# Spawn a car
blueprint = world.get_blueprint('vehicle.tesla.model3')
spawn_point = carla.Transform(carla.Location(x=200, y=30, z=0), carla.Rotation(roll=0, pitch=0, yaw=90))
vehicle = world.spawn_actor(blueprint, spawn_point)

# Set the car's autopilot to off
vehicle.set_autopilot(False)

while True:
    # Get the car's current location
    current_location = vehicle.get_location()

    # Generate a random speed and steering angle
    speed = random.uniform(5, 20)
    steering_angle = random.uniform(-30, 30)

    # Apply the speed and steering angle to the car
    vehicle.set_throttle(speed)
    vehicle.set_steer(steering_angle)

    # Print the car's current location
    print(current_location)

    # Wait for a second
    time.sleep(1.0)
