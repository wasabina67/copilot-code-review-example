def kuku():
    for i in range(1, 10):
        nums = []
        for j in range(1, 10):
            nums.append(f"{i*j}")
        print(" ".join(nums))


if __name__ == "__main__":
    kuku()
