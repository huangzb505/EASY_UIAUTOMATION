import unittest
from src.page.base_case import BaseTestCase
from src.page.home_page import ModifyOrder
from utils.log import logger


class ModifyOrderTest(BaseTestCase):
    """修改订单"""

    def test_modify_order_add_pro(self):
        """修改订单——增加商品"""
        mo = ModifyOrder(self.driver, "待订单审核")
        mo.open_order_list()
        if mo.exist_state():
            mo.modify_order()
            mo.modify_number()
            mo.modify_unit_price()
            mo.modify_count_money()
            mo.add_product()
            mo.select_all_products()
            mo.confirm()
            if mo.in_pages("请选择商品"):
                logger.warning("当前列表的商品已在商品清单中")
            mo.save()
            self.assertTrue(mo.in_pages("订单详情"))
            logger.info("订单添加商品成功")

    def test_modify_order_reduce_pro(self):
        """修改订单——减少商品"""
        mo = ModifyOrder(self.driver, "待订单审核")
        mo.open_order_list()
        if mo.exist_state():
            mo.modify_order()
            mo.reduce_product()
            mo.save()
            self.assertTrue(mo.in_pages("订单详情"))
            logger.info("订单删除商品成功")


if __name__ == '__main__':
    unittest.main()