# -*-coding：utf-8-*-
import re
import json
with open("./data.json", "r", encoding="utf-8") as f:
    control_table = json.load(f)


def Transformation(string):
    """
    :param string: 带翻译的字符或语句
    :return: 返回翻译后的内容
    """
    newstring = ''
    for i in string:
        try:
            newstring = newstring+control_table['{}'.format(i)]
        except:
            newstring = newstring +i
    newstring = ''.join(re.findall('[\u4E00-\u9FA5,!，？?：:；；]', newstring))  # 对结果简单处理
    return newstring


if __name__ == '__main__':
    Transformation("搖")