""" circuit-breaker.py - Overloading a Circuit Breaker """

class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps  # maximum amps
        self.load = 0             # current load

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('Connection will exceed capacity.')
        elif self.load + amps < 0:
            raise Exception('Connection will cause negative load.')
        else:
            self.load += amps


if __name__ == "__main__":
    # Demo circuit
    cb = CircuitBreaker(20)
    print("Circuit capacity:", cb.capacity)
    print("Initial load:", cb.load)

    try:
        cb.connect(12)  # vacuum
        cb.connect(7)   # stereo
        cb.connect(10)  # dishwasher → exceeds
    except Exception as e:
        print("Error connecting device:", e)

    print("Current load:", cb.load)