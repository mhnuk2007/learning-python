""" Loading the Dishwasher """

def load_dishwasher():
    sink = ['bowl', 'plate', 'cup']
    print(f"\nThere are {len(sink)} dishes in the sink: {sink}\n")

    while sink:
        dish = sink.pop()  # removes last item safely
        print(f" - Put a {dish} in the dishwasher")

    print(f"\nThere are {len(sink)} dishes in the sink: {sink}\n")


if __name__ == "__main__":
    load_dishwasher()