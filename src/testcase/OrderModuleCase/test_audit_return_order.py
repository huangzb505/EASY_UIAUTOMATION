import unittest
from src.page.base_case import BaseTestCase
from src.page.home_page import ReturnAudit, BatchReturnAudit
from utils.log import logger


class ReturnAuditTest(BaseTestCase):
    """退单审核流程"""

    def test_a_return_audit(self):
        """待退单审核"""
        return_audit = ReturnAudit(self.driver, "待退单审核")
        return_audit.click_r_order()
        if return_audit.exist_state():
            audit_order_index = return_audit.state_first_index()
            return_audit.select_order_audit()
            return_audit.audit_pass()
            return_audit.confirm_pass()
            after_audit_state = return_audit.order_status()[audit_order_index]
            self.assertEqual("待收货确认", after_audit_state)
            logger.info("退单审核成功")

    def test_b_receipt_confirm(self):
        """待收货确认"""
        return_audit = ReturnAudit(self.driver, "待收货确认")
        return_audit.click_r_order()
        if return_audit.exist_state():
            audit_order_index = return_audit.state_first_index()
            return_audit.select_order_audit()
            return_audit.audit_pass()
            return_audit.select_stock()
            return_audit.confirm_pass()
            after_audit_state = return_audit.order_status()[audit_order_index]
            self.assertEqual("待退款确认", after_audit_state)
            logger.info("收货确认成功")

    def test_c_refund_confirm(self):
        """待退款确认"""
        return_audit = ReturnAudit(self.driver, "待退款确认")
        return_audit.click_r_order()
        if return_audit.exist_state():
            audit_order_index = return_audit.state_first_index()
            return_audit.select_order_audit()
            return_audit.audit_pass()
            return_audit.confirm_pass()
            after_audit_state = return_audit.order_status()[audit_order_index]
            self.assertIsNot("待退款确认", after_audit_state)
            logger.info("退款确认成功")

    def test_d_batch_return_audit(self):
        """批量退单审核"""
        batch_return = BatchReturnAudit(self.driver, "待退单审核")
        batch_return.click_r_order()
        batch_return.select_all()
        batch_return.return_audit()
        batch_return.audit_pass()
        self.assertNotIn("待退单审核", batch_return.order_status())
        logger.info("批量退单审核成功")

if __name__ == '__main__':
    unittest.main()