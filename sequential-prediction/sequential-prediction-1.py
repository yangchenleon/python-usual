import xlrd #  xlrd==1.2.0才支持xlsx
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

def timestamp_trans(timestamps):
    timelist = []
    for time in timestamps:
        time = int(time)
        year = 1900 + time // 365
        month = int((time % 365) / 30)

        if (month == 0):
            month = 12
            year -= 1

        timelist.append(str(year)+'-'+str(f'{month:02d}'))
    return timelist

def read_sheet_data(sheet):
    facts = sheet.col_values(3)
    times_f = sheet.col_values(2)

    preds = sheet.col_values(1)
    times_p = sheet.col_values(0)

    title = facts[0]
    
    return facts[1:], preds[1:], times_f[1:], times_p[1:], title

def draw_sheet(sheet, output_dir):
    num_pred = 24

    data = read_sheet_data(sheet)
    y1, y2 = np.array(data[0]), np.array(data[1][:num_pred])
    t1, t2 = np.array(data[2]), np.array(data[3][:num_pred])
    title = data[4]

    lx1, lx2 = timestamp_trans(t1), timestamp_trans(t2)
    lx2.insert(0, lx1[-1])

    y2 = np.insert(y2, 0, y1[-1])
    x1, x2 = np.array(range(1, len(y1) + 1)), np.array(range(len(y1) + 1, len(y1) + len(y2) + 1))
    
    plt.close()
    plt.plot(x1, y1, linestyle='-.', color='g')
    plt.plot(x2, y2, linestyle='--', color='blue')

    plt.xticks(np.array(range(len(y1) + len(y2))), labels=lx1+lx2)
    plt.xticks(rotation=60, fontsize=8)
    ax=plt.gca()
    x_major_locator=MultipleLocator(5)
    y_major_locator=MultipleLocator((max(y1.tolist() + y2.tolist()) - min(y1.tolist() + y2.tolist())) / 15)
    ax.xaxis.set_major_locator(x_major_locator) 
    ax.yaxis.set_major_locator(y_major_locator)

    plt.rcParams['figure.figsize'] = (9, 6)
    plt.rcParams['font.sans-serif']=['SimHei'] 
    plt.rcParams['axes.unicode_minus']=False
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.legend(["历年数据", "预测数据"], loc='upper right')
    plt.xlabel(f"年份-月份")
    plt.ylabel(f"{title}")
    plt.title(f"{sheet.name}预测结果")
    
    # # fig = plt.figure(figsize=(16, 10))
    # fig.savefig(fname=f".\{output_dir}\{sheet.name}.svg", format="svg")
    plt.savefig(fname=f".\{output_dir}\{sheet.name}.svg", format="svg")
    # plt.show()

def draw_excel(filename, output_dir):
    workbook = xlrd.open_workbook(filename)
    sheet_names = workbook.sheet_names()
    for sheet_name in sheet_names:
        sheet = workbook.sheet_by_name(sheet_name)
        draw_sheet(sheet, output_dir)

if __name__ == '__main__':
    base_dir = ".\\prediction-plot\\"
    sub_dir = ["200mm的时序预测", "降水量预测", "中间变量预测"]
    for dir in sub_dir:
        filename = f"{base_dir}\\data\\{dir}\\collection.xlsx"
        output_dir = f"{base_dir}\\svg-result\\{dir}"
        draw_excel(filename, output_dir)