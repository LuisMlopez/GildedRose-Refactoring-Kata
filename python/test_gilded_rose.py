# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_aged_brie_decrease_sell_in(self):
        item = Item('Aged Brie', 10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(50, item.quality)

    def test_aged_brie_increase_quality(self):
        item = Item('Aged Brie', 10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(41, item.quality)

    def test_aged_brie_sellig_less_than_zero(self):
        item = Item('Aged Brie', 0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(-1, item.sell_in)
        self.assertEquals(42, item.quality)

    def test_backstage_decrease_sell_in(self):
        item = Item('Backstage passes to a TAFKAL80ETC concert', 10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(50, item.quality)

    def test_backstage_increase_quality(self):
        item = Item('Backstage passes to a TAFKAL80ETC concert', 10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(42, item.quality)

    def test_backstage_sellig_less_than_zero(self):
        item = Item('Backstage passes to a TAFKAL80ETC concert', 0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)

    def test_sulfuras_decrease_sell_in(self):
        item = Item('Sulfuras, Hand of Ragnaros', 10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(10, item.sell_in)
        self.assertEquals(50, item.quality)

    def test_sulfuras_increase_quality(self):
        item = Item('Sulfuras, Hand of Ragnaros', 10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(10, item.sell_in)
        self.assertEquals(40, item.quality)

    def test_sulfuras_sellig_less_than_zero(self):
        item = Item('Sulfuras, Hand of Ragnaros', 0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(0, item.sell_in)
        self.assertEquals(40, item.quality)

    def test_pepe_decrease_sell_in(self):
        item = Item('Pepe', 10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(49, item.quality)

    def test_pepe_increase_quality(self):
        item = Item('Pepe', 10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(39, item.quality)

    def test_pepe_sellig_less_than_zero(self):
        item = Item('Pepe', 0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(-1, item.sell_in)
        self.assertEquals(38, item.quality)

        
if __name__ == '__main__':
    unittest.main()
