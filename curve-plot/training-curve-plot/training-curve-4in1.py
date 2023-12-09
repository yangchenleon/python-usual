import xlrd #  xlrd==1.2.0才支持xlsx
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

def read_loss(filename, cols_index):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    losses = list()
    for c_idx in cols_index:
        col = sheet.col_values(c_idx)
        losses.append(col[2:])
    return losses

def draw_train_cruve(loss, output_dir, curve_name):
    epoch = np.array(range(1,502))
    loss = np.array(loss)
    plt.close()
    plt.style.use('bmh')
    colors = ['blue', 'green', 'red', 'purple']
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    plt.subplots_adjust(hspace=0.4)

    for i in range(1):
        for j in range(2):
            if i * 2 + j < len(curve_name):
                ax[i * 2 + j].plot(epoch, loss[i * 2 + j], color=colors[i * 2 + j])
                ax[i * 2 + j].xaxis.set_major_locator(MultipleLocator(50))
                ax[i * 2 + j].spines['top'].set_visible(False)
                ax[i * 2 + j].spines['right'].set_visible(False)
                ax[i * 2 + j].set_xlabel("Epoch")
                ax[i * 2 + j].set_ylabel("银行收入")
                ax[i * 2 + j].set_title(curve_name[i * 2 + j])
                ax[i * 2 + j].set_facecolor('#d9e2f3')

                max_idx = 499  # find index of maximum value in loss array
                max_epoch = epoch[max_idx]
                max_loss = loss[i * 2 + j][max_idx]
                ax[i * 2 + j].plot(max_epoch, max_loss, marker='o', markersize=4, color='black')
                ax[i * 2 + j].text(max_epoch * 0.7, max_loss * 0.9, f"({max_epoch}, {max_loss:.2f})", fontsize=12)  # add label with max value  # plot marker for max value
    
    plt.rcParams['font.sans-serif']=['SimHei'] 
    plt.rcParams['axes.unicode_minus']=False

    plt.savefig(fname=f".\{output_dir}\\问题二.svg", format="svg")

if __name__ == '__main__':
    # files = ["中间变量beta(完)", "200cm预测"]
    # cols_idx_list = [[6, 19, 14, 18], [3, 7, 11, 15]]
    # curve_names_list = [["PRNN", "tft", "TCN", "nbeats"], ["nbeats", "tft", "TCN", "PRNN"]]
    # output_dir = ["beta", "200cm"]
    # for file, cols_idx, curve_names in zip(files, cols_idx_list, curve_names_list, output_dir):
    #     filename = f".\\training-cruve\\{file}.xlsx"
    #     losses = read_loss(filename, cols_idx)
    #     for loss, curve_name in zip(losses, curve_names):
    #         # print(loss)
    #         draw_train_cruve(loss, f".\\training-cruve\\{output_dir}", curve_name)
    filename = ".\\training-curve-plot\\副本问题二.xlsx"
    cols_idx = [3, 7] #[6, 19, 14, 18]
    curve_names = ["LIGWO", "IMO"]# ["PRNN", "tft", "TCN", "nbeats"]
    losses = read_loss(filename, cols_idx)
    draw_train_cruve(losses, ".\\training-curve-plot\\200cm", curve_names)

