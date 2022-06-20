import time

# seconds passed since epoch


def gettime():
    seconds = 1545925769.9618232
    local_time = time.ctime(seconds)
    print("Local time:", local_time)

if __name__ == "__main__":
    gettime()
