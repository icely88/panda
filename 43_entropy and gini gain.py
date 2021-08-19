import numpy as np
# 进行数据整理
import pandas as pd
# 数据
import io
# 验证结果
from scipy import stats

data_str = output = io.StringIO('''编号,色泽,根蒂,敲声,纹理,脐部,触感,密度,含糖率,好瓜
1,青绿,蜷缩,浊响,清晰,凹陷,硬滑,0.697,0.46,是
2,乌黑,蜷缩,沉闷,清晰,凹陷,硬滑,0.774,0.376,是
3,乌黑,蜷缩,浊响,清晰,凹陷,硬滑,0.634,0.264,是
4,青绿,蜷缩,沉闷,清晰,凹陷,硬滑,0.608,0.318,是
5,浅白,蜷缩,浊响,清晰,凹陷,硬滑,0.556,0.215,是
6,青绿,稍蜷,浊响,清晰,稍凹,软粘,0.403,0.237,是
7,乌黑,稍蜷,浊响,稍糊,稍凹,软粘,0.481,0.149,是
8,乌黑,稍蜷,浊响,清晰,稍凹,硬滑,0.437,0.211,是
9,乌黑,稍蜷,沉闷,稍糊,稍凹,硬滑,0.666,0.091,否
10,青绿,硬挺,清脆,清晰,平坦,软粘,0.243,0.267,否
11,浅白,硬挺,清脆,模糊,平坦,硬滑,0.245,0.057,否
12,浅白,蜷缩,浊响,模糊,平坦,软粘,0.343,0.099,否
13,青绿,稍蜷,浊响,稍糊,凹陷,硬滑,0.639,0.161,否
14,浅白,稍蜷,沉闷,稍糊,凹陷,硬滑,0.657,0.198,否
15,乌黑,稍蜷,浊响,清晰,稍凹,软粘,0.36,0.37,否
16,浅白,蜷缩,浊响,模糊,平坦,硬滑,0.593,0.042,否
17,青绿,蜷缩,沉闷,稍糊,稍凹,硬滑,0.719,0.103,否''')

data = pd.read_csv(data_str)
data.set_index('编号', inplace=True)
print(data)

def entropy(data, att_name):
    '''
    data: 数据集
    att_name: 属性名
    '''
    levels = data[att_name].unique()
    # 信息熵
    ent = 0
    for lv in levels:
        pi = sum(data[att_name]==lv) / data.shape[0]
        ent += pi*np.log(pi)
    return -ent
# print('好瓜的信息熵:')
# entropy(data, '好瓜'）

def entropy_scipy(data, att_name):
    n = data.shape[0]
    values = data[att_name].value_counts()
    return stats.entropy(values/n)

print (entropy(data, '好瓜'))
print(entropy(data, '好瓜'))


def conditional_entropy(data, xname, yname):
    xs = data[xname].unique()
    ys = data[yname].unique()
    p_x = data[xname].value_counts() / data.shape[0]
    print(data[xname].value_counts() )
    print('p_x:',p_x)
    print('xs:',xs)

    ce = 0
    for x in xs:
        print('entropy' + str(x),entropy(data[data[xname]==x], yname))
        ce += p_x[x]*entropy(data[data[xname]==x], yname)
    return ce

print('触感条件下, 好瓜的信息熵:',conditional_entropy(data, '触感', '好瓜'))


def gain(data, xname, yname):
    en = entropy(data, yname)
    ce = conditional_entropy(data, xname, yname)
    return en - ce

print('触感的引入导致的信息增益:',gain(data, '触感', '好瓜'))


# data['testCol'] = 0
# print(data)
# print('testcol gain:',gain(data, 'testCol', '触感'))
# print('密度gain', gain(data, '密度', '触感'))
