import matplotlib.pyplot as plt
import pickle
import numpy as np

# %matplotlib inline
# plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
# plt.rcParams['image.interpolation'] = 'nearest'
# plt.rcParams['image.cmap'] = 'gray'
#
# %load_ext autoreload
# %autoreload 2

colors = ['r', 'g', 'b', 'orange', 'purple', 'gray', 'cyan', 'magenta', '#4134FF', '#FF7B9E']

def graphics(search):
    graphics = {'train_acc': {}, 'lr': {}}
    graph_name = ['train_acc', 'lr']
    # search = ["N3-E50-CS8-BS256-20200118-105812", "N4-E20-CS8-BS256-20200118-105659", "N4-E50-CS4-BS256-20200118-105518",
    #          "N4-E50-CS8-BS128-20200118-105259", "N4-E50-CS8-BS256-20200118-104919"]

    for g_n in graph_name:
        for i_s in search:
            with open("./search-" + i_s + "/" + g_n + ".bin", 'rb') as f:
                graphics[g_n][i_s] = pickle.load(f)



    for g_n in graph_name:
        for c_i, i_s in enumerate(search):
            plt.plot(graphics[g_n][i_s], colors[c_i])
        plt.xlabel('epoch')
        plt.ylabel(g_n)
        plt.legend(search, loc='upper left')
        plt.show()

def graphics_genotype(search, gen_file = "genotype"):
    genes = {}
    for i_s in search:
        with open("./search-" + i_s + "/" + gen_file + ".bin", 'rb') as f:
            genes[i_s] = pickle.load(f)
    weight_free_n = []
    weight_free_r = []
    weight_equipped_n = []
    weight_equipped_r = []

    PRIMITIVES_free = [
        'max_pool_3x3',
        'avg_pool_3x3',
        'skip_connect'
    ]

    PRIMITIVES_equipped = [
        'sep_conv_3x3',
        'sep_conv_5x5',
        'dil_conv_3x3',
        'dil_conv_5x5'
    ]

    # search = ["N3-E50-CS8-BS256-20200118-105812", "N4-E20-CS8-BS256-20200118-105659",
    #           "N4-E50-CS4-BS256-20200118-105518",
    #           "N4-E50-CS8-BS128-20200118-105259", "N4-E50-CS8-BS256-20200118-104919"]
    weight_type_graph = ['weight_free_n', 'weight_free_r', 'weight_equipped_n', 'weight_equipped_r']
    graphics = {'weight_free_n': {}, 'weight_equipped_n': {}, 'weight_free_r': {}, 'weight_equipped_r': {}}

    for g_i in weight_type_graph:
        for i_s in search:
            graphics[g_i][i_s] = []
            for gen_i in genes[i_s]:
                num_weight_free_n = 0
                num_weight_free_r = 0
                num_weight_equipped_n = 0
                num_weight_equipped_r = 0
                if g_i == 'weight_free_n':
                    for op in gen_i.normal:
                        if op[0] in PRIMITIVES_free:
                            num_weight_free_n += 1
                    graphics[g_i][i_s].append(num_weight_free_n)
                if g_i == 'weight_free_r':
                    for op in gen_i.reduce:
                        if op[0] in PRIMITIVES_free:
                            num_weight_free_r += 1
                    graphics[g_i][i_s].append(num_weight_free_r)
                if g_i == 'weight_equipped_n':
                    for op in gen_i.normal:
                        if op[0] in PRIMITIVES_equipped:
                            num_weight_equipped_n += 1
                    graphics[g_i][i_s].append(num_weight_equipped_n)
                if g_i == 'weight_equipped_r':
                    for op in gen_i.reduce:
                        if op[0] in PRIMITIVES_equipped:
                            num_weight_equipped_r += 1
                    graphics[g_i][i_s].append(num_weight_equipped_r)

    for g_n in weight_type_graph:
        for c_i, i_s in enumerate(search):
            plt.plot(graphics[g_n][i_s], colors[c_i], marker=c_i + 2)
        plt.xticks(np.arange(0, 50))
        plt.yscale('linear')
        plt.grid(True)
        plt.xlabel('epoch')
        plt.ylabel(g_n)
        plt.legend(search, loc='upper left')
        plt.show()