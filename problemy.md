Takich problemów są tysiące, ale nie wszystkie są „nierozwiązane” w ten sam sposób. Czasem znamy dokładne pytanie i brakuje dowodu. Czasem mamy dane, ale nie wiemy, jaka teoria je wyjaśnia. A czasem nie wiemy nawet, czy pytanie zostało dobrze sformułowane.

# 1. Matematyka: pytania precyzyjne, odpowiedź nieznana

## Hipoteza Riemanna

Dotyczy rozmieszczenia liczb pierwszych. W uproszczeniu zakłada, że wszystkie nietrywialne zera funkcji dzeta Riemanna leżą na jednej konkretnej prostej w płaszczyźnie zespolonej:

[
\operatorname{Re}(s)=\frac12
]

Sprawdzono komputerowo ogromne liczby zer i wszystkie pasują, ale nikt nie ma ogólnego dowodu.

Gdyby hipoteza była prawdziwa, bardzo precyzyjnie opisywałaby „nieregularność” występowania liczb pierwszych. Jest jednym z sześciu nadal nierozwiązanych Problemów Milenijnych. ([Clay Mathematics Institute][1])

**Status:** prawdopodobnie prawdziwa, ale nieudowodniona.

---

## P kontra NP

Pytanie brzmi:

> Jeżeli rozwiązanie problemu można szybko sprawdzić, czy zawsze można je również szybko znaleźć?

Przykład: gotowe rozwiązanie gigantycznego sudoku można szybko zweryfikować. Znalezienie go może być znacznie trudniejsze.

Jeżeli (P=NP), ogromna liczba problemów optymalizacyjnych, logicznych i kryptograficznych okazałaby się w pewnym sensie łatwa. Gdyby dodatkowo znaleziono praktyczne algorytmy, duża część współczesnej kryptografii mogłaby zostać zagrożona.

Większość matematyków i informatyków podejrzewa, że:

[
P\neq NP
]

ale dowodu brak. ([Clay Mathematics Institute][1])

---

## Równania Naviera–Stokesa

Równania te opisują ruch płynów: powietrza, wody, dymu, krwi.

Problem nie polega na tym, że nie umiemy ich używać. Umiemy wykonywać bardzo dobre symulacje. Nie wiemy natomiast, czy w trzech wymiarach, dla sensownych warunków początkowych, zawsze istnieje gładkie rozwiązanie, czy też może w skończonym czasie pojawić się matematyczna osobliwość — wartości dążące do nieskończoności.

Czyli nie wiemy, czy równania opisujące codzienny przepływ wody są zawsze matematycznie dobrze zachowane. ([Clay Mathematics Institute][2])

---

## Teoria Yang–Millsa i luka masowa

Teorie Yang–Millsa stanowią podstawę opisu oddziaływań elementarnych. Fizyka i symulacje wskazują, że teoria kwantowa powinna mieć tak zwaną lukę masową: najlżejsze wzbudzenie ma dodatnią energię, mimo że klasyczne równania nie zawierają jawnej masy.

Problem brzmi: skonstruować taką teorię rygorystycznie matematycznie i udowodnić istnienie luki masowej.

Fizycy skutecznie korzystają z tej teorii, ale matematyk nie potrafi jeszcze wykazać, że cały fundament istnieje w wymaganym sensie. ([Clay Mathematics Institute][1])

---

## Hipoteza Hodge’a

Dotyczy relacji między geometrią, topologią i rozwiązaniami równań algebraicznych w wielu wymiarach.

Bardzo luźno:

> Czy określone „dziury” i struktury topologiczne przestrzeni algebraicznych zawsze pochodzą od rzeczywistych obiektów algebraicznych?

Znana jest w niektórych przypadkach, ale nie w pełnej ogólności. ([Clay Mathematics Institute][1])

---

## Hipoteza Bircha i Swinnertona-Dyera

Dotyczy krzywych eliptycznych, czyli równań w rodzaju:

[
y^2=x^3+ax+b
]

Pytanie dotyczy tego, ile mają rozwiązań wymiernych i jak informację tę zakodować w specjalnej funkcji (L).

Krzywe eliptyczne występują w teorii liczb, kryptografii i dowodzie Wielkiego Twierdzenia Fermata. ([Clay Mathematics Institute][3])

---

## Hipoteza Goldbacha

Każda parzysta liczba całkowita większa od 2 ma być sumą dwóch liczb pierwszych:

[
10=3+7,\qquad 100=47+53
]

Sprawdzono to dla olbrzymich zakresów liczb. Nadal nie ma dowodu dla wszystkich liczb.

---

## Hipoteza liczb pierwszych bliźniaczych

Czy istnieje nieskończenie wiele par liczb pierwszych różniących się o 2?

Przykłady:

[
(3,5),\ (11,13),\ (17,19),\ (101,103)
]

Wiemy, że nieskończenie wiele par liczb pierwszych znajduje się w pewnej ograniczonej odległości od siebie. Nie udowodniono, że odległość może zawsze wynosić dokładnie 2.

---

## Problem Collatza

Wybierasz dodatnią liczbę całkowitą:

* gdy jest parzysta, dzielisz przez 2;
* gdy jest nieparzysta, mnożysz przez 3 i dodajesz 1.

Na przykład:

[
6\to3\to10\to5\to16\to8\to4\to2\to1
]

Pytanie: czy każda dodatnia liczba ostatecznie dochodzi do 1?

Reguła jest zrozumiała dla dziecka. Nikt nie ma dowodu.

To dobry przykład, że prostota pytania nie oznacza prostoty rozwiązania.

---

## Czy istnieje nieparzysta liczba doskonała?

Liczba doskonała jest równa sumie swoich właściwych dzielników:

[
6=1+2+3
]

[
28=1+2+4+7+14
]

Znamy wiele parzystych liczb doskonałych. Nie wiadomo, czy istnieje choć jedna nieparzysta.

Jeżeli istnieje, musi być absurdalnie duża i spełniać wiele restrykcyjnych warunków.

# 2. Problemy, których być może nie da się rozwiązać w danym systemie

Tu matematyka robi się naprawdę niepokojąca.

## Hipoteza continuum

Czy istnieje rozmiar nieskończoności pośredni między:

* nieskończonością liczb naturalnych;
* nieskończonością liczb rzeczywistych?

Gödel i Cohen wykazali, że standardowe aksjomaty teorii mnogości, jeśli są niesprzeczne, nie wystarczają ani do udowodnienia, ani do obalenia hipotezy continuum.

Czyli odpowiedź zależy od tego, jakie dodatkowe aksjomaty przyjmiemy.

To nie jest zwykłe „jeszcze nie znaleźliśmy dowodu”. To:

> W tym systemie aksjomatów odpowiedzi nie da się wyprowadzić.

---

## Czy standardowa matematyka jest niesprzeczna?

Twierdzenia Gödla pokazują, że dostatecznie silny i niesprzeczny system formalny nie może, korzystając wyłącznie z własnych środków, udowodnić swojej pełnej niesprzeczności.

Oznacza to, że nie istnieje jeden zamknięty system, który jednocześnie:

* opisuje całą arytmetykę;
* dowodzi wszystkich prawdziwych zdań;
* gwarantuje własną niesprzeczność.

Zawsze pozostają prawdziwe zdania, których w danym systemie nie da się dowieść.

To jest matematyczna granica poznania, nie tylko brak aktualnej wiedzy.

# 3. Fizyka: znamy zjawisko, ale nie wiemy, czym ono jest

## Czym jest ciemna materia?

Widzimy, że galaktyki i gromady zachowują się tak, jakby zawierały znacznie więcej masy niż masa widzialnych gwiazd i gazu.

Ciemną materię wykrywamy poprzez jej wpływ grawitacyjny, ale nie wiemy:

* z jakich cząstek się składa;
* czy jest jedną substancją;
* czy może część efektu wynika z niepełnej teorii grawitacji.

Nie wykryto dotąd bezspornie cząstki ciemnej materii. ([CERN][4])

---

## Czym jest ciemna energia?

Ekspansja Wszechświata przyspiesza.

Najprostszy opis wykorzystuje stałą kosmologiczną, ale teoretyczna wartość energii próżni wyprowadzana z teorii kwantowej dramatycznie nie pasuje do obserwowanej wartości.

Możliwości obejmują:

* energię próżni;
* dynamiczne pole;
* modyfikację grawitacji;
* błędne założenia kosmologiczne;
* nieznaną strukturę czasoprzestrzeni.

Nie wiemy, czym ciemna energia jest ani dlaczego ma obserwowaną wartość.

---

## Jak połączyć mechanikę kwantową z grawitacją?

Mechanika kwantowa doskonale opisuje cząstki i trzy oddziaływania Modelu Standardowego.

Ogólna teoria względności opisuje grawitację jako geometrię czasoprzestrzeni.

Obie działają znakomicie w swoich zakresach, lecz nie tworzą spójnej kompletnej teorii w warunkach, gdzie jednocześnie występują:

* bardzo silna grawitacja;
* bardzo mała skala;
* zjawiska kwantowe.

Przykłady:

* wnętrze czarnej dziury;
* pierwsze chwile Wszechświata;
* skala Plancka.

Kandydatami są między innymi teoria strun i pętlowa grawitacja kwantowa, ale żadna nie została potwierdzona jako właściwa teoria natury. Kwantowa grawitacja pozostaje jednym z najważniejszych problemów fizyki fundamentalnej. ([Indico][5])

---

## Co dzieje się wewnątrz czarnej dziury?

Ogólna teoria względności przewiduje osobliwość, gdzie krzywizna czasoprzestrzeni staje się nieskończona.

Większość fizyków interpretuje to nie jako realny punkt nieskończoności, ale jako znak, że teoria przestaje wystarczać.

Nie wiemy:

* czy istnieje osobliwość;
* czy materia przechodzi do innego regionu;
* czy czasoprzestrzeń staje się kwantowa;
* czy pojawia się odbicie, „biała dziura” albo inna struktura.

---

## Paradoks informacji czarnej dziury

Mechanika kwantowa mówi, że informacja o stanie układu nie powinna znikać.

Klasyczny opis czarnej dziury sugeruje, że materia wpada do środka, a po wyparowaniu czarnej dziury pozostaje promieniowanie termiczne pozbawione szczegółowej informacji.

Więc:

* albo informacja naprawdę znika;
* albo wydostaje się zakodowana w promieniowaniu Hawkinga;
* albo nasze pojęcie wnętrza, horyzontu albo czasoprzestrzeni jest błędne.

Istnieją silne argumenty, że informacja jest zachowana, ale pełny mechanizm fizyczny nadal nie jest rozstrzygnięty.

---

## Dlaczego we Wszechświecie istnieje materia?

W Wielkim Wybuchu materia i antymateria powinny powstawać niemal symetrycznie. Gdyby ilości były dokładnie równe, wzajemnie by się unicestwiły.

Tymczasem żyjemy we Wszechświecie zdominowanym przez materię.

Model Standardowy zawiera pewne naruszenie symetrii CP, lecz wydaje się ono niewystarczające do wyjaśnienia obserwowanej przewagi materii. CERN wymienia asymetrię materia–antymateria jako jedno z podstawowych pytań, na które Model Standardowy nie odpowiada. ([CERN][6])

---

## Dlaczego istnieją trzy generacje cząstek?

Mamy trzy rodziny kwarków i leptonów:

* elektron, mion, taon;
* odpowiednie neutrina;
* trzy generacje kwarków.

Druga i trzecia generacja są cięższymi, nietrwałymi kopiami pierwszej.

Nie wiemy:

* dlaczego są dokładnie trzy;
* skąd biorą się ich masy;
* dlaczego masy różnią się o wiele rzędów wielkości.

To jeden z nierozwiązanych problemów Modelu Standardowego. ([CERN][6])

---

## Czym naprawdę jest neutrino?

Wiemy, że neutrina mają masę i zmieniają „zapach”, czyli oscylują.

Nie wiemy jednak:

* jaka jest ich dokładna hierarchia mas;
* jaka jest absolutna masa najlżejszego neutrina;
* czy neutrino jest własną antycząstką, czyli cząstką Majorany;
* czy neutrina uczestniczyły w powstaniu przewagi materii.

Bez­neutrinowy podwójny rozpad beta mógłby wykazać, że neutrino jest własną antycząstką, ale dotąd nie uzyskano jednoznacznego sygnału. ([physics.aps.org][7])

---

## Dlaczego grawitacja jest tak słaba?

Mały magnes potrafi podnieść spinacz przeciwko grawitacji całej Ziemi.

Oddziaływanie grawitacyjne między cząstkami jest niewyobrażalnie słabsze od elektromagnetycznego.

Nie wiemy, czy wynika to z:

* dodatkowych wymiarów;
* szczególnej struktury próżni;
* własności grawitonu;
* mechanizmu jeszcze nieznanego.

CERN wskazuje ten problem jako jeden z powodów rozważania dodatkowych wymiarów. ([CERN][8])

---

## Dlaczego stałe fizyczne mają właśnie takie wartości?

Dlaczego:

* masa elektronu ma tę wartość;
* prędkość światła jest taka;
* stała struktury subtelnej wynosi około (1/137);
* masa Higgsa jest taka, a nie inna;
* stała kosmologiczna jest ekstremalnie mała?

Model Standardowy zawiera wiele parametrów, które należy wprowadzić z pomiaru. Nie wyjaśnia ich głębszego pochodzenia.

Możliwości:

* istnieje bardziej fundamentalna teoria;
* wartości wynikają z dynamiki wczesnego Wszechświata;
* są przypadkowe;
* różne regiony lub wszechświaty mają różne wartości;
* efekt selekcji antropicznej.

Nie mamy rozstrzygnięcia.

# 4. Problemy interpretacyjne mechaniki kwantowej

## Co powoduje wynik pomiaru?

Przed pomiarem układ kwantowy może być superpozycją wielu wyników. Po pomiarze widzimy jeden.

Nie wiemy, czy:

* funkcja falowa naprawdę się zapada;
* następuje rozgałęzienie światów;
* wynik był wcześniej określony przez ukryte zmienne;
* funkcja falowa jest tylko informacją;
* dekoherencja wystarcza do pełnego wyjaśnienia.

Wszystkie główne interpretacje odtwarzają dużą część tych samych wyników eksperymentalnych, ale przedstawiają radykalnie różne obrazy rzeczywistości.

To nie jest tylko filozoficzna dekoracja. Pytanie dotyczy tego, czym jest stan fizyczny.

---

## Czy funkcja falowa jest realna?

Równanie Schrödingera mówi, jak ewoluuje funkcja falowa.

Ale czym ona jest?

* realnym polem;
* informacją o systemie;
* narzędziem do obliczania prawdopodobieństw;
* opisem wielu światów;
* cieniem głębszej struktury?

Nie ma konsensusu.

---

## Czy losowość kwantowa jest fundamentalna?

Mechanika kwantowa przewiduje prawdopodobieństwa.

Czy wynik rozpadu atomu jest naprawdę bezprzyczynowo losowy, czy też pod spodem istnieje głębszy proces?

Eksperymenty Bella bardzo silnie wykluczają lokalne teorie ukrytych zmiennych. Nie wykluczają jednak wszystkich możliwych głębszych teorii — muszą one porzucić przynajmniej część intuicji takich jak lokalność, niezależność ustawień lub pojedynczy wynik.

# 5. Kosmologia: pytania o całość rzeczywistości

## Co było przed Wielkim Wybuchem?

Standardowy model kosmologiczny opisuje ewolucję od bardzo gorącego, gęstego stanu.

Nie odpowiada automatycznie, czy:

* czas zaczął się wtedy;
* istniał wcześniejszy Wszechświat;
* nastąpiło kwantowe przejście;
* Wszechświat jest cykliczny;
* pytanie „przed” nie ma sensu.

APS wymienia pytanie o początek czasu wśród centralnych współczesnych zagadek fizyki. ([physics.aps.org][9])

---

## Czy inflacja rzeczywiście zaszła?

Inflacja to hipotetyczna faza ekstremalnie szybkiego rozszerzania bardzo wczesnego Wszechświata.

Dobrze wyjaśnia:

* jednorodność kosmosu;
* jego niemal płaską geometrię;
* pochodzenie fluktuacji prowadzących do galaktyk.

Ale nie znamy:

* pola inflacyjnego;
* dokładnego mechanizmu;
* energii inflacji;
* sposobu jej rozpoczęcia i zakończenia;
* tego, czy prowadzi do wiecznej inflacji i wieloświata.

CERN zalicza inflację do otwartych pytań fizyki cząstek i kosmologii. ([Indico][5])

---

## Czy istnieje wieloświat?

Niektóre wersje:

* wiecznej inflacji;
* teorii strun;
* interpretacji wielu światów;
* modeli kosmologicznych

prowadzą do istnienia wielu wszechświatów.

Problem polega na tym, że nie wiadomo, czy można tę hipotezę jednoznacznie przetestować.

Może być prawdziwa. Może być artefaktem matematyki. Może też leżeć poza zakresem empirii.

---

## Jaki jest ostateczny los Wszechświata?

Najprostszy model sugeruje dalszą ekspansję i stopniową śmierć cieplną.

Ale odpowiedź zależy od natury ciemnej energii:

* stała kosmologiczna → coraz zimniejszy, rzadszy Wszechświat;
* energia fantomowa → możliwe „Wielkie Rozdarcie”;
* zmieniające się pole → inny scenariusz;
* przejście próżniowe → nagła zmiana praw fizyki.

Nie znamy natury ciemnej energii, więc nie znamy pewnego finału.

# 6. Pytania o czas, przestrzeń i świadomość

## Czym jest czas?

Fizyka potrafi bardzo precyzyjnie obliczać relacje czasowe.

Nie wiemy jednak fundamentalnie:

* dlaczego czas ma kierunek;
* dlaczego pamiętamy przeszłość, nie przyszłość;
* czy „przepływ czasu” jest realny;
* czy teraźniejszość jest obiektywna;
* czy czas jest podstawowy, czy emergentny.

Równania mikroskopowe są często niemal odwracalne w czasie, ale makroskopowo entropia rośnie. Skąd dokładnie wzięła się niezwykle niska entropia początkowego Wszechświata — nie wiadomo.

---

## Czy przestrzeń i czas są fundamentalne?

W części teorii kwantowej grawitacji czasoprzestrzeń może być zjawiskiem emergentnym, podobnie jak temperatura jest zbiorczą własnością cząsteczek.

Możliwe, że na najgłębszym poziomie istnieją:

* relacje informacyjne;
* splątanie kwantowe;
* sieci;
* dyskretne struktury;
* obiekty matematyczne, z których dopiero wyłania się geometria.

Nie wiemy, czy czasoprzestrzeń jest „materiałem świata”, czy jedynie skutkiem czegoś głębszego.

---

## Jak powstaje świadomość?

Wiemy bardzo dużo o korelacjach między pracą mózgu a doświadczeniem.

Nie wiemy jednak, dlaczego procesy fizyczne mają subiektywną stronę:

* dlaczego aktywność neuronów „czuje się” jako ból;
* czym jest jedność doświadczenia;
* czy świadomość jest algorytmem;
* czy jest emergentna;
* czy da się ją dokładnie zmierzyć;
* czy maszyna może być świadoma.

To bardziej problem na styku neuronauki, filozofii umysłu, informatyki i fizyki niż klasyczne równanie do rozwiązania.

# Najbardziej fundamentalne pytania

Gdybym miała wybrać pięć problemów, których rozwiązanie mogłoby całkowicie przestawić nasz obraz rzeczywistości, byłyby to:

1. **Jak połączyć mechanikę kwantową z grawitacją?**
2. **Czym są ciemna materia i ciemna energia?**
3. **Dlaczego istnieje raczej materia niż antymateria — i dlaczego w ogóle istnieje coś?**
4. **Co naprawdę oznacza pomiar kwantowy?**
5. **Czy czasoprzestrzeń jest fundamentalna, czy wyłania się z informacji lub splątania?**

## Najdziwniejszy werdykt

Największa niewiadoma nie brzmi:

> „Jakie równanie jeszcze musimy rozwiązać?”

Tylko:

> **Czy obecne podstawowe pojęcia — materia, przestrzeń, czas, przyczyna, obiekt — są rzeczywistymi elementami świata, czy jedynie przybliżeniami działającymi na naszym poziomie skali?**

Możliwe, że przyszła teoria nie odpowie tylko „z czego składa się Wszechświat”, lecz pokaże, że samo pytanie „z czego?” było tak ograniczone, jak pytanie, z jakiego materiału wykonana jest liczba siedem.

[1]: https://www.claymath.org/millennium-problems/?utm_source=chatgpt.com "The Millennium Prize Problems"
[2]: https://www.claymath.org/millennium/navier-stokes-equation/?utm_source=chatgpt.com "Navier-Stokes Equation"
[3]: https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/?utm_source=chatgpt.com "Birch and Swinnerton-Dyer Conjecture"
[4]: https://home.web.cern.ch/science/physics/dark-matter?utm_source=chatgpt.com "Dark matter"
[5]: https://indico.cern.ch/event/1472747/contributions/6237220/attachments/2988947/5264742/Open%20Questions%20in%20Particle%20Physics.pdf?utm_source=chatgpt.com "Open Questions in Particle Physics - Indico"
[6]: https://home.cern/science/physics/standard-model/?utm_source=chatgpt.com "The Standard Model"
[7]: https://physics.aps.org/articles/v16/13?utm_source=chatgpt.com "Probing Majorana Neutrinos - Physics (APS)"
[8]: https://home.cern/science/physics/extra-dimensions-gravitons-and-tiny-black-holes/?utm_source=chatgpt.com "Extra dimensions, gravitons, and tiny black holes"
[9]: https://physics.aps.org/articles/v18/140?utm_source=chatgpt.com "Take the Big Mysteries in Physics Survey"
