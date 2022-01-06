from item import Item


class Pepe(Item):
    NAME = 'Pepe'
    QUALITY_FACTOR = 0
    SELL_IN_FACTOR = 0

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        self.decrase_quality()
        self.decrease_sell_in()

        if self.sell_in < self.SELL_IN_FACTOR and self.quality > self.QUALITY_FACTOR:
            self.decrase_quality()
