import unittest
from src.page.home_page import PromotionManage
from src.page.base_case import BaseTestCase
from utils.log import logger


class InitPromotionTacticsTest(BaseTestCase):
    """初始化促销策略"""
    # 只做了批量作废和删除

    def test_cancel_tactics_pro(self):
        """批量作废商品促销"""
        pro = PromotionManage(self.driver)
        pro.open_promotion_manage()
        pro.click_pro_promotion()
        if len(pro.checkbox) > 1:
            pro.select_all()
            pro.cancel_all()
            self.assertNotIn("促销中", pro.pro_status)
            logger.info("批量作废商品促销成功")
        else:
            print("商品促销列表为空")
            logger.warning("商品促销列表为空")

    def test_cancel_tactics_gro(self):
        """批量作废组合促销"""
        gro = PromotionManage(self.driver)
        gro.open_promotion_manage()
        gro.click_group_promotion()
        if len(gro.checkbox) > 1:
            gro.select_all()
            gro.cancel_all()
            self.assertNotIn("促销中", gro.gro_status)
            logger.info("批量作废组合促销成功")
        else:
            print("组合促销列表为空")
            logger.warning("组合促销列表为空")

    def test_cancel_tactics_order(self):
        """批量作废订单促销"""
        ord = PromotionManage(self.driver)
        ord.open_promotion_manage()
        ord.click_order_promotion()
        if len(ord.checkbox) > 1:
            ord.select_all()
            ord.cancel_all()
            self.assertNotIn("促销中", ord.gro_status)
            logger.info("批量作废订单促销成功")
        else:
            print("订单促销列表为空")
            logger.warning("订单促销列表为空")

    def test_del_tactics_pro(self):
        """批量删除商品促销"""
        pro = PromotionManage(self.driver)
        pro.open_promotion_manage()
        pro.click_pro_promotion()
        if len(pro.checkbox) > 1:
            pro.select_all()
            pro.del_all()
            self.assertTrue(pro.in_pages("暂无数据"))
            logger.info("批量删除商品促销成功")
        else:
            print("商品促销列表为空")
            logger.warning("商品促销列表为空")

    def test_del_tactics_gro(self):
        """批量删除组合促销"""
        gro = PromotionManage(self.driver)
        gro.open_promotion_manage()
        gro.click_group_promotion()
        if len(gro.checkbox) > 1:
            gro.select_all()
            gro.del_all()
            self.assertTrue(gro.in_pages("暂无数据"))
            logger.info("批量删除组合促销成功")
        else:
            print("组合促销列表为空")
            logger.warning("组合促销列表为空")

    def test_del_tactics_order(self):
        """批量删除订单促销"""
        ord = PromotionManage(self.driver)
        ord.open_promotion_manage()
        ord.click_order_promotion()
        if len(ord.checkbox) > 1:
            ord.select_all()
            ord.del_all()
            self.assertTrue(ord.in_pages("暂无数据"))
            logger.info("批量删除订单促销成功")
        else:
            print("订单促销列表为空")
            logger.warning("订单促销列表为空")

if __name__ == '__main__':
    unittest.main(verbosity=2)
