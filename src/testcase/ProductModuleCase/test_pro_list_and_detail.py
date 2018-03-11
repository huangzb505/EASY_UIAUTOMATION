import unittest
from src.page.base_case import BaseTestCase
from src.page.home_page import ProductList
from utils.log import logger


class ProductPageTest(BaseTestCase):
    """商品列表及详情"""

    def test_product_page(self):
        """商品列表及详情校验"""
        pp = ProductList(self.driver)
        pp.click_product_menu()
        first_market_price = pp.first_market_price
        first_name = pp.first_name
        logger.info("第一个商品名称：{0}，市场价：{1}".format(first_name, first_market_price))
        if pp.total_strip() > pp.each_page_strip():
            self.assertEqual(pp.display_products(), pp.each_page_strip())
        else:
            self.assertEqual(pp.display_products(), pp.total_strip())
        self.assertTrue(pp.price_precision())
        pp.click_first_goods()
        logger.info("商品详情商品名称为：{1},市场价为：{0}，".format(pp.market_price, pp.product_name))
        self.assertEqual(first_market_price, pp.market_price)
        self.assertIn(pp.product_name, first_name)


if __name__ == '__main__':
    unittest.main()
