# StopLightSim.py
# Name:
# Date:
# Assignment:

import simpy
import random

# Global variable to track light state
greenLight = True
# Queue (cars waiting at red light)
car_queue = []

def stopLight(env):
    """Simulates a traffic light that cycles between green, yellow, and red."""
    global greenLight

    while True:
        print("Green at time", env.now)
        greenLight = True
    # let cars pass during green
        yield env.timeout(30)

        print("Yellow at time", env.now)
        yield env.timeout(2)

        print("Red at time", env.now)
        greenLight = False
        yield env.timeout(20)


def car(env, car_id):

    """Simulates a car arriving and waiting for the light."""
    
    print(f"Car", car_id, "arrived at", env.now)

    car_queue.append(car_id)


    # TODO: Make the car wait while the light is red
    while (not greenLight) or (len(car_queue) == 0) or (car_queue[0] != car_id):
        print("car", car_id, "waiting at", env.now)
        yield env.timeout(1)
    # Hint: use a loop and env.timeout(1)

    print("Car", car_id, "departed at", env.now)
    # remove from queue
    car_queue.pop(0) 

    # small delay between cars passing
    yield env.timeout(1)



def carArrival(env):
    """Creates cars at regular intervals."""
    
    car_id = 0

    while True:
        car_id += 1
        print("Creating Car", car_id)

        # TODO: Start a new car process
        env.process(car(env, car_id))

        yield env.timeout(random.randint(3,7))


def main():
    env = simpy.Environment()

    # Start processes
    env.process(stopLight(env))
    
    # TODO: Start the carArrival process
    env.process(carArrival(env))

    # Run simulation
    env.run(until=100)

    print("Simulation complete")


if __name__ == "__main__":
    main()
