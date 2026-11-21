# importuje moj wlasny modul converters z tego samego folderu
import converters

# testuje wszystkie funkcje z modulu podajac nazwe modulu przed kropka
print('Three meters is', converters.m_to_cm(3), 'cm')
print('250 cm is', converters.cm_to_m(250), 'm')
print('50 cm is', round(converters.cm_to_inches(50), 2), 'inches')
print('6 feet 2 inches is', converters.feet_inches_to_cm(6, 2), 'cm')