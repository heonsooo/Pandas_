import json

info= { 
    'Smasung': {
        "현재": '92,300',
        '과거': '62,200',
        'date': '2020-01-11'
        }
    , "LG": {
        "현재": '143,000',
        '과거': '73,000',
        'date': '2020-01-10'
    }
}

hyundai = {
    'hyundai': {
        "현재": '212,000',
        '과거': '163,000',
        'date': '2020-01-10'
            }
        }


print(info)

# _data.json 파일에 딕셔너리 형태로 info 저장
with open("stock_data.json", 'w',encoding='utf-8') as f:
    json.dump(info, f, indent='\t')

# 저장 된 _data.json 파일을 읽어오기. 
with open('stock_data.json', 'r', encoding='utf-8') as f:
    stock = json.load(f)

# 읽어 온 파일에 새로운 딕셔너리 업데이트
stock.update(hyundai)


print(stock)


# 업데이트 된 json 파일 저장
with open("stock_data.json", 'w',encoding='utf-8') as f:
    json.dump(stock, f, indent='\t')

# 업데이트 된 json 파일 읽기 
with open('stock_data.json', 'r', encoding='utf8') as f:
    f = f.read()
    my_data = json.loads(f)

print(json.dumps(my_data, indent=4))
