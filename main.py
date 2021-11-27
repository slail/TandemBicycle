def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    """
    Write a function that returns the maximum possible total speed or the minimum possible total speed of all of the
    tandem bicycles being ridden based on an input parameter, fastest .If fastest = true your function should return the
    maximum possible total speed; otherwise it should return the minimum total speed.
    """
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArray(redShirtSpeeds)

    total = 0
    for idx in range(len(redShirtSpeeds)):
        riderOne = redShirtSpeeds[idx]
        riderTwo = blueShirtSpeeds[len(blueShirtSpeeds) - 1 - idx]
        total += max(riderOne, riderTwo)
    return total


def reverseArray(array):
    startIdx = 0
    endIdx = len(array) - 1
    while startIdx < endIdx:
        array[startIdx], array[endIdx] = array[endIdx], array[startIdx]
        startIdx += 1
        endIdx -= 1
