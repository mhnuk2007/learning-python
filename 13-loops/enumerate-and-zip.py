""" enumerate-and-zip.py """

def enumerate_example():
    names = ["Bill", "Katy", "Verne"]
    for index, name in enumerate(names):
        print(index, name)


def zip_example():
    names = ["Bill", "Katy", "Verne"]
    scores = [85, 92, 78]
    for name, score in zip(names, scores):
        print(name, "scored", score)


if __name__ == "__main__":
    enumerate_example()
    zip_example()