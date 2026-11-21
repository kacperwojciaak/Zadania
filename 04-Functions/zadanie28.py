# funkcja sprawdza czy podany tekst czytany od tylu brzmi tak samo
def f(palindrome):
    # odwracam napis i porownuje go z oryginalem
    return palindrome == palindrome[::-1]

# sprawdzam funkcje na przykladach z polecenia
print(f("radar"))
print(f("12-11-21"))
print(f("book"))