import matplotlib.pyplot as plt
import pickle

%matplotlib inline
plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

%load_ext autoreload
%autoreload 2

def graphics(search):
    graphics = {'train_acc': {}, 'lr': {}}
    graph_name = ['train_acc', 'lr']
    # search = ["N3-E50-CS8-BS256-20200118-105812", "N4-E20-CS8-BS256-20200118-105659", "N4-E50-CS4-BS256-20200118-105518",
    #          "N4-E50-CS8-BS128-20200118-105259", "N4-E50-CS8-BS256-20200118-104919"]

    for g_n in graph_name:
        for i_s in search:
            with open("./search-" + i_s + "/" + g_n + ".bin", 'rb') as f:
                graphics[g_n][i_s] = pickle.load(f)

    colors = ['r', 'g', 'b', 'orange', 'purple', 'gray', 'cyan', 'magenta', '#4134FF', '#FF7B9E']

    for g_n in graph_name:
        for c_i, i_s in enumerate(search):
            plt.plot(graphics[g_n][i_s], colors[c_i])
        plt.xlabel('epoch')
        plt.ylabel(g_n)
        plt.legend(search, loc='upper left')
        plt.show()