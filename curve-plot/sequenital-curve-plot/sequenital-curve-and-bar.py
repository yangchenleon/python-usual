import xlrd #  xlrd==1.2.0才支持xlsx
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator, xlabel

def get_time():
    filename = ".\\sequenital-curve\\附件10、叶面积指数（LAI）2012-2022年.xls"
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    times = sheet.col_values(0)
    return [int(i) for i in times[1:]]

def read_and_draw(filename, col_idx, unit, title, output_dir):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    col_cont = sheet.col_values(col_idx)
    data = [float(i) for i in col_cont[1:]]

    y = np.array(data)
    print(y.tolist(), type(y.tolist()[0]))
    x = np.array(range(len(y)))

    plt.close()
    plt.plot(x, y, linestyle='-.', color='g')

    times = get_time()
    plt.xticks(x, labels=times[0:len(x)])
    plt.xticks(rotation=60, fontsize=8)
    ax=plt.gca()
    x_major_locator=MultipleLocator(5)
    y_major_locator=MultipleLocator((max(y.tolist()) - min(y.tolist())) / 15)
    ax.xaxis.set_major_locator(x_major_locator) 
    ax.yaxis.set_major_locator(y_major_locator)

    plt.rcParams['figure.figsize'] = (9, 6)
    plt.rcParams['font.sans-serif']=['SimHei'] 
    plt.rcParams['axes.unicode_minus']=False
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.xlabel(f"年份-月份")
    plt.ylabel(f"{unit}")
    plt.title(f"{title}")  

    plt.savefig(fname=f".\{output_dir}\{title}.svg", format="svg")
    # plt.show()

def draw_bar():
    xlabels = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    x = np.array(range(len(xlabels)))
    y1 = [0.24775, 0.251583333, 0.258583333, 0.261545455, 0.203916667, 0.19975, 0.276, 0.232916667, 0.265166667, 0.249333333, 0.0995]
    y2 = [978637.5033, 740531.2417, 655650.005, 865856.245, 736481.25, 418837.5, 896343.7533, 676518.75, 598781.25, 892743.7367, 974250]
    y3 = [0.765666667, 0.765583333, 0.765583333, 0.765583333, 0.765666667, 0.765583333, 0.765583333, 0.765583333, 0.765666667, 0.765583333, 0.751557143]
    for y, fname in zip([y1, y2, y3], ["植被指数", "径流量", "叶面积指数"]):
        plt.close()
        plt.xticks(x, xlabels)  # 绘制x刻度标签
        plt.bar(x, y)
        

        plt.rcParams['figure.figsize'] = (9, 6)
        plt.rcParams['font.sans-serif']=['SimHei'] 
        plt.rcParams['axes.unicode_minus']=False
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.xlabel(f"年份")
        plt.ylabel(f"{fname}均值")
        plt.title(f"{fname}年均值柱状图")  

        plt.savefig(fname=f".\\sequenital-curve\\{fname}-柱状图.svg", format="svg")



if __name__ == '__main__':
    base_dir = ".\\sequenital-curve\\"
    # read_and_draw(base_dir+"附件10、叶面积指数（LAI）2012-2022年.xls", 4, "LAI", "叶面积指数：2012-2022年", base_dir)
    # read_and_draw(base_dir+"附件9、径流量2012-2022年.xlsx", 5, "径流量", "径流量：2012-2022年", base_dir)
    # read_and_draw(base_dir+"附件6、植被指数-NDVI2012-2022年.xls", 4, "NDVI", "植被指数：2012-2022年", base_dir)
    draw_bar()