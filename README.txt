1. Uruchomienie programu:
	Aby uruchmonić program, należy wykonać skrypt "main.py".
	Jego kolejne parametry to:
	- liczba wywołań przy założeniu, że punktem startowym jest stan, w którym żadna publikacja żadnego autora nie wchodzi w skład początkowego rozwiązania
	- liczba wywołań przy założeniu, że punktem startowym jest stan, w którym wszystkie publikacje każdego autora wchodzą w skład początkowego rozwiązania
	- liczba wywołań przy założeniu, że punktem startowym jest stan, w którym dla każdego autora wybrane są te jego publikacje, które zostały wybrane jako pierwsze k z listy posortowanej względem stosunku liczby punktów przynależnych autorowi podzielonych przez stopień współautorstwa
	- liczba wywołań przy założeniu, że punktem startowym jest stan, w którym dla każdego autora wybrane są te jego publikacje, które zostały wybrane jako pierwsze k z listy ustawionych losowo
	- ścieżka względna pliku wejściowego
	- ścieżka względna pliku wyjściowego
	
2. Zmiana parametrów algorytmu:
	Plik "params.py" zawiera zestaw modyfikowalnych parametrów takich jak:
	- GENE_CROSS_PROBABILITY = 30	(prawdopodobieństwo skrzyżowania się genów jako liczba z przedziału [0,100])
	- GENE_MUTATION_PROBABILITY = 1
	- NUMBER_OF_CHROMOSOMES = 50
	- GREEDY_SELECTION_SHARE_LIMIT = 5.5
	- MODE = Mode.PUNISHMENT  (może być Mode.PUNISHMENT lub Mode.REPAIR)