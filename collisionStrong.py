import hashlib
import string
import random
import time

def createHash():
    newStr = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(10))
    newStr = bytes(newStr, "utf-8")
    newMsg = hashlib.sha256()
    newMsg.update(newStr)
    newHash = newMsg.hexdigest()
    newHash = newHash[0:6]
    return newHash

if __name__ == "__main__":
    print("This may take a while..")
    avg = 0
    avgTrials = 0
    for i in range(100):
        # Start time
        startTime = time.time()

        # Dictionary to save
        Checked = dict()

        # Loop until we find a matching hash
        count = 0
        match = False
        newHash = 0
        while match == False:
            count = count+1
            # Create a new hash to compare to the given hash
            newStr = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for n in     range(10))
            newStr = bytes(newStr, "utf-8")
            newMsg = hashlib.sha256()
            newMsg.update(newStr)
            newHash = newMsg.hexdigest()
            newHash = newHash[0:6]
            # compare to hash with all hashes in Checked, but also make sure it's not the same msg
            if (newHash in Checked and Checked[newHash] != newStr):
                match = True
            else:
                Checked[newHash] = newStr

        # HAVEN'T TESTED BUT SHOULD WORK.  FIND A WAY TO PRINT THE VALUE

        endTime = time.time() - startTime
        print("")
        print("Found match with ", newHash)
        print("Time " + str(endTime))
        print("Count " + str(count))

    avgTrials = avgTrials + count
    avg = avg + endTime
    print("Average time: " + str(avg/3))
    print("Average trials: " + str(avgTrials/3))


