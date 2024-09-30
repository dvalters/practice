
def is_palindrome(palinput: str) -> bool:
    """
    Takes a string and tests whether it is a palindrome
    """
    reversed_str = palinput[::-1]
    return reversed_str == palinput