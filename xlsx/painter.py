from PIL import Image
import xlsxwriter


# 颜色转换
def fnColorEx(value):
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = "#"
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return (a1, a2, a3)


# 路径
path = 'a.jpg'
img = Image.open(path)
imgL = img.convert("P").convert("RGB")

pix = imgL.load()

w, h = imgL.size
workbook = xlsxwriter.Workbook('hjy.xlsx')  # 新建excel表

worksheet = workbook.add_worksheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）

for j in range(w):
    for i in range(h):
        color_cell = fnColorEx(pix[j, i])
        # 添加样式
        sty = workbook.add_format({'bg_color': '{}'.format(color_cell)})
        # 写入
        worksheet.write(i, j, '', sty)
        # 设置行高
        worksheet.set_row(i, 1)
# 设置列宽
worksheet.set_column(0, w - 1, 0.1)

workbook.close()
