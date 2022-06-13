# ✨ ZELDA ✨
## PROGRAMOWANIE PROJEKT

Siema, siema

Zrobiliśmy zeldę i działa (mimo jednego poważnego błędu i kilku małych):
 - Kuba ("szef" grupy):  
 -- Zrobił implementację grafiki i skleił grę w całość. Pomagał pozostałym członkom zespołu rozwiązać problemy w kodzie.
 - Julia:  
 -- Zrobiła postać i wszelkie mechaniki związane z postacią, tzn. bomby, ekspolozje, miecz.
 - Gosia:
 -- Zrobiła przeciwników, zaprojektowała walki i wszelkie rzeczy związane z przeciwnikami.
 - Marcin:
 -- Zrobił poszczególne mapki i ogarnął kolizyjność z mapą oraz przejście między poziomami. Wszelkie elementy mapowe to jego sprawka. Dodatkowo, z rzeczy nieprogramistycznych, zrobił wszystkie grafiki, które są użyte w grze.
 
 
 Największe problemy, które napotkaliśmy:
 - Czasem niszczenie pocisku przeciwnika powoduje error, który wyłącza grę. Nie wiemy jak go naprawić. Chodzi o to, że czasem pociski nie wpisują się na listę, co powoduje problem przy usunięciu.
 - Zdarza się, że przeciwnicy, którzy strzelają, podczas ucieczki przechodzą przez ściany w dół. Jest to pozostałość po błędzie, który powodował, że podczas ucieczki przeciwnicy w ogóle ignorowali ściany.
 - Nie udało się zrobić strzelania prosto w gracza, dlatego przeciwnicy strzelają losowo w różne strony.
 - Dużym problemem było zrobienie przejścia między poziomami, ale ostatecznie skorzystaliśmy ze znalezionego rozwiązania i trochę je zmodyfikowaliśmy (link do kodu, z którego korzystamy: https://stackoverflow.com/questions/21573533/pygame-change-level-level-made-of-list).
 - Niestety przez powyższe problemy nie starczyło czasu na pełne zaprojektowanie walki z bossem, dlatego wygląda ona dosyć biednie, ale plan był taki, żeby poza strzelaniem boss również spawnował bomby na mapie i przywoływał pomocników.

