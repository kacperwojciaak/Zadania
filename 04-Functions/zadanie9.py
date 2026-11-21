# definiuje funkcje ktora zamienia godziny i minuty na odpowiedni format czasu
def time_string(hours, minutes, time_format):
    # jezeli wybrano format 24 godzinny to dopisuje zera z przodu do dwoch cyfr
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'
    
    # jezeli wybrano format 12 godzinny to rozbijam na przed poludniem i po poludniu
    elif time_format == '12':
        # sprawdzam czy jest przed poludniem (od 0 do 11) czy po poludniu (od 12 do 23)
        if hours < 12:
            period = 'am'
        else:
            period = 'pm'
        
        # przeliczam godzine na zegar 12 godzinny
        if hours == 0:
            hour_12 = 12
        elif hours > 12:
            hour_12 = hours - 12
        else:
            hour_12 = hours
            
        # w formacie 12h godzina nie ma zera z przodu a minuty zawsze maja dwie cyfry
        return f'{hour_12}:{minutes:02d}{period}'

# sprawdzam wszystkie przypadki testowe z polecenia
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))