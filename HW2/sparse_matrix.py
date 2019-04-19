from sys import argv
import pandas as pd
import numpy as np

if len(argv) != 3:
	print('Usage: python3 sparse_matrix.py INPUT.csv OUTPUT.csv')
	exit(1)
data = pd.read_csv(argv[1], dtype={'ID':int,'QUESTION_INDEX':str,'ANS_ORDER':int,'ANS_NOTE':str}, encoding='utf-8')
data = data.sort_values(['ID','QUESTION_INDEX'])
out = []

#remove A0,A3,A6,A7,A13
option_n = {'A01':24, 'A02':7, 'A04':5, 'A05':3, 'A08':7, 'A09':9, 'A10':5, 'A11':5, 'A12':3, 'A14':3, 'B01':5, 'B02':5, 'B03':5, 'B04':5, 'B05':5, 'B06':5, 'B07':5}
end=False
it=data.iterrows()
row=next(it)[1]
while not end:
	#print(row)
	line = [row['ID']]
	assert row['QUESTION_INDEX'] == 'A01'
	for question_name in option_n:
		while row['QUESTION_INDEX']==question_name:
			#print(row)
			option = [0] * option_n[question_name]
			if row['QUESTION_INDEX'] == 'A05':
				if row['ANS_ORDER'] == 1:
					option[0] = 1
				elif row['ANS_ORDER'] == 2:
					child_n = row['ANS_NOTE'][0]
					if child_n.isdigit() and int(child_n) > 0:
						option[1] = 1
					else:
						option[2] = 1
			elif row['QUESTION_INDEX'] == 'A14':
				if row['ANS_ORDER'] < 4: #neither of them
					option[row['ANS_ORDER']-1]=1
			else:
				option[row['ANS_ORDER'] - 1] = 1
			try:
				row = next(it)[1]
			except:
				end = True
				break
		line+=option
	out.append(line)

df = pd.DataFrame(out)
df.to_csv(argv[2], index=False,
			header=['客戶ID'
			, '職業-軍警公教', '職業-資訊業', '職業-金融業', '職業-製造業', '職業-服務業', '職業-醫療服務業', '職業-學生', '職業-退休人士', '職業-餐飲旅館/旅遊業', '職業-量販店', '職業-政治性職務', '職業-營造/不動產業', '職業-進出口貿易', '職業-專業服務', '職業-民間匯兌業/虛擬貨幣產業', '職業-武器設備業', '職業-非營利機構', '職業-高單價物品之買賣或拍賣', '職業-當鋪/銀樓', '職業-學齡前', '職業-家管', '職業-待業中', '職業-自營商', '職業-其他'
			, '職務-基層職員', '職務-專業人員', '職務-技術人員', '職務-中階主管', '職務-高階主管', '職務-企業負責人', '職務-其他'
			, '學歷-國中(含以下)', '學歷-高中', '學歷-專科', '學歷-大學', '學歷-碩士/博士 '
			, '婚姻狀況-未婚', '婚姻狀況-已婚有子女', '婚姻狀況-已婚無子女'
			, '投資目的-閒置資金運用', '投資目的-節稅', '投資目的-儲備退休金', '投資目的-子女教育基金', '投資目的-追求長期投資報酬', '投資目的-資金調度', '投資目的-其他'
			, '投資基金來源-薪資收入', '投資基金來源-退休金', '投資基金來源-投資收益', '投資基金來源-繼承/贈與', '投資基金來源-借貸', '投資基金來源-出售資產', '投資基金來源-租賃收入', '投資基金來源-自營收入', '投資基金來源-其他'
			, '家庭年收入-50 萬元以下', '家庭年收入-50 萬元~100 萬元', '家庭年收入-100 萬元~300 萬元', '家庭年收入-300 萬元~500 萬元', '家庭年收入-500 萬元以上'
			, '家庭年支出-50 萬元以下', '家庭年支出-50 萬元~100 萬元', '家庭年支出-100 萬元~300 萬元', '家庭年支出-300 萬元~500 萬元', '家庭年支出-500 萬元以上'
			, '預計(單筆)投資金額-100 萬元以下', '預計(單筆)投資金額-100 萬元~300 萬元', '預計(單筆)投資金額-300 萬元以上'
			, '特殊身分客戶-70 歲以上', '特殊身分客戶-國中畢業以下', '特殊身分客戶-領有全民健康保險重大傷病證明'
			, '年齡-75 歲以上/20歲以下', '年齡-66~75歲', '年齡-56~65歲', '年齡-46~55歲', '年齡-20~45歲'
			, '曾經持有投資產品-現金、存款、定存、貨幣型基金與保本型基金', '曾經持有投資產品-債券、投資等級之債券基金', '曾經持有投資產品-外幣存款、非投資等級之債券基金、平衡型基金、新興市場債券基金', '曾經持有投資產品-股票、全球股票基金、歐美成熟國家股票基金、投資型保單', '曾經持有投資產品-新興市場股票基金、單一新興國家股票基金、衍生性商品'
			, '基金投資目的偏好-現金、存款、定存、貨幣型基金與保本型基金', '基金投資目的偏好-債券、投資等級之債券基金', '基金投資目的偏好-外幣存款、非投資等級之債券基金、平衡型基金、新興市場債券基金', '基金投資目的偏好-股票、全球股票基金、歐美成熟國家股票基金、投資型保單', '基金投資目的偏好-新興市場股票基金、單一新興國家股票基金、衍生性商品'
			, '備用金相當家庭開銷-無備用金', '備用金相當家庭開銷-3 個月以下', '備用金相當家庭開銷-介於3~6 個月', '備用金相當家庭開銷-介於6~9 個月', '備用金相當家庭開銷-超過9 個月'
			, '基金投資方式-不曾投資過', '基金投資方式-只買過貨幣型基金', '基金投資方式-定時定額', '基金投資方式-單筆(不含貨幣型基金)和定時定額兩者都有', '基金投資方式-單筆或私募基金'
			, '期望投資報酬率-1%~2%', '期望投資報酬率-3%~5%', '期望投資報酬率-6%~8%', '期望投資報酬率-9%~12%', '期望投資報酬率-12%以上'
			, '最大投資損失-1%~2%', '最大投資損失-3%~5%', '最大投資損失-6%~8%', '最大投資損失-9%~12%', '最大投資損失-12%以上'])
		

		


		
	