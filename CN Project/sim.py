import random
import time
import carla

def main():
    try:
        # Connect to the CARLA server
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)

        # Get the world
        world = client.get_world()

        # Get the blueprint library and spawn a car
        blueprint_library = world.get_blueprint_library()
        blueprint = blueprint_library.filter('vehicle.tesla.model3')[0]

        # Set a spawn point
        spawn_point = carla.Transform(carla.Location(x=200, y=30, z=0), carla.Rotation(roll=0, pitch=0, yaw=90))

        # Spawn the vehicle
        vehicle = world.spawn_actor(blueprint, spawn_point)

        # Disable autopilot
        vehicle.set_autopilot(False)

        # Create control object
        control = carla.VehicleControl()

        while True:
            # Get the car's current location
            current_location = vehicle.get_location()

            # Generate a random speed (throttle between 0 and 1) and steering angle (-1 to 1)
            control.throttle = random.uniform(0.2, 0.8)  # Moderate speed
            control.steer = random.uniform(-1.0, 1.0)    # Steering angle

            # Apply the control to the vehicle
            vehicle.apply_control(control)

            # Print the car's current location
            print(f"Location: {current_location}")

            # Wait for a second
            time.sleep(1.0)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Destroy the vehicle to clean up the simulation
        if vehicle:
            vehicle.destroy()
        print("Vehicle destroyed.")

if __name__ == "__main__":
    main()
