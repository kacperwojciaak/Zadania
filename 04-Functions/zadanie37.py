# funkcja wstawia myslnik pomiedzy kazdy znak w podanym tekscie
def f(text):
    # lacze wszystkie znaki z tekstu uzywajac myslnika jako kleju
    return "-".join(text)

# sprawdzam funkcje na przykladach z polecenia
print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))