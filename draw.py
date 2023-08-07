import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from datetime import datetime
import os
import config

def set_chinese_font():
    # 指定中文字体文件路径
    chinese_font = '/System/Library/Fonts/PingFang.ttc'  # 替换成你下载的中文字体文件路径
    
    # 加载中文字体
    prop = fm.FontProperties(fname=chinese_font)
    
    # 设置全局字体为中文字体
    plt.rcParams['font.family'] = prop.get_name()


def draw_pics(data_res, chart_type):
    set_chinese_font()
    img_fn = None
    if len(data_res) <= 1:
        return img_fn
    if len(data_res[0]) != 2:
        return img_fn
    
    bar_x = []
    bar_y = []
    for x, y in data_res:
        bar_x.append(x)
        bar_y.append(int(y))
    plt.bar(bar_x, bar_y, color='skyblue')
    plt.xticks(rotation=45)

    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    img_fn = f"img_chat_{current_time}.png"
    img_fn = os.path.join(config.img_save_dir, img_fn)
    plt.savefig(img_fn, dpi=300, bbox_inches='tight')

    return img_fn

if __name__ == "__main__":
    # 设置中文字体
    set_chinese_font()

    # 创建一个简单的绘图
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]
    plt.plot(x, y)
    plt.xlabel('X轴', fontsize=14)  # 可以通过fontsize参数设置中文的字体大小
    plt.ylabel('Y轴', fontsize=14)
    plt.title('示例图', fontsize=16)

    # 保存绘图为图片
    plt.savefig("sample_plot.png")

    plt.show()

