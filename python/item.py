from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abstractmethod
    def update_quality(self):
        pass

    def decrease_sell_in(self):
        self.sell_in -= 1

    def increase_quality(self):
        self.quality += 1

    def decrase_quality(self):
        self.quality -= 1

    def reset_quality(self):
        self.quality -= self.quality
