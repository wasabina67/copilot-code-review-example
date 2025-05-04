def kuku():
    for i in range(1, 10):
        print(" ".join([f"{i*j}" for j in range(1, 10)]))


if __name__ == "__main__":
    kuku()
