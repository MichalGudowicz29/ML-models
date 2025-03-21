import numpy as np

class DecisionTreeRegressor:
    """Drzewo decyzyjne do regresji implementowane od podstaw"""
    
    def __init__(self, max_depth=5, min_samples_split=2):
        """
        Parametry:
        max_depth (int): Maksymalna głębokość drzewa
        min_samples_split (int): Minimalna liczba próbek do podziału węzła
        """
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None  # Tutaj przechowamy strukturę drzewa

    def _find_best_split(self, X, y):
        """Znajduje optymalny podział dla węzła (TODO: Zaimplementuj)"""
        # Zwracamy (indeks cechy, wartość podziału, MSE)
        return None, None, np.inf

    def _build_tree(self, X, y, depth=0):
        """Rekurencyjnie buduje drzewo (TODO: Zaimplementuj)"""
        # Warunki stopu:
        # - osiągnięto max_depth
        # - liczba próbek < min_samples_split
        # - brak możliwości podziału
        return None

    def fit(self, X, y):
        """Trenuje model na danych wejściowych"""
        self.tree = self._build_tree(X, y)
        return self

    def _predict_single(self, x, node):
        """Predykcja dla pojedynczej próbki (TODO: Zaimplementuj)"""
        return 0.0

    def predict(self, X):
        """Zwraca predykcje dla zestawu danych"""
        return np.array([self._predict_single(x, self.tree) for x in X])