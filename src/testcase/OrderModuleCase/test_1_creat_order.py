import unittest


from src.page.base_case import BaseTestCase
from src.page.home_page import CreateOrder ,CreateReturnOrder, AddReceiptRecord
from utils.log import logger

NEW = 2              # 新增订单数


class CreateOrderTest(BaseTestCase):

    def test_create_order(self):
        """新增订货单"""
        co = CreateOrder(self.driver)
        co.click_order_menu()
        before_add = co.total_strip()
        for i in range(NEW):
            co.add()
            co.open_user_option()
            co.select_user()
            co.select_date()
            co.invoice_info()
            co.remark()
            co.open_product_list()
            co.select_products()
            co.confirm()
            co.save()
            print("新增{}条订单成功".format(i + 1))
        after_add = co.total_strip()
        new_orders = list(n for n in co.order_codes[:NEW])
        self.assertEqual(after_add, before_add + NEW)
        logger.info("成功新增{0}条订单,新增的订单号为{1}".format(NEW, new_orders))

    def test_create_r_order(self):
        """新增退货单"""
        cro = CreateReturnOrder(self.driver)
        cro.click_r_order()
        before_add = cro.total_strip()
        for i in range(NEW):
            cro.add()
            cro.open_user_option()
            cro.select_user()
            cro.remark()
            cro.open_product_list()
            cro.select_products()
            cro.confirm()
            cro.click_final_refuse_icon()
            cro.input_refund_sum()
            self.assertEqual(cro.goods_total_money(), cro.approval_money())
            cro.save()
            print("新增{}条退单成功".format(i + 1))
        after_add = cro.total_strip()
        new_orders = list(n for n in cro.return_order_codes[:NEW])
        self.assertEqual(after_add, before_add + NEW)
        logger.info("成功新增{0}条退单,新增的订单号为{1}".format(NEW, new_orders))

    def test_receipt_record_add(self):
        """添加收款记录"""
        arr = AddReceiptRecord(self.driver, "未付款")
        arr.open_order_list()
        if arr.exist_state():
            arr.select_to_pay()
            arr.click_receipt_record()
            arr.transfer_pay()
            arr.select_receipt_account()
            unpay_money = arr.unpay_money
            cash_money = arr.cash_money
            pay_money = arr.pay_money
            advance_money = arr.advance_money
            rebate_money = arr.rebate_money
            total_pay = pay_money + advance_money + rebate_money + cash_money
            print(total_pay)
            self.assertEqual(unpay_money, total_pay)
            arr.confirm()


if __name__ == '__main__':
    unittest.main(verbosity=2)