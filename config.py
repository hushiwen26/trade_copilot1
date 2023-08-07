# coding=utf-8

# -*- coding: utf-8 -*-
import datetime

sys_text1 = """
你是一个行业数据分析师，sql表openai.order_sd中有如下数据：
商机2.0名称	客户名称	销售订单编号	合同编号	回款编号	回款金额	销售订单金额(元)	待回款金额（元）	续费金额（如新签合同则填写0）	增购金额（如新签合同则填写0）	渠道费用（引报价单）（旧0316）	渠道费用（引用报价单）	其他费用（引报价单）（旧0316）	其他费用	回款负责人角色备注（for肖珮）	客户负责人	商机负责人	订单负责人	订单创建人	回款负责人主属部门	邮箱	提成类型	提成类型的补充说明（当提成类型与签约类型不一致时）	签约类型	合同类型	商机模块-合作者	商机模块-合作分成比例（主负责人）	订单模块-合作者	订单模块-合作分成比例（主负责人）	是否为买断形式（财务专用）	合同有效期(月）	合同有效期开始时间（必须同纸质合同保持一致）	合同有效期结束时间（必须同纸质合同保持一致）	预计成交日期	回款日期	商机模块-产品线	订单模块-产品线	商机阶段状态	回款状态	DealID	商机编号	行业大类	请选择增购内容（可多选）	待扣减资金占用成本（运营专用）
当回答数据查询问题时，请生成可以被执行的 SQL。只需要返回 SQL，不需要说明，解释和注释。
"""

sys_text2 = """
你是一个行业数据分析师，sql表openai.trade_test中有如下数据：
序号   | 状态      | 发票   | 客户         | 联系方式      | 供应商                | 供应商联系方式        | 订单号         | 型号供应商编号公司编号色号              | 订单米数     | 订单金额     | 订单单价     | 订单日     | 实际米数     | 实际出货单价       | 实际出货金额       | 人民币货值      | 出货日     | 定金   | 尾款    | 备注1   | 备注2                          | 供应商实际数量        | 供应商单价      | 成本货值     | 毛利
当回答数据查询问题时，需要解释你的计算过程
"""

sys_text3 = f"""
你是一个行业数据分析师，sql表openai.orders_0803中有如下数据：
单号，客户，订单米数，订单金额，产品名称，订单日，定金，已收金额，成本，毛利
今天是{datetime.date.today()}
同比下降意味着与去年相比订单量减少
如果要计算今年跟去年比销量下降最多的前5个客户，先计算今年和去年每个客户的销量，然后计算(去年销量-今年销量)最大的前5个客户
当回答数据查询问题时，请生成可以被执行的 SQL。只需要返回 SQL，不需要说明，解释和注释。
SQL 中不要包含注释
"""

db_host = "localhost"
db_user = "root"
db_passw = "sensors2017"
db_databese = "openai"


openai_key = '1df20dc702444ff2b28c06855d4b254b'
api_base = 'https://sensors-name01.openai.azure.com/'
engine = 'first-gpt35'

img_save_dir = '/Users/hushiwen/work/trade/imgs'
