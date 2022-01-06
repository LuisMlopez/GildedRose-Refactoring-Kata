from item import Item


class AgedBrie(Item):
    NAME = 'Aged Brie'
    QUALITY_FACTOR = 50
    SELL_IN_FACTOR = 0

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        self.decrease_sell_in()

        if self.quality < self.QUALITY_FACTOR:
            self.increase_quality()

        if self.sell_in < self.SELL_IN_FACTOR and self.quality < self.QUALITY_FACTOR:
            self.increase_quality()
