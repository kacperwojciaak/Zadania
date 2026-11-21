# importuje wlasny modul z pliku MyText.py
import MyText

# zapisuje tekst z polecenia w zmiennej
text = "Jedno jabłko dziennie trzyma lekarza z daleka"

# wyswietlam tekst oraz wyniki dzialania funkcji z modulu
print("Text:", text)
print("Number of words:", MyText.word_count(text))
print("Words from the longest:", ",".join(MyText.longest_to_shortest(text)))
print("Words ordered alphabetically:", ",".join(MyText.alphabetical(text)))