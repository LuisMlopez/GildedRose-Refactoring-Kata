# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from aged_brie import AgedBrie
from backstage import Backstage
from sulfuras import Sulfuras
from pepe import Pepe


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_decrease_sell_in(self):
        item = AgedBrie(10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(50, item.quality)

    def test_aged_brie_increase_quality(self):
        item = AgedBrie(10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(41, item.quality)

    def test_aged_brie_sellig_less_than_zero(self):
        item = AgedBrie(0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(-1, item.sell_in)
        self.assertEquals(42, item.quality)

    def test_backstage_decrease_sell_in(self):
        item = Backstage(10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(50, item.quality)

    def test_backstage_increase_quality(self):
        item = Backstage(10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(42, item.quality)

    def test_backstage_increase_quality_2(self):
        item = Backstage(6, 48)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(5, item.sell_in)
        self.assertEquals(50, item.quality)

    def test_backstage_sellig_less_than_zero(self):
        item = Backstage(0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)

    def test_sulfuras_decrease_sell_in(self):
        item = Sulfuras(10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(10, item.sell_in)
        self.assertEquals(50, item.quality)

    def test_sulfuras_increase_quality(self):
        item = Sulfuras(10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(10, item.sell_in)
        self.assertEquals(40, item.quality)

    def test_sulfuras_sellig_less_than_zero(self):
        item = Sulfuras(0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(0, item.sell_in)
        self.assertEquals(40, item.quality)

    def test_pepe_decrease_sell_in(self):
        item = Pepe(10, 50)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(49, item.quality)

    def test_pepe_increase_quality(self):
        item = Pepe(10, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, item.sell_in)
        self.assertEquals(39, item.quality)

    def test_pepe_sellig_less_than_zero(self):
        item = Pepe(0, 40)
        items = [item]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(-1, item.sell_in)
        self.assertEquals(38, item.quality)

        
if __name__ == '__main__':
    unittest.main()
