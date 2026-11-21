# funkcja zaslania srodkowe cyfry karty gwiazdkami
def hide(card_number):
    # biore dwie pierwsze cyfry doklejam dziesiec gwiazdek i cztery ostatnie cyfry
    return card_number[:2] + ('*' * 10) + card_number[-4:]