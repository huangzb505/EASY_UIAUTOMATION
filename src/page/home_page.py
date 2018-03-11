import os
import time
from random import randint
from time import sleep

from src.page.locators import *

from src.page.base_page import BasePage


def random_str(random_length=8, only_digit=False):
    my_str = ""
    if only_digit:
        chars = '0123456789'
    else:
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(random_length):
        my_str += chars[randint(0, length)]
    return my_str


class PublicPages(BasePage):

    def add(self):
        self.click(*PublicLoc.add_btn)
        sleep(1)

    def confirm(self):
        self.click(*PublicLoc.confirm_btn)
        sleep(1)

    def got_it(self):
        self.click(*PublicLoc.got_it_btn)
        sleep(1)

    def save(self):
        self.click(*PublicLoc.save_btn)
        sleep(3)

    def export(self):                   # 导出当前列表
        self.click(*PublicLoc.export_btn)
        sleep(3)

    def export_selected(self):          # 选择性导出
        self.click(*PublicLoc.ex_btn)
        sleep(3)

    def export_default(self):           # 导出默认模板
        self.export_selected()
        self.click(*PublicLoc.default_template)
        sleep(3)

    def download(self):
        self.click(*PublicLoc.down_load)
        sleep(3)

    @property
    def export_data(self):
        # chrome好坑，自动化下载的默认文件位置不按设定的默认文件路径保存
        file_path = self.new_file(r"C:\Users\ircloud\Downloads").replace('\~$', '\\')
        dat = self.get_data(file_path)
        print(file_path)
        return dat

    @property
    def checkbox(self):
        return self.find_elements(*PublicLoc.check_box)

    def select_all(self):
        self.checkbox[0].click()
        sleep(2)

    @property
    def checkbox_num(self):
        return len(self.checkbox)

    @property
    def radio(self):
        return self.find_elements(*PublicLoc.radio)

    def open_product_list(self):
        self.click(*PublicLoc.products_icon)
        sleep(3)

    def total_strip(self):
        pagination_text = self.find_element(*PublicLoc.total_strip_loc).text
        return int(pagination_text[1:-1])

    def each_page_strip(self):
        return int(self.find_element(*PublicLoc.each_page_strip_loc).text[:-3])


class LoginPage(BasePage):

    def click_portal_login_btn(self):
        self.click(*LoginPageLoc.portal_login_btn)

    def input_username(self, username):
        self.find_element(*LoginPageLoc.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*LoginPageLoc.password_loc).send_keys(password)

    def click_login(self):
        self.click(*LoginPageLoc.sso_login_btn)

    def login(self, url, username, password):
        self.get(url)
        self.click_portal_login_btn()
        self.input_username(username)
        self.input_password(password)
        self.click_login()


class ProductList(PublicPages):

    def click_product_menu(self):
        self.click(*MenuLoc.product_menu)

    def display_products(self):
        return len(self.find_elements(*ProductListLoc.product_name))

    def price_precision(self):
        # 取所有单价小数点后的字符长度进行比较，相同返回1,否则0
        return self.decimal_precision(*ProductListLoc.unit_price)

    @property
    def first_market_price(self):
        price = float(self.elements_text(*ProductListLoc.unit_price)[0])
        return price

    @property
    def first_name(self):
        first_name = self.elements_text(*ProductListLoc.product_name)[0]
        return first_name

    def click_first_goods(self):
        self.find_elements(*ProductListLoc.product_name)[0].click()
        sleep(2)

    @property
    def market_price(self):
        return float(self.find_element(*ProductListLoc.market_price).text)

    @property
    def product_name(self):
        return self.find_element(*ProductListLoc.good_name).text


class AddProduct(PublicPages):

    def click_product_menu(self):
        self.move_to_element(*MenuLoc.product_menu)
        sleep(1)
        self.click(*MenuLoc.goods_list)
        sleep(2)

    def input_name(self):
        now = time.strftime("%H%M%S", time.localtime())
        name = "自动新增商品" + now
        self.find_element(*AddProductLoc.product_name).send_keys(name)

    def input_sort_number(self):  # 排序值大一点
        self.send_keys(*AddProductLoc.sort_number, value=9999)

    def select_classify(self):
        self.click(*AddProductLoc.product_classify)
        sleep(1)
        self.click(*AddProductLoc.default_classify)
        sleep(1)

    def select_unit(self):
        self.click(*AddProductLoc.measuring_unit)
        sleep(1)
        self.click(*AddProductLoc.first_unit)
        sleep(1)

    def select_brand(self):
        if self.in_pages("品牌"):
            self.click(*AddProductLoc.product_brand)
            sleep(1)
            self.click(*AddProductLoc.first_brand)
            sleep(1)
        else:
            print("没有启用品牌字段")
            pass

    def product_description(self):
        self.switch_frame(AddProductLoc.frame_id)
        sleep(0.5)
        self.find_element(*AddProductLoc.description).send_keys(random_str(random_length=30))
        self.default_content()
        sleep(0.5)

    def input_price(self):
        self.find_element(*AddProductLoc.market_price).send_keys(random_str(random_length=3, only_digit=True))
        self.find_element(*AddProductLoc.cost_price).send_keys(random_str(random_length=2, only_digit=True))


class BookAndReturnOrderList(PublicPages):

    def open_order_list(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.book_order)
        sleep(1)

    def open_return_list(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.return_order)
        sleep(1)

    def display_orders(self):
        return self.checkbox_num - 1

    def money_precision(self):
        return self.decimal_precision(*OrderListLoc.account_money)

    def click_first_order_code(self):
        self.find_elements(*OrderListLoc.order_id)[0].click()
        sleep(1)

    @property
    def fist_order_code(self):
        return self.elements_text(*OrderListLoc.order_id)[0]

    def click_first_return_code(self):
        self.find_elements(*ReturnOrderAuditLoc.r_order_id)[0].click()
        sleep(1)

    @property
    def fist_return_code(self):
        return self.elements_text(*ReturnOrderAuditLoc.r_order_id)[0]

    @property
    def return_codes(self):
        return self.elements_text(*ReturnOrderAuditLoc.r_order_id)


class CreateOrder(PublicPages):

    def click_order_menu(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.book_order)

    def open_user_option(self):
        self.click(*CreateOderLoc.user_select_option)

    def select_user(self):
        self.click(*CreateOderLoc.first_user)

    def select_products(self):
        select_option = self.checkbox
        for i in range(randint(0, 5), randint(5, 10)):
            select_option[i].click()

    def select_date(self):
        self.click(*CreateOderLoc.calendar_loc)
        self.click(*CreateOderLoc.this_moment)

    def invoice_info(self):
        self.click(*CreateOderLoc.invoice_info)
        sleep(1)
        self.click(*CreateOderLoc.regular_invoice)

    def remark(self):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.find_element(*CreateOderLoc.remark_info).send_keys(u'自动下单时间是' + now)

    @property
    def order_codes(self):
        return self.elements_text(*OrderListLoc.order_id)


class AuditOrder(PublicPages):

    def __init__(self, driver, state):
        super().__init__(driver)
        self.state = state

    def open_order_list(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.book_order)
        sleep(1)

    def select_order_audit(self):
        order_id = self.find_elements(*OrderListLoc.order_id)
        idx = self.state_first_index()
        if idx > 13:
            self.driver.execute_script("arguments[0].scrollIntoView();", order_id[idx])
        order_id[idx].click()
        sleep(1.5)

    def state_first_index(self):
        return self.order_status().index(self.state)

    def exist_state(self):
        if self.state in self.order_status():
            return True
        else:
            print("没有%s的订单" % self.state)
            return False

    def order_status(self):
        return self.elements_text(*OrderListLoc.order_status)

    def audit_pass(self):
        self.click(*AuditOrderLoc.pass_btn)
        sleep(1)

    def confirm_pass(self):
        self.click(*PublicLoc.confirm_btn)
        sleep(2.5)

    def select_date(self):
        self.click(*CreateOderLoc.calendar_loc)
        sleep(1)
        self.click(*CreateOderLoc.this_moment)

    def send_company(self):
        self.click(*AuditOrderLoc.logistics_select)
        sleep(1)
        companies = self.find_elements(*AuditOrderLoc.logistics_companies)
        i = randint(0, len(companies)-1)
        companies[i].click()

    def send_number(self):
        self.find_element(*AuditOrderLoc.logistics_number).send_keys(random_str(only_digit=True))

    def logistics_remark(self):
        self.find_element(*AuditOrderLoc.logistics_remark).send_keys(random_str(random_length=20))

    def display_status(self):
        return self.find_element(*AuditOrderLoc.display_status).text


class ModifyOrder(AuditOrder):

    def modify_order(self):
        self.select_order_audit()
        self.click(*ModifyOrderLoc.modify_btn)

    def modify_number(self):
        self.send_keys(*ModifyOrderLoc.modify_num, value=randint(10, 100))

    def modify_unit_price(self):
        self.send_keys(*ModifyOrderLoc.unit_price, value=randint(10, 100))
        sleep(1)

    def modify_count_money(self):
        self.send_keys(*ModifyOrderLoc.count_money, value=randint(100, 1000))

    def add_product(self):
        self.find_elements(*ModifyOrderLoc.icon_plus)[0].click()
        sleep(1)
        self.click(*ModifyOrderLoc.icon_product_list)
        sleep(2)

    def icon_plus(self):
        return self.find_elements(*ModifyOrderLoc.icon_plus)

    def reduce_product(self):
        if len(self.icon_plus()) > 1:
            red = self.find_elements(*ModifyOrderLoc.icon_reduce)
            for i in range(0, randint(1, len(red) - 1)):
                red[i].click()
        else:
            print("订单中只有一种商品，无法删除")

    def select_all_products(self):
        self.checkbox[0].click()

    def select_same_products(self):
        select_option = self.checkbox       # 更简单的方法是直接全选 select_option[0].click()
        for i in range(0, randint(5, 13)):  # i=0时全选，i!=0时进行反选,若当前列表商品已被选择则有可能会选不到商品
            if select_option[i].is_enabled():      # is_displayed()\is_selected()
                select_option[i].click()


class BatchAudit(PublicPages):

    def open_order_list(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.book_order)
        sleep(3)

    def batch_export(self):
        self.click(*BatchAuditLoc.batch_export)
        sleep(8)

    @property
    def order_codes(self):
        return self.elements_text(*OrderListLoc.order_id)

    def order_audit(self):
        self.click(*BatchAuditLoc.order_audit)

    def financial_audit(self):
        self.click(*BatchAuditLoc.financial_audit)

    def storage_audit(self):
        self.click(*BatchAuditLoc.storage_audit)

    def delivery_confirm(self):
        self.click(*BatchAuditLoc.delivery_confirm)

    def audit_pass(self):
        if "没有" in self.find_element(*BatchAuditLoc.confirm_content).text:
            self.got_it()
            print("没有需要审核的订单!")
        else:
            self.confirm()
            sleep(2)

    def order_status(self):
        return self.elements_text(*OrderListLoc.order_status)


class AddReceiptRecord(BasePage):

    def __init__(self, driver, state):
        super().__init__(driver)
        self.state = state

    def open_order_list(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.book_order)
        sleep(2)

    def pay_status(self):
        return self.elements_text(*OrderListLoc.pay_status)

    def order_status(self):
        return self.elements_text(*OrderListLoc.order_status)

    def exist_state(self):
        if self.state in self.pay_status():
            return True
        else:
            print("没有%s的订单" % self.state)
            return False

    @property
    def receipt_order_index(self):
        return self.pay_status().index(self.state)

    @property
    def receipt_style(self):
        return self.find_elements(*PublicLoc.radio)

    def cash_pay(self):
        self.receipt_style[0].click()

    def transfer_pay(self):
        self.receipt_style[1].click()

    def select_to_pay(self):
        order_id = self.find_elements(*OrderListLoc.order_id)
        tg = order_id[self.receipt_order_index]
        if self.receipt_order_index > 13:
            self.driver.execute_script("arguments[0].scrollIntoView();", tg)
        tg.click()
        sleep(2)

    def click_receipt_record(self):
        self.click(*AddReceiptRecordLoc.receipt_record)
        self.click(*AddReceiptRecordLoc.add_receipt_record)
        sleep(1)

    def select_receipt_account(self):
        self.click(*AddReceiptRecordLoc.receipt_account)
        sleep(1)
        self.click(*AddReceiptRecordLoc.bank_account)

    @property
    def unpay_money(self):
        return float(self.find_element(*AddReceiptRecordLoc.unpay_money).text.split("：")[1].strip().replace(',', ''))

    @property
    def pay_money(self):
        return float(self.find_element(*AddReceiptRecordLoc.pay_money).get_attribute("value").replace(',', ''))

    @property
    def cash_money(self):
        return float(self.find_element(*AddReceiptRecordLoc.cash_money).get_attribute("value"))

    @property
    def advance_money(self):
        return float(self.find_element(*AddReceiptRecordLoc.advance_money).get_attribute("value"))

    @property
    def rebate_money(self):
        return float(self.find_element(*AddReceiptRecordLoc.rebate_money).get_attribute("value"))

    def confirm(self):
        self.click(*PublicLoc.confirm_btn)
        sleep(1)


class CreateReturnOrder(CreateOrder):

    def click_r_order(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.return_order)
        sleep(1)

    def click_final_refuse_icon(self):       # 点击最后一行的删除按钮
        icons = self.find_elements(*ReturnOrderLoc.refuce_icons)
        target = icons.pop()
        if len(icons) > 13:
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        sleep(1)

    def goods_total_money(self):
        money = self.elements_text(*ReturnOrderLoc.subtotal_money)
        return money.pop()

    def input_refund_sum(self):
        self.find_elements(*ReturnOrderLoc.input_refund_num).pop().send_keys(self.goods_total_money())
        sleep(1)

    def approval_money(self):
        return self.find_element(*ReturnOrderLoc.approval_sum).text

    @property
    def return_order_codes(self):
        return self.elements_text(*OrderListLoc.return_order_code)


class ReturnAudit(AuditOrder):

    def click_r_order(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.return_order)
        sleep(1)

    def select_order_audit(self):
        order_id = self.find_elements(*ReturnOrderAuditLoc.r_order_id)
        target = order_id[self.state_first_index()]
        if self.state_first_index() > 13:
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        sleep(2)

    def order_status(self):
        return self.elements_text(*ReturnOrderAuditLoc.r_order_status)

    def select_stock(self):
        self.send_company()


class BatchReturnAudit(BatchAudit, ReturnAudit):

    def return_audit(self):
        self.click(*ReturnOrderAuditLoc.audit_btn)
        sleep(1)

    def order_status(self):
        return self.elements_text(*ReturnOrderAuditLoc.r_order_status)


class AdvertiseRelease(PublicPages):

    def click_advertise_release(self):
        self.move_to_element(*MenuLoc.marketing_menu)
        sleep(1)
        self.click(*MenuLoc.ad_release)
        sleep(2)

    @property
    def can_release_num(self):
        return int(self.find_element(*AdvertiseReleaseLoc.can_release_num).text)

    def del_advice(self):
        self.click(*AdvertiseReleaseLoc.offside_option)
        sleep(1)
        self.click(*AdvertiseReleaseLoc.delete_btn)
        sleep(1)
        self.click(*PublicLoc.confirm_btn)
        sleep(1)

    @property
    def ad_title(self):
        return "广告" + time.strftime("%H%M%S", time.localtime())

    def enter_ad_title(self):
        self.send_keys(*AdvertiseReleaseLoc.enter_title, value=self.ad_title)

    def select_link_address(self):
        self.click(*AdvertiseReleaseLoc.link_address)
        sleep(1)
        self.click(*AdvertiseReleaseLoc.product_classify)
        sleep(2)
        ic = randint(0, 14)
        self.radio[ic].click()
        self.confirm()
        sleep(1)

    def upload_picture(self):
        self.click(*AdvertiseReleaseLoc.upload_picture)
        sleep(1)
        os.system("E:\\uploadphoto.exe")
        sleep(2)


class AdviceNotice(AdvertiseRelease):

    def open_advice_notice(self):
        self.move_to_element(*MenuLoc.marketing_menu)
        sleep(1)
        self.click(*MenuLoc.notification)
        sleep(1)

    def enter_ad_title(self):
        self.send_keys(*AdviceNoticeLoc.title, value=self.ad_title)

    def select_category(self):
        self.click(*AdviceNoticeLoc.category_option)
        sleep(1)
        self.click(*AdviceNoticeLoc.ad_category)
        sleep(1)

    def input_body_view(self):
        self.switch_frame(AdviceNoticeLoc.frame_id)
        sleep(0.5)
        self.find_element(*AdviceNoticeLoc.body_view).send_keys(random_str(20))
        self.default_content()
        sleep(0.5)

    def send_all_object(self):
        check_box = self.find_elements(*AdviceNoticeLoc.send_object)
        check_box[0].click()
        sleep(0.5)
        check_box[1].click()
        sleep(1)


class PromotionManage(PublicPages):

    def open_promotion_manage(self):
        self.move_to_element(*MenuLoc.marketing_menu)
        sleep(1)

    def click_pro_promotion(self):
        self.click(*MenuLoc.product_promotion)
        sleep(1)

    def click_order_promotion(self):
        self.click(*MenuLoc.order_promotion)
        sleep(1)

    def click_group_promotion(self):
        self.click(*MenuLoc.group_promotion)
        sleep(1)

    @property
    def pro_status(self):
        return self.elements_text(*PromotionLoc.pro_status)

    @property
    def gro_status(self):
        return self.elements_text(*PromotionLoc.gro_status)

    def cancel_all(self):
        self.click(*PromotionLoc.batch_cancel)
        if "没有" in self.find_element(*BatchAuditLoc.confirm_content).text:
            self.got_it()
            print("没有可以作废的促销策略！")
        else:
            self.confirm()
            sleep(3)

    def del_all(self):
        self.click(*PromotionLoc.batch_dele)
        sleep(1)
        if "没有" in self.find_element(*BatchAuditLoc.confirm_content).text:
            self.got_it()
            print("没有可以删除的促销策略！")
        else:
            self.confirm()

    @property
    def gro_title(self):
        now = time.strftime("%H%M%S", time.localtime())
        return "自动促销" + now

    def promotion_title(self):
        self.find_element(*PromotionLoc.pro_title).send_keys(self.gro_title)

    def select_product_01(self):
        self.checkbox[1].click()
        sleep(1)

    def select_product_0910(self):
        self.checkbox[9].click()
        self.checkbox[10].click()
        sleep(1)

    def select_product_0405(self):
        self.checkbox[4].click()
        self.checkbox[5].click()
        sleep(1)

    def select_product_0607(self):
        self.checkbox[6].click()
        self.checkbox[7].click()
        sleep(1)

    def input_numbers(self):  # 数值输入的元素列表
        return self.find_elements(*PromotionLoc.input_num)

    def condition_num(self):    # 满足数量
        self.input_numbers()[0].send_keys(randint(100, 500))

    def discount_num(self):     # 赠品数量 或 降至XX元
        self.input_numbers()[1].send_keys(randint(1, 100))

    def discount_price(self):  # 商品直降价格
        self.input_numbers()[0].send_keys(randint(50, 100))

    def discount_percent(self):  # 折扣率
        self.input_numbers()[0].send_keys(randint(80, 100))

    def select_gift(self):
        self.click(*PromotionLoc.select_gift)
        sleep(2)
        self.radio[1].click()
        self.confirm()
        sleep(1)

    def straight_down(self):  # 直降
        self.radio[1].click()

    def gro_straight_down(self):  # 组合直降
        self.radio[3].click()

    def discount(self):       # 打折
        self.radio[2].click()

    def gro_discount(self):       # 组合打折
        self.radio[4].click()

    def customer_level(self):    # 全部客户级别
        self.checkbox[1].click()


class OrderStatistics(PublicPages):

    def click_delivery_statistics(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.delivery_statistics)
        sleep(1)

    def click_statistics_by_customer(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.statistics_customer)
        sleep(1)

    def click_statistics_by_goods(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.statistics_goods)
        sleep(1)

    def click_statistics_by_detail(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.statistics_detail)
        sleep(1)

    def click_outbound_record(self):
        self.move_to_element(*MenuLoc.order_menu)
        sleep(1)
        self.click(*MenuLoc.storage_del_record)
        sleep(1)

    def export_linked_list(self):
        self.click(*PublicLoc.ex_btn)
        self.click(*OrderStatisticsLoc.linked_list)
        sleep(3)

    def export_delivery_list(self):
        self.click(*OrderStatisticsLoc.export_delivery_list)
        sleep(1)
        self.confirm()
        sleep(5)

    def export_storage_list(self):
        self.click(*OrderStatisticsLoc.export_storage_list)
        sleep(1)
        self.confirm()
        sleep(5)

    @property
    def delivery_codes(self):
        return self.elements_text(*OrderStatisticsLoc.delivery_code)

    @property
    def total_account(self):
        tem = self.elements_text(*OrderStatisticsLoc.statistics_item)
        return float(tem[0])


