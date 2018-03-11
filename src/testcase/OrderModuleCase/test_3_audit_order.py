import unittest
from src.page.base_case import BaseTestCase
from src.page.home_page import AuditOrder
from utils.log import logger


class OrderAuditTest(BaseTestCase):
    """订单审核流程"""

    def test_1_order_audit(self):
        """订单审核"""
        order_audit = AuditOrder(self.driver, "待订单审核")
        order_audit.open_order_list()
        if order_audit.exist_state():
            audit_order_index = order_audit.state_first_index()
            order_audit.select_order_audit()
            order_audit.audit_pass()
            order_audit.confirm_pass()
            after_audit_state = order_audit.order_status()[audit_order_index]
            self.assertEqual("待财务审核", after_audit_state)
            logger.info("订单审核成功")

    def test_2_financial_audit(self):
        """财务审核"""
        order_audit = AuditOrder(self.driver, "待财务审核")
        order_audit.open_order_list()
        if order_audit.exist_state():
            audit_order_index = order_audit.state_first_index()
            order_audit.select_order_audit()
            order_audit.audit_pass()
            order_audit.confirm_pass()
            after_audit_state = order_audit.order_status()[audit_order_index]
            self.assertEqual("待出库审核", after_audit_state)
            logger.info("财务审核成功")

    def test_3_storage_audit(self):
        """出库审核"""
        order_audit = AuditOrder(self.driver, "待出库审核")
        order_audit.open_order_list()
        if order_audit.exist_state():
            order_audit.select_order_audit()
            order_audit.audit_pass()
            order_audit.audit_pass()
            order_audit.confirm_pass()
            self.assertEqual("待发货确认", order_audit.display_status())
            logger.info("出库审核成功")

    def test_4_delivery_confirm(self):
        """发货确认"""
        order_audit = AuditOrder(self.driver, "待发货确认")
        order_audit.open_order_list()
        if order_audit.exist_state():
            order_audit.select_order_audit()
            order_audit.audit_pass()
            order_audit.audit_pass()
            order_audit.select_date()
            order_audit.send_company()
            order_audit.send_number()
            order_audit.logistics_remark()
            order_audit.confirm_pass()
            self.assertEqual("已完成", order_audit.display_status())
            logger.info("发货确认成功")

if __name__ == '__main__':
    unittest.main()

