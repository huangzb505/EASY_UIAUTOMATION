import unittest
from src.page.home_page import BatchAudit
from src.page.base_case import BaseTestCase
from utils.log import logger


class BatchOrderAuditTest(BaseTestCase):
    """批量订单审核流程"""

    def test_a_batch_order_audit(self):
        """批量订单审核"""
        batch_audit = BatchAudit(self.driver)
        batch_audit.open_order_list()
        batch_audit.select_all()
        batch_audit.order_audit()
        batch_audit.audit_pass()
        self.assertNotIn("待订单审核", batch_audit.order_status())
        logger.info("批量订单审核成功")

    def test_b_batch_financial_audit(self):
        """批量财务审核"""
        batch_audit = BatchAudit(self.driver)
        batch_audit.open_order_list()
        batch_audit.select_all()
        batch_audit.financial_audit()
        batch_audit.audit_pass()
        self.assertNotIn("待财务审核", batch_audit.order_status())
        logger.info("批量财务审核成功")

    def test_c_batch_storage_audit(self):
        """批量出库审核"""
        batch_audit = BatchAudit(self.driver)
        batch_audit.open_order_list()
        batch_audit.select_all()
        batch_audit.storage_audit()
        batch_audit.audit_pass()
        self.assertNotIn("待出库审核", batch_audit.order_status())
        logger.info("批量出库审核成功")

    def test_d_batch_delivery_confirm(self):
        """批量发货确认"""
        batch_audit = BatchAudit(self.driver)
        batch_audit.open_order_list()
        batch_audit.select_all()
        batch_audit.delivery_confirm()
        batch_audit.audit_pass()
        self.assertNotIn("待发货确认", batch_audit.order_status())
        logger.info("批量发货确认成功")

if __name__ == '__main__':
    unittest.main()
