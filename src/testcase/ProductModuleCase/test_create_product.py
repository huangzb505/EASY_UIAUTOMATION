import unittest
from src.page.base_case import BaseTestCase
from src.page.home_page import AddProduct
from utils.log import logger


class AddProductTest(BaseTestCase):
    """新增商品"""

    def test_add_product(self):
        """新增商品"""
        ap = AddProduct(self.driver)
        ap.click_product_menu()
        before_add = ap.total_strip()
        ap.add()
        ap.input_name()
        ap.input_sort_number()
        ap.select_brand()
        ap.select_classify()
        ap.select_unit()
        ap.product_description()
        ap.input_price()
        ap.save()
        after_add = ap.total_strip()
        self.assertEqual(after_add, before_add + 1)
        logger.info("新增商品成功,当前商品总数为{}".format(after_add))

if __name__ == '__main__':
    unittest.main()