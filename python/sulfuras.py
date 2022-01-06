from item import Item


class Sulfuras(Item):
    NAME = 'Sulfuras, Hand of Ragnaros'

    def __init__(self, sell_in, quality):
        super().__init__(self.NAME, sell_in, quality)

    def update_quality(self):
        pass
