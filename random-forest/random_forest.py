import numpy as np
from .decision_tree import DecisionTreeRegressor  # Zakładając, że drzewo jest w tym samym pakiecie

class RandomForestRegressor:
    """Las losowy do regresji implementowany od podstaw"""
    
    def __init__(self, n_estimators=10, max_depth=5, max_features=None):
        """
        Parametry:
        n_estimators (int): Liczba drzew w lesie
        max_depth (int): Maksymalna głębokość pojedynczego drzewa
        max_features (int): Liczba cech do losowego wyboru
        """
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.max_features = max_features
        self.trees = []

    def _bootstrap_sample(self, X, y):
        """Generuje próbkę bootstrapową (TODO: Zaimplementuj)"""
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, n_samples, replace=True)
        return X[indices], y[indices]

    def fit(self, X, y):
        """Trenuje las losowy"""
        self.trees = []
        for _ in range(self.n_estimators):
            # 1. Stwórz próbkę bootstrapową
            # 2. Trenuj drzewo z losowym podzbiorem cech
            # 3. Dodaj do listy drzew
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            self.trees.append(tree)
        return self

    def predict(self, X):
        """Zwraca średnią predykcję wszystkich drzew"""
        predictions = np.array([tree.predict(X) for tree in self.trees])
        return np.mean(predictions, axis=0)