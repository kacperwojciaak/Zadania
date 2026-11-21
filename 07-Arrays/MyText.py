# funkcja dzieli tekst po spacjach i zwraca liczbe slow
def word_count(text):
    words = text.split()
    return len(words)

# funkcja zwraca tablice slow posortowana od najdluzszego do najkrotszego
def longest_to_shortest(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

# funkcja zwraca tablice slow posortowana alfabetycznie
def alphabetical(text):
    words = text.split()
    return sorted(words, key=str.lower)