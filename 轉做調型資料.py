import csv
import re
from pathlib import Path

tongmia = '《臺灣客家語常用詞辭典》內容資料(1100430).csv'

四縣聲調表 = {
    '24': 'ˊ',
    '33': '+',
    '11': 'ˇ',
    '31': 'ˋ',
    '55': '',
    '2': 'ˋ',
    '5': '',
    '53': 'ˋ',  # 畀 bi53
}

海陸聲調表 = {
    '53': 'ˋ',
    '55': '',
    '24': 'ˊ',
    '11': 'ˇ',
    '33': '+',
    '5': '',
    '2': 'ˋ',
}

大埔聲調表 = {
    '33': '+',
    '35': 'ˊ',
    '113': 'ˇ',
    '31': '^',
    '53': 'ˋ',
    '21': '^',
    '54': 'ˋ',
}

饒平聲調表 = {
    '11': 'ˇ',
    '55': '',
    '53': 'ˋ',
    '24': 'ˊ',
    '2': 'ˋ',
    '5': '',
}

詔安聲調表 = {
    '11': 'ˇ',
    '53': 'ˋ',
    '31': '^',
    '55': '',
    '24': 'ˊ',
    '43': 'ˋ',
}

造字表 = {
    '\ue72c': '𫟧',  # U+2B7E7
    '\ue0c7': '𫠛',  # U+2B81B
    '\ue711': '𫝘',  # U+2B758
    '\ue700': '𫣆',  # U+2B8C6
    '\ue725': '𬠖',  # U+2C816
    '\ue76f': '⿺皮卜',  # 還無Unicode
}


def uann(lomaji, pio):
    for tat, hing in pio.items():
        pattern = r'([a-z]+)' + tat + r'(?![\d])'
        lomaji = re.sub(
            pattern,
            lambda match: match.group(1) + hing,
            lomaji
        )
    return lomaji


def biang_zosii(row_dict):
    for col in row_dict:
        for k, v in 造字表.items():
            row_dict[col] = row_dict[col].replace(k, v)
    return row_dict


def main():
    with open(Path(__file__).parent / '調值資料_raw' / tongmia) as guanpun:
        with open(Path(__file__).parent / '調型資料' / tongmia, 'w') as sin:
            reader = csv.DictReader(guanpun)
            writer = csv.DictWriter(sin, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                row = biang_zosii(row)
                row['四縣腔音讀'] = uann(row['四縣腔音讀'], 四縣聲調表)
                row['南四縣腔音讀'] = uann(row['南四縣腔音讀'], 四縣聲調表)
                row['南四縣相關字詞音讀'] = uann(row['南四縣相關字詞音讀'], 四縣聲調表)
                row['海陸腔音讀'] = uann(row['海陸腔音讀'], 海陸聲調表)
                row['大埔腔音讀'] = uann(row['大埔腔音讀'], 大埔聲調表)
                row['大埔腔相關字詞音讀'] = uann(row['大埔腔相關字詞音讀'], 大埔聲調表)
                row['饒平腔音讀'] = uann(row['饒平腔音讀'], 饒平聲調表)
                row['饒平腔相關字詞音讀'] = uann(row['饒平腔相關字詞音讀'], 饒平聲調表)
                row['詔安腔音讀'] = uann(row['詔安腔音讀'], 詔安聲調表)
                row['詔安腔相關字詞音讀'] = uann(row['詔安腔相關字詞音讀'], 詔安聲調表)
                writer.writerow(row)

    with open(Path(__file__).parent / '調值資料_raw' / tongmia) as guanpun:
        with open(Path(__file__).parent / '調值資料_uni' / tongmia, 'w') as sin:
            reader = csv.DictReader(guanpun)
            writer = csv.DictWriter(sin, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                row = biang_zosii(row)
                writer.writerow(row)


if __name__ == '__main__':
    main()
