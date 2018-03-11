import unittest
from src.page.home_page import AdvertiseRelease, AdviceNotice
from src.page.base_case import BaseTestCase


class AdviceNoticeTest(BaseTestCase):
    """广告通知"""

    def test_add_advertise(self):
        """广告发布"""
        ar = AdvertiseRelease(self.driver)
        ar.click_advertise_release()
        if ar.can_release_num:
            before_add = ar.can_release_num
            ar.add()
            title = ar.ad_title
            ar.enter_ad_title()
            ar.select_link_address()
            ar.upload_picture()
            ar.save()
            after_add = ar.can_release_num
            self.assertEqual(before_add, after_add + 1)
            self.assertTrue(ar.in_pages(title))
        else:
            print("广告发布已达上限")

    def test_delete_advertise(self):
        """广告删除"""
        da = AdvertiseRelease(self.driver)
        da.click_advertise_release()
        if da.can_release_num != 10:
            before_del = da.can_release_num
            da.del_advice()
            after_del = da.can_release_num
            self.assertEqual(before_del, after_del - 1)
        else:
            print("暂无数据，赶紧新增广告吧")

    def test_advice_notice(self):
        """通知公告"""
        an = AdviceNotice(self.driver)
        an.open_advice_notice()
        add_before = 0 if an.in_pages("暂无数据") else an.total_strip()
        an.add()
        title = an.ad_title
        an.enter_ad_title()
        an.select_category()
        an.input_body_view()
        an.send_all_object()
        an.save()
        add_after = an.total_strip()
        self.assertEqual(add_after, add_before + 1)
        self.assertTrue(an.in_pages(title))

    def test_delete_notice(self):
        """通知删除"""
        dn = AdviceNotice(self.driver)
        dn.open_advice_notice()
        if dn.in_pages("暂无数据"):
            print("暂无通知，赶紧发布吧！")
        else:
            before_del = dn.total_strip()
            dn.del_advice()
            after_del = dn.total_strip() if before_del != 1 else 0
            self.assertEqual(before_del, after_del + 1)

if __name__ == '__main__':
    unittest.main()
