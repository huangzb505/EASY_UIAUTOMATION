from selenium.webdriver.common.by import By


class PublicLoc:
    add_btn = (By.XPATH, "//span[text()='新 增']")
    save_btn = (By.XPATH, "//span[text()='保 存']")
    confirm_btn = (By.XPATH, "//span[text()='确 定']")
    got_it_btn = (By.XPATH, "//span[text()='知道了']")
    check_box = (By.CSS_SELECTOR, "input.ant-checkbox-input")
    radio = (By.CSS_SELECTOR, "input.ant-radio-input")
    products_icon = (By.XPATH, "//tr[1]/td[3]/div/button/i")
    total_strip_loc = (By.CSS_SELECTOR, "span.ant-pagination-total-text")
    each_page_strip_loc = (By.XPATH, "//ul/div/div[1]/div/div/div")
    export_btn = (By.XPATH, "//span[text()='导 出']")
    ex_btn = (By.XPATH, "//span[text()='导出']")
    down_load = (By.XPATH, "//ul[@class='progress-ul']/li[1]/a")
    default_template = (By.LINK_TEXT, "导出默认模板")


class LoginPageLoc:
    portal_login_btn = (By.LINK_TEXT, "登录")
    username_loc = (By.ID, "username")
    password_loc = (By.ID, "password")
    sso_login_btn = (By.ID, "loginBtn")


class MenuLoc:
    order_menu = (By.XPATH, "//span[text()='订单']")
    book_order = (By.XPATH, "//span[text()='订货单']")
    return_order = (By.LINK_TEXT, "退货单")
    storage_del_record = (By.LINK_TEXT, "出库/发货记录")
    statistics_detail = (By.LINK_TEXT, "订单商品统计（明细）")
    statistics_customer = (By.LINK_TEXT, "订单商品统计（按客户）")
    statistics_goods = (By.LINK_TEXT, "订单商品统计（按商品）")
    delivery_statistics = (By.LINK_TEXT, "发货统计")

    product_menu = (By.XPATH, "//span[text()='商品']")
    goods_list = (By.LINK_TEXT, "商品列表")
    goods_stock = (By.LINK_TEXT, "商品库存")
    input_storage = (By.LINK_TEXT, "商品入库")
    output_storage = (By.LINK_TEXT, "商品出库")
    stock_transfer = (By.LINK_TEXT, "库存调拨")
    stock_check = (By.LINK_TEXT, "库存盘点")
    stock_detail = (By.LINK_TEXT, "出入库明细")
    transmit_collect = (By.LINK_TEXT, "商品收发汇总")
    cost_adjust = (By.LINK_TEXT, "成本调整")
    terminal_carry = (By.LINK_TEXT, "期末结转")
    customer_manage = (By.LINK_TEXT, "供应商管理")
    intelligent_procurement = (By.LINK_TEXT, "智能采购")
    procurement_order = (By.LINK_TEXT, "采购订单")
    procurement_return = (By.LINK_TEXT, "采购退货")
    procurement_collect = (By.LINK_TEXT, "采购汇总")

    customer_menu = (By.XPATH, "//span[text()='客户']")
    customer_list = (By.LINK_TEXT, "客户列表")
    join_info = (By.LINK_TEXT, "加盟信息")
    customer_feedback = (By.LINK_TEXT, "客户反馈")

    capital_menu = (By.XPATH, "//span[text()='资金']")
    receipt_confirm = (By.LINK_TEXT, "收款确认")
    capital_account = (By.LINK_TEXT, "资金账户")
    receipt_account = (By.LINK_TEXT, "收款账户")
    capital_detail = (By.LINK_TEXT, "收支明细")
    receipt_collect = (By.LINK_TEXT, "订单收款统计")

    marketing_menu = (By.XPATH, "//span[text()='营销']")
    ad_release = (By.LINK_TEXT, "广告发布")
    notification = (By.LINK_TEXT, "通知公告")
    SMS_pay = (By.LINK_TEXT, "短信充值")
    SMS_set = (By.LINK_TEXT, "短信设置")
    product_promotion = (By.LINK_TEXT, "商品促销")
    order_promotion = (By.LINK_TEXT, "订单促销")
    combine_promotion = (By.LINK_TEXT, "组合促销")
    seckill_manage = (By.LINK_TEXT, "秒杀管理")
    big_wheel = (By.LINK_TEXT, "大转盘")

    report_menu = (By.XPATH, "//span[text()='报表']")
    application_center = (By.XPATH, "//span[text()='应用中心']")
    fresh_suite = (By.XPATH, "//span[text()='生鲜套件']")


class ProductListLoc:
    product_name = (By.XPATH, "//tr/td[4]/a/div/span")
    first_product = (By.XPATH, "//tr[1]/td[4]/a/div/span")
    unit_price = (By.XPATH, "//tr/td[8]/span")  # 单价位于第8列时
    market_price = (By.XPATH, "//div[@class='pd-money-head1']/span[1]/span")
    good_name = (By.TAG_NAME, "h4")


class AddProductLoc:
    product_name = (By.ID, "name")
    product_classify = (By.XPATH, "//span[text()='请选择']")
    default_classify = (By.XPATH, "//span[text()='通用']")
    measuring_unit = (By.XPATH, "//div[text()='请选择']")
    product_brand = (By.XPATH, "//div[text()='请选择商品品牌']")
    sort_number = (By.ID, "sortNum")
    first_brand = (By.XPATH, "//ul/li[@class='ant-select-dropdown-menu-item'][1]")
    first_unit = (By.XPATH, "//li[text()='个']")
    frame_id = "ueditor_0"
    description = (By.CSS_SELECTOR, "body.view")
    market_price = (By.CSS_SELECTOR, "div.pde-serprice-head > div > div > input")
    cost_price = (By.CSS_SELECTOR, "div.pde-serprice-head > span > div > div > input")


class OrderListLoc:
    # 订单列表
    sub_tag = (By.CLASS_NAME, "sub-tag")
    order_id = (By.XPATH, "//tr/td[2]/div/div/span/a")
    account_money = (By.XPATH, "//tr/td[6]/div")  # 金额所在列
    order_status = (By.XPATH, "//tr/td[8]/div/span")
    offside_btn = (By.XPATH, "//tbody/tr/td/span/i")
    pay_status = (By.XPATH, "//tr/td[9]/div")

    # 退单列表
    return_order_code = (By.XPATH, "//tr/td[2]/div/span/a/div")


class CreateOderLoc:
    user_select_option = (By.CSS_SELECTOR, "div.ant-select-selection__placeholder")
    first_user = (By.CSS_SELECTOR, "div.body > div > div > div > div > ul > li")
    calendar_loc = (By.CSS_SELECTOR, "input.ant-calendar-picker-input.ant-input.ant-input-lg")
    this_moment = (By.CLASS_NAME, "ant-calendar-today-btn ")
    invoice_info = (By.XPATH, "//div[text()='不开发票']")
    regular_invoice = (By.XPATH, "//li[contains(text(),'普通发票（')]")
    remark_info = (By.ID, "remark")


class AuditOrderLoc:
    # 订单审核
    pass_btn = (By.XPATH, "//button/span")      # 通过、出库、发货的按钮
    logistics_select = (By.CLASS_NAME, "ant-select-selection__rendered")
    logistics_companies = (By.CLASS_NAME, "ant-select-dropdown-menu-item")
    logistics_number = (By.CSS_SELECTOR, "input#sendNumber")
    logistics_remark = (By.ID, "logisticsRemark")
    display_status = (By.CSS_SELECTOR, "span.red.order-dispalyStatus")


class ModifyOrderLoc:
    # 订单修改
    modify_btn = (By.XPATH, "//div[@class='order-detail-op']/span[1]/i")
    modify_num = (By.XPATH, "//tbody/tr[1]/td[7]/div/div[2]/input")
    unit_price = (By.XPATH, "//tbody/tr[1]/td[9]/div/div[2]/input")
    count_money = (By.XPATH, "//tbody/tr[1]/td[9]/div/div[2]/input")
    icon_plus = (By.CSS_SELECTOR, "i.iconfont.icon-plus.common-op")
    icon_reduce = (By.CSS_SELECTOR, "i.iconfont.icon-reduce.common-op")
    icon_product_list = (By.XPATH, "//tbody/tr[2]/td[3]/div/button/i")


class BatchAuditLoc:
    confirm_content = (By.CSS_SELECTOR, "div.table-box.ant-table-confirm")
    order_audit = (By.XPATH, "//span[text()='订单审核']")
    financial_audit = (By.XPATH, "//span[text()='财务审核']")
    storage_audit = (By.XPATH, "//span[text()='出库审核']")
    delivery_confirm = (By.XPATH, "//span[text()='发货确认']")
    batch_export = (By.XPATH, "//a[text()='导出']")


class AddReceiptRecordLoc:
    receipt_record = (By.XPATH, "//div[text()='收款记录']")
    add_receipt_record = (By.XPATH, "//span[text()='添加收款记录']")
    receipt_account = (By.CLASS_NAME, "ant-select-selection__rendered")
    bank_account = (By.XPATH, "(//li[@role='menuitem'])[1]")
    pay_money = (By.ID, "payMoney")
    cash_money = (By.ID, "fundAccount1")
    advance_money = (By.ID, "fundAccount2")
    rebate_money = (By.ID, "fundAccount3")
    unpay_money = (By.CSS_SELECTOR, ".danger.mr40")


class ReturnOrderLoc:
    # 其他元素同新增订货单
    refuce_icons = (By.CSS_SELECTOR, ".iconfont.icon-reduce.common-op")
    subtotal_money = (By.XPATH, "//tr/td[10]")
    input_refund_num = (By.CLASS_NAME, "ant-input-number-input")
    approval_sum = (By.CSS_SELECTOR, ".order-money-item.red")


class ReturnOrderAuditLoc:
    r_order_status = (By.XPATH, "//tr/td[6]/div/span")
    r_order_id = (By.XPATH, "//tr/td[2]/div/span/a/div")
    audit_btn = (By.XPATH, "//button[text()='审核']")


class AdvertiseReleaseLoc:

    can_release_num = (By.CSS_SELECTOR, "span.red")
    enter_title = (By.XPATH, "//input[@placeholder='请输入广告标题']")
    link_address = (By.XPATH, "//div[text()='请设置广告页面链接']")
    product_classify = (By.XPATH, "//li[text()='商品及分类']")
    select_icon = (By.CLASS_NAME, "ant-radio-input")
    upload_picture = (By.CLASS_NAME, "txt")
    offside_option = (By.XPATH, "//*[@id='main-wrap']/div/div[2]/div[2]/div[1]/div/div[2]/div\
                                /div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td/span/i")
    delete_btn = (By.XPATH, "//li[text()='删除']")


class AdviceNoticeLoc:
    title = (By.ID, "title")
    category_option = (By.XPATH, "//form/div[2]/div/div/div[2]/div/div/div/div")
    ad_category = (By.XPATH, "//li[text()='公司公告']")
    frame_id = "ueditor_0"
    body_view = (By.CSS_SELECTOR, "body.view")
    send_object = (By.XPATH, "//input[@type='checkbox']")


class PromotionLoc:
    batch_cancel = (By.XPATH, "//button[text()='批量作废']")
    batch_dele = (By.XPATH, "//button[text()='批量删除']")
    pro_status = (By.XPATH, "//tbody/tr/td[9]")
    gro_status = (By.XPATH, "//tbody/tr/td[6]")
    radio = (By.CSS_SELECTOR, "input.ant-radio-input")
    select_gift = (By.LINK_TEXT, "请选择商品")
    pro_title = (By.ID, "name")
    all_level = (By.XPATH, "//label/span[1]/input")
    input_num = (By.CSS_SELECTOR, "input.ant-input-number-input")


class OrderStatisticsLoc:

    statistics_item = (By.CLASS_NAME, "statistics-item-val")
    linked_list = (By.PARTIAL_LINK_TEXT, "二维表")
    delivery_code = (By.XPATH, "//tr/td[2]/a")
    export_storage_list = (By.XPATH, "//button[contains(text(),'导出出库单')]")
    export_delivery_list = (By.XPATH, "//button[contains(text(),'导出发货单')]")


