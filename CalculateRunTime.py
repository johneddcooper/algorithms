import time


def calculateRunTime(function, *args):
    """run a function and return the run time and the result of the
    function if the function requires arguments, those can be passed in too"""
    startTime = time.time()
    result = function(*args)
    return time.time() - startTime, result
