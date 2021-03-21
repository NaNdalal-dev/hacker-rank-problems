#evens_and_odds = lambda num: hex(num)[2:] if num % 2 else bin(num)[2:]
def evens_and_odds(n):
    return f"{n:x}" if n % 2 else f"{n:b}"
print(evens_and_odds(13))