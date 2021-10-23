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
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - 1 - idx]
        total += max(rider1, rider2)
    return total


def reverseArray(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
