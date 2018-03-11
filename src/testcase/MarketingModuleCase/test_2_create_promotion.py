import unittest
from src.page.home_page import PromotionManage
from src.page.base_case import BaseTestCase
from utils.log import logger


class CreatePromotionTest(BaseTestCase):
    """新增促销"""

    def test_sale_with_present(self):
        """新增买赠"""
        product_pro = PromotionManage(self.driver)
        product_pro.open_promotion_manage()
        product_pro.click_pro_promotion()
        before_add = len(product_pro.checkbox)
        product_pro.add()
        product_pro.open_product_list()
        product_pro.select_product_01()
        product_pro.confirm()
        product_pro.condition_num()
        product_pro.discount_num()
        product_pro.select_gift()
        product_pro.customer_level()
        product_pro.save()
        after_add = len(product_pro.checkbox)
        self.assertEqual(after_add, before_add + 1)
        logger.info("成功新增商品促销——买赠")

    def test_straight_down(self):
        """新增直降"""
        product_pro = PromotionManage(self.driver)
        product_pro.open_promotion_manage()
        product_pro.click_pro_promotion()
        before_add = len(product_pro.checkbox)
        product_pro.add()
        product_pro.open_product_list()
        product_pro.select_product_01()
        product_pro.confirm()
        product_pro.straight_down()
        product_pro.discount_price()
        product_pro.customer_level()
        product_pro.save()
        after_add = len(product_pro.checkbox)
        self.assertEqual(after_add, before_add + 1)
        logger.info("成功新增商品促销——直降")

    def test_product_discount(self):
        """新增打折"""
        product_pro = PromotionManage(self.driver)
        product_pro.open_promotion_manage()
        product_pro.click_pro_promotion()
        before_add = len(product_pro.checkbox)
        product_pro.add()
        product_pro.open_product_list()
        product_pro.select_product_01()
        product_pro.confirm()
        product_pro.discount()
        product_pro.discount_percent()
        product_pro.customer_level()
        product_pro.save()
        after_add = len(product_pro.checkbox)
        self.assertEqual(after_add, before_add + 1)
        logger.info("成功新增商品促销——打折")

    def test_satisfy_gift_ord(self):
        """新增订单满赠"""
        ord = PromotionManage(self.driver)
        ord.open_promotion_manage()
        ord.click_order_promotion()
        before_add = ord.total_strip() if len(ord.checkbox) != 1 else 0
        ord.add()
        ord.condition_num()
        ord.discount_num()
        ord.select_gift()
        ord.customer_level()
        ord.save()
        after_add = ord.total_strip()
        self.assertEqual(after_add, before_add + 1)
        logger.info("成功新增订单促销——满赠")

    def test_satisfy_subtract_ord(self):
        """新增订单满减"""
        ord = PromotionManage(self.driver)
        ord.open_promotion_manage()
        ord.click_order_promotion()
        before_add = ord.total_strip() if len(ord.checkbox) != 1 else 0
        ord.add()
        ord.straight_down()
        ord.condition_num()
        ord.discount_num()
        ord.customer_level()
        ord.save()
        after_add = ord.total_strip()
        self.assertEqual(after_add, before_add + 1)
        logger.info("成功新增订单促销——满减")

    def test_satisfy_discount_ord(self):
        """新增订单满折"""
        ord = PromotionManage(self.driver)
        ord.open_promotion_manage()
        ord.click_order_promotion()
        before_add = ord.total_strip() if len(ord.checkbox) != 1 else 0
        ord.add()
        ord.discount()
        ord.condition_num()
        ord.discount_num()
        ord.customer_level()
        ord.save()
        after_add = ord.total_strip()
        self.assertEqual(after_add, before_add + 1)
        logger.info("成功新增订单促销——满折")

    def test_sale_present_n(self):
        """新增买赠"""
        gro = PromotionManage(self.driver)
        gro.open_promotion_manage()
        gro.click_group_promotion()
        before_add = gro.total_strip() if len(gro.checkbox) != 1 else 0
        gro.add()
        title = gro.gro_title
        gro.promotion_title()
        gro.open_product_list()
        gro.select_product_0910()
        gro.confirm()
        gro.condition_num()
        gro.discount_num()
        gro.select_gift()
        gro.customer_level()
        gro.save()
        after_add = gro.total_strip()
        self.assertEqual(after_add, before_add + 1)
        self.assertTrue(gro.in_pages(title))
        logger.info("成功新增组合促销——买赠")

    def test_straight_down_n(self):
        """新增直降"""
        gro = PromotionManage(self.driver)
        gro.open_promotion_manage()
        gro.click_group_promotion()
        before_add = gro.total_strip() if len(gro.checkbox) != 1 else 0
        gro.add()
        title = gro.gro_title
        gro.promotion_title()
        gro.open_product_list()
        gro.select_product_0405()
        gro.confirm()
        gro.gro_straight_down()
        gro.condition_num()
        gro.discount_num()
        gro.customer_level()
        gro.save()
        after_add = gro.total_strip()
        self.assertEqual(after_add, before_add + 1)
        self.assertTrue(gro.in_pages(title))
        logger.info("成功新增组合促销——直降")

    def test_product_discount_n(self):
        """新增打折"""
        gro = PromotionManage(self.driver)
        gro.open_promotion_manage()
        gro.click_group_promotion()
        before_add = gro.total_strip() if len(gro.checkbox) != 1 else 0
        gro.add()
        title = gro.gro_title
        gro.promotion_title()
        gro.open_product_list()
        gro.select_product_0607()
        gro.confirm()
        gro.gro_discount()
        gro.condition_num()
        gro.discount_num()
        gro.customer_level()
        gro.save()
        after_add = gro.total_strip()
        self.assertEqual(after_add, before_add + 1)
        self.assertTrue(gro.in_pages(title))
        logger.info("成功新增组合促销——打折")


if __name__ == '__main__':
    unittest.main()
