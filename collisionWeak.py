import hashlib
import string
import random
import time


def createHash():
    newStr = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)     for n in     range(10))
    newStr = bytes(newStr, "utf-8")
    newMsg = hashlib.sha256()
    newMsg.update(newStr)
    newHash = newMsg.hexdigest()
    newHash = newHash[0:5]
    return newHash

if __name__ == "__main__":
    print("This may take a while...")
    avg = 0
    avgTrials = 0
    for i in range(10):
        # Start time
        startTime = time.time()
        # Create the original message and corresponding hash
        givenHash = createHash()
        print("Looking for ", givenHash)
        # Loop until we find a matching hash
        count = 0
        match = False
        while match == False:
            count = count+1
            # Create a new hash to compare to the given hash
            newHash = createHash()
            # compare to hash with given hash
            if (givenHash == newHash):
                match = True
            #print(newHash)
        endTime = time.time() - startTime
        print("")
        print("Found match with " + givenHash)
        print("Time " + str(endTime))
        print("Count " + str(count))

    avgTrials = avgTrials + count
    avg = avg + endTime
    print("Average time: " + str(avg/3))
    print("Average trials: " + str(avgTrials/3))


