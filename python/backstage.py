from item import Item


class Backstage(Item):
    NAME = 'Backstage passes to a TAFKAL80ETC concert'
    QUALITY_FACTOR = 50
    FIRST_SELL_IN_FACTOR = 11
    SECOND_SELL_IN_FACTOR = 6
    THIRD_SELL_IN_FACTOR = 0

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        self.decrease_sell_in()

        if self.quality < self.QUALITY_FACTOR:
            self.increase_quality()

        if self.sell_in < self.FIRST_SELL_IN_FACTOR and self.quality < self.QUALITY_FACTOR:
            self.increase_quality()

        if self.sell_in < self.SECOND_SELL_IN_FACTOR and self.quality < self.QUALITY_FACTOR:
            self.increase_quality()

        if self.sell_in < self.THIRD_SELL_IN_FACTOR:
            self.reset_quality()
