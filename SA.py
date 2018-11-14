
# coding: utf-8

# In[1]:


import numpy as np
import random
import matplotlib.pyplot as plt


# In[2]:


# 用邻接矩阵表示图 
# 随机生成一个无向图的邻接矩阵
# nodes代表城市的数量
nodes = 9
G = np.zeros([nodes,nodes])
for i in range(nodes-1):
    G[i,i+1:] = random.sample(range(1,nodes+20),nodes-1-i)

for i in range(nodes-1):
    G[:,i] = G[i,:]
    
print(G)


# In[3]:


init_path = np.array(range(nodes))


# In[4]:

# 根据前一条路径产生新的路径
def generatePath(pre_path): 
    # 随机选择2个节点，将路径中这2个节点间的节点顺序逆转，生成新的路径
    index1,index2 =random.sample(range(0,nodes),2)
    new_path = pre_path.copy()
    temp = new_path[index2]
    new_path[index2] = new_path[index1]
    new_path[index1] = temp
    return new_path

#generatePath(init_path)


# In[5]:


print('init_path ',init_path)


# In[6]:


def pathCost(path):
    nodeNum = len(path)
    cost = 0
    for i in range(nodeNum):
        node = path[i]
        next_node = path[(i+1)%nodeNum]
        cost = cost + G[node,next_node]
    return cost


# In[7]:


T = 1000
minT = 0.0001
path = init_path
r = 0.96
allCost = []
while T > minT:
    next_path = generatePath(path)
    dE = pathCost(next_path) - pathCost(path)
    if dE <= 0:
        # 新路径代价降低，接受
        path = next_path.copy()
    else:
        # 函数exp( dE/T )的取值范围是(0,1) ，dE/T越大，则exp( dE/T )也越大
        if np.exp(-dE/T) > random.random():
            path = next_path.copy()
            #print(np.exp(dE/T))
    
    T = r*T
    allCost.append(pathCost(path))


# In[10]:


plt.plot(allCost)
plt.xlabel('times')
plt.ylabel('cost of path')
plt.title('find best path')
plt.show()


# In[9]:


print('final path',path)

