# laduje moj wlasny modul z miesiacami
import months

# pobieram numer miesiaca od uzytkownika
month_num = int(input('Enter month number: '))

# wywoluje funkcje z modulu i zapisuje nazwe miesiaca
month_name = months.month(month_num)

# wyswietlam gotowe zdanie na ekranie
print(f'The name of month {month_num} is {month_name}')