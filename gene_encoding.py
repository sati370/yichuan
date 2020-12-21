import random

#基因编码，每一行产生一个随机数
def gene_encoding(pop_size, chrom_length):
    pop = []  # 2d
    for i in range(pop_size):
        temp = []
        for j in range(chrom_length):
            temp.append(random.randint(0, 1))
        pop.append(temp)
    return pop[:]