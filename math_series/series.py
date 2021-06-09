

def fibonacci(n):
   
    
    """
    This function takes in a number and returns a fibonacci value of it which is the sum of the fibonacci value of the two nambers before and it uses recursion.
    Arguments:
        n:int --- to know where exactly 
    Returns:
        returns a fibonacci value
    """
    if type(n) != int or n<0:
        return 'invalid intrence'
    if n==1:
        return 1
    if n==0:
        return 0
    return fibonacci(n-1)+fibonacci(n-2)




def lucas(n):


    """
    This function takes in a number and returns a lucas value of it which is the sum of the lucas value of the two nambers before and it uses recursion.
    Arguments:
        n:int --- to know where exactly 
    Returns:
        returns a lucas value
    """

    if type(n) != int or n<0:
        return 'invalid intrence'
    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1)+lucas(n-2)




def sum_series(n,first=0,second=1):
   
    """
    This function takes in a number and returns a fibonacci value of it which is the sum of the fibonacci value of the two nambers before and it uses recursion when two optional arguments are passed, it returns the lucas value.
    Arguments:
        n:int --- to know where exactly 
        first:int --- first number in serise
        second:int --- second number in serise
    Returns:
        returns a lucas value
    """
    if type(n) != int or n<0:
        return 'invalid intrence'
    if n==0:
        return first
    if n==1:
        return second
    return sum_series(n-1)+sum_series(n-2)