from abc import ABC, abstractmethod

class SimalarityStrategy:
    @abstractmethod
    def calculate_simalarity(self, image1, images):
        pass    