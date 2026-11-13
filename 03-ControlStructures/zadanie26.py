# tekst z którego będziemy zliczać samogłoski
text = "This is a sample text to count vowels"

# definiuję samogłoski które chcę sprawdzać
vowels = "aeiouAEIOU"

# zeruję licznik samogłosek
vowels_count = 0

# ustawiam indeks początkowy na zero do pętli while
i = 0

# uruchamiam pętlę dopóki indeks mieści się w długości tekstu
while i < len(text):
    # wyciągam pojedynczy znak z tekstu pod aktualnym indeksem
    char = text[i]
    
    # sprawdzam czy ten znak znajduje się w naszej liście samogłosek
    if char in vowels:
        vowels_count += 1
        
    # zwiększam indeks o jeden żeby przejść do kolejnego znaku
    i += 1

# wyświetlam ostateczny wynik liczby samogłosek
print(f"Total number of vowels: {vowels_count}")