1. Uruchomienie programu:
	Aby uruchmoni� program, nale�y wykona� skrypt "main.py".
	Algorytm nie ma odg�rnie okre�lonej liczby iteracji.
	Aby przerwa� i otrzyma� wynik programu nale�y wcisn�� ctrl+c.
	
2. Zmiana parametr�w algorytmu:
	Plik "params.py" zawiera zestaw modyfikowalnych parametr�w takich jak:
	- GENE_CROSS_PROBABILITY = 30	(prawdopodobie�stwo skrzy�owania si� gen�w jako liczba z przedzia�u [0,99])
	- GENE_MUTATION_PROBABILITY = 1
	- NUMBER_OF_CHROMOSOMES = 50
	- GREEDY_SELECTION_SHARE_LIMIT = 5.5
	- MODE = Mode.PUNISHMENT  (mo�e by� Mode.PUNISHMENT lub Mode.REPAIR)
	- FILENAME = "input_data/filozofia-input.txt" (nazwa pliku z danymi wej�ciowymi; plik musi zawiera� now� lini� na ko�cu pliku)