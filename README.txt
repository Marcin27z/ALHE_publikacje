1. Uruchomienie programu:
	Aby uruchmoniæ program, nale¿y wykonaæ skrypt "main.py".
	Algorytm nie ma odgórnie okreœlonej liczby iteracji.
	Aby przerwaæ i otrzymaæ wynik programu nale¿y wcisn¹æ ctrl+c.
	
2. Zmiana parametrów algorytmu:
	Plik "params.py" zawiera zestaw modyfikowalnych parametrów takich jak:
	- GENE_CROSS_PROBABILITY = 30	(prawdopodobieñstwo skrzy¿owania siê genów jako liczba z przedzia³u [0,99])
	- GENE_MUTATION_PROBABILITY = 1
	- NUMBER_OF_CHROMOSOMES = 50
	- GREEDY_SELECTION_SHARE_LIMIT = 5.5
	- MODE = Mode.PUNISHMENT  (mo¿e byæ Mode.PUNISHMENT lub Mode.REPAIR)
	- FILENAME = "input_data/filozofia-input.txt" (nazwa pliku z danymi wejœciowymi; plik musi zawieraæ now¹ liniê na koñcu pliku)