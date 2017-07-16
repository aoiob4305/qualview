#-*- coding:utf-8 -*-

import codecs

def ansi2utf8(src_filename):
    convenc(src_filename, 'cp949', 'utf8')

def ansi2utf8_tofile(src_filename, des_filename):
    convenc_tofile(src_filename, 'ansi', des_filename, 'utf8')

def convenc_tofile(src_filename, src_encoding, des_filename, des_encoding):
    with codecs.open(src_filename, 'r', encoding=src_encoding) as file:
        lines = file.read()

    with codecs.open(des_filename, 'w', encoding=des_encoding) as file:
        file.write(lines)

    return des_filename

def convenc(src_filename, src_encoding, des_encoding):
    with codecs.open(src_filename, 'r', encoding=src_encoding) as file:
        lines = file.read()

    return lines.decode(src_encoding).encode(des_encoding) 


def parse2db(filename):
    with codecs.open(filename,'r',encoding='utf8') as f:
        rows = f.readlines()[3:]
        errors = []
        for row in rows:
            #?문자 발생시 구분기호로 변경
            row = row.replace('?','|')
            data = [x.strip() for x in row.split('|')][1:-1]
            if len(data) == 20:
                #수량 이상 시 이상표시
                try:
                    data[8] = int(data[8])
                except ValueError:
                    data[8] = '9999'
                errors.append(data)
                
                querySet = item.objects.filter(no = data[0])
                if querySet.exists() == False:
                    db = item(no = data[0],
                            group = data[1],
                            name = data[2],
                            description = data[3],
                            slot = data[4],
                            oldNo = data[5],
                            groupText = data[6],
                            safetyAmount = data[7],
                            amount = data[8],
                            buyAmount = data[9],
                            totalAmount = data[10],
                            itemType = data[11],
                            BUn = data[12],
                            price = float(data[13].replace(',','')),
                            totalPrice = float(data[14].replace(',','')),
                            Pe = data[15],
                            Plnt = data[16],
                            Sloc = data[17],
                            itemGroup = data[18],
                            itemUsage = data[19]
                    )
                    db.save()
            else:
                errors.append(data)

    return errors

def makedict(keys, values):
    dictdata = {}
    for num in range(0, len(values)):
        dictdata[keys[num]] = values[num]
    return dictdata

def parse(filename):
    with codecs.open(filename,'r',encoding='utf8') as f:
        rows = f.readlines()
        errors = []
        datas = []
        keys = [x.strip() for x in rows[1].split('|')][1:-1]
        for row in rows[3:]:
            #?문자 발생시 구분기호로 변경
            row = row.replace('?','|')
            data = [x.strip() for x in row.split('|')][1:-1]
            datas.append(makedict(keys, data))
    return datas