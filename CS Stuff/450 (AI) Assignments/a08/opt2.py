"""
Utility function for opt-2 successor
"""

def opt2_successor(points, i, j):
    """
    Returns a list of points if points[i]-points[i+1] intersects with
    points[j]-points[j+1] at a unique point. Otherwise, None is returned.

    Note that the new set of points can have a larger length, i.e.,
    this function does not check for lengths.

    Note that if i is j, None is returned.
    """
    N = len(points)
    i = i % N
    j = j % N
    if i == j: return False

    print("*** NOT IMPLEMENTED ***")
    return None

