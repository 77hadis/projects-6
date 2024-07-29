#%%


import networkx as nx
import random as rn
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import random
from numpy.lib.function_base import append 


#tedad afradi ke mikhay ro be n bede 
n=50
karmand=int(0.3*n)
ostad=int(0.25*n)
daneshj=n-(karmand+ostad)

#dorost kardane list afrad
l=[]
p=0
m=int (n/4)
for i in range(n+m):
    random=(rn.uniform(100,999))
    random=int(random)
    if random not in l:
        l.append(random)

for a in range (m+1):
    if len(l) > n:
        l.pop()

print(l)

p=0
for a in range (len(l)):
    e=l[p:p+1]
    e=str(e)
    p=p+1

print(l)

#yek list az adadi ke na'barabar hastand
#sakhte shod
#har shomare in list ro yek shakhs dar 
#nazar migirim


H=nx.Graph()
#n : tedade afrad
#l : liste esme afrad

# marahele sakhtan k 
# k yek adade tasadofi baraye tedade yal ha mibashad
payin=int(0.35*n)
payin=int(((payin)*(payin-1))/2)
bala=int(0.45*n)
bala=int(((bala)*(bala-1))/2)
print(payin,bala)

k= np.random.randint(payin,bala)
print(k)
k=int(k)

#shorue sakhte graph H
#be surate random, k ta yal ijad mishavad
H.add_nodes_from(l)
for a in range(k):
    a=rn.choice(l)
    b= rn.choice(l)
    H.add_edge(a,b)

#tabe tekrare rang
def tekrar(x,color):
    listrang=[]
    color=str(color)
    for i in range (x):
        listrang.append(color)
    return listrang

print(tekrar(5,'cyan'))

#ba tabe tekrar(x,color) ke sakhtam 
#ino mituni benevisi
#bedune un ham mishe
color_map=[]
for x in range (n) :
    if x in range (0,9):
        color_map = color_map + tekrar(1,'pink')
    if x in range (9,17):
        color_map.append('blueviolet')
    if x in range (17,25):
        color_map.append('orange')
    if x in range (25,37):
        color_map.append('deeppink')
    if x in range (37,50):
        color_map.append('paleturquoise')

print(color_map)

#entekhabe tasadofi 2 adad node az graph
# gharar dadan dar liste ghermeze bimari
H2=nx.Graph
H2=H


h2n= list(H.nodes)
print(h2n)

red1=rn.choice(h2n)
red2=rn.choice(h2n)
red_list=[red1,red2]
print('this is red list:' ,red_list)


neighbor_list=list(nx.all_neighbors(H2,red_list[0]))
neighbor_list=neighbor_list + (list(nx.all_neighbors
(H2,red_list[1])))
print('this is neighbor list:' ,neighbor_list)

#baraye inke azaye tekrari hazf shavand
for ozv in neighbor_list:
    if ozv in red_list:
        neighbor_list.remove(ozv)

for ozv in red_list:
    if ozv in neighbor_list:
        red_list.remove(ozv)


print(red_list)
print(neighbor_list)


color_map2=[]
d=np.random.randint(1,3)
for x in range (1):
    for v in H2:
        if v in red_list:
            color_map2.append('red')
        else:
            color_map2.append('gray')

#print(color_map2)

H3=H
color_map3=[]
for v in H3:
    if v in neighbor_list:
        color_map3.append('royalblue')
    elif v in red_list:
        color_map3.append('red')
    else:
        color_map3.append('gray')

#########################################

neighbor_list_abi=[]
len_nei= len(neighbor_list)
for i in range(len_nei):
    neighbor_list_abi.append(list(nx.all_neighbors(H,neighbor_list[i])))

print(len(neighbor_list_abi))
len_abi= len(neighbor_list_abi)


for i in range(len_abi):
    neighbor_list_abi= neighbor_list_abi + neighbor_list_abi[i]

for i in range (len_abi):
    neighbor_list_abi.pop(0)


print('this is neighbor list abi :', neighbor_list_abi)

#hazf ozv haye tekrari az list
list_komaki=[]
for i in neighbor_list_abi:
    if i not in list_komaki:
        list_komaki.append(i)

neighbor_list_abi=list_komaki
print(neighbor_list_abi)


##############################################

#hazfe ozv hayi ke tuye list ha moshabeh hastan
for ozv in neighbor_list_abi:
    if ozv in neighbor_list:
        neighbor_list_abi.remove(ozv)

for ozv in neighbor_list_abi:
    if ozv in red_list:
        neighbor_list_abi.remove(ozv)

for ozv in neighbor_list:
    if ozv in neighbor_list_abi:
        neighbor_list.remove(ozv)

for ozv in red_list:
    if ozv in neighbor_list_abi:
        red_list.remove(ozv)

print(neighbor_list_abi)

print('red list: ', red_list)

H4=H
color_map4=[]
for v in H4:
    if v in neighbor_list_abi:
        color_map4.append('royalblue')
    elif v in neighbor_list:
        color_map4.append('red')
    elif v in red_list:
        color_map4.append('yellow')
    else:
        color_map4.append('gray')
        
#nx.draw_networkx(H2, node_color= color_map2 , node_size= 400)

###############################################

neighbor_list_abi2=[]
len_nei= len(neighbor_list_abi)
for i in range(len_nei):
    neighbor_list_abi2.append(list(nx.all_neighbors(H,neighbor_list_abi[i])))

print(len(neighbor_list_abi2))
len_abi2= len(neighbor_list_abi2)


for i in range(len_abi2):
    neighbor_list_abi2= neighbor_list_abi2 + neighbor_list_abi2[i]

for i in range (len_abi2):
    neighbor_list_abi2.pop(0)

print('this is neighbor list abi2 :', neighbor_list_abi2)

#hazf ozv haye tekrari az list
list_komaki2=[]
for i in neighbor_list_abi2:
    if i not in list_komaki2:
        list_komaki2.append(i)

neighbor_list_abi2=list_komaki2
print(neighbor_list_abi2)

#hazfe ozv hayi ke tuye list ha moshabeh hastan
for ozv in neighbor_list_abi2:
    if ozv in neighbor_list_abi:
        neighbor_list_abi2.remove(ozv)

for ozv in neighbor_list_abi2:
    if ozv in neighbor_list:
        neighbor_list_abi2.remove(ozv)

for ozv in neighbor_list_abi2:
    if ozv in red_list:
        neighbor_list_abi2.remove(ozv)

for ozv in neighbor_list_abi:
    if ozv in neighbor_list_abi2:
        neighbor_list_abi.remove(ozv)

for ozv in neighbor_list:
    if ozv in neighbor_list_abi2:
        neighbor_list.remove(ozv)

for ozv in red_list:
    if ozv in neighbor_list_abi2:
        red_list.remove(ozv)


print(neighbor_list_abi2)
print('red list: ', red_list)

H5=H
color_map5=[]
for v in H5:
    if v in neighbor_list_abi2:
        color_map5.append('royalblue')
    elif v in neighbor_list_abi:
        color_map5.append('red')
    elif v in neighbor_list:
        color_map5.append('yellow')
    elif v in red_list:
        color_map5.append('green')
    else:
        color_map5.append('gray')
        
####################### 

neighbor_list_abi3=[]
len_nei= len(neighbor_list_abi2)
for i in range(len_nei):
    neighbor_list_abi3.append(list(nx.all_neighbors(H,neighbor_list_abi2[i])))

print(len(neighbor_list_abi3))
len_abi3= len(neighbor_list_abi3)


for i in range(len_abi3):
    neighbor_list_abi3= neighbor_list_abi3 + neighbor_list_abi3[i]

for i in range (len_abi3):
    neighbor_list_abi3.pop(0)


print('this is neighbor list abi3 :', neighbor_list_abi3)

#hazf ozv haye tekrari az list
list_komaki3=[]
for i in neighbor_list_abi3:
    if i not in list_komaki3:
        list_komaki3.append(i)

neighbor_list_abi3=list_komaki3
print(neighbor_list_abi3)

#hazfe ozv hayi ke tuye list ha moshabeh hastan
for ozv in neighbor_list_abi3:
    if ozv in neighbor_list_abi2:
        neighbor_list_abi3.remove(ozv)

for ozv in neighbor_list_abi3:
    if ozv in neighbor_list_abi:
        neighbor_list_abi3.remove(ozv)

for ozv in neighbor_list_abi3:
    if ozv in neighbor_list:
        neighbor_list_abi3.remove(ozv)

for ozv in neighbor_list_abi3:
    if ozv in red_list:
        neighbor_list_abi3.remove(ozv)

for ozv in neighbor_list_abi2:
    if ozv in neighbor_list_abi3:
        neighbor_list_abi2.remove(ozv)

for ozv in neighbor_list_abi:
    if ozv in neighbor_list_abi3:
        neighbor_list_abi.remove(ozv)

for ozv in neighbor_list:
    if ozv in neighbor_list_abi3:
        neighbor_list.remove(ozv)

for ozv in red_list:
    if ozv in neighbor_list_abi3:
        red_list.remove(ozv)


print(neighbor_list_abi3)
neighbor_list_black= neighbor_list[:1]

for i in range(1):
    neighbor_list.pop(i)


H6=H
color_map6=[]
for v in H6:
    if v in neighbor_list_abi3:
        color_map6.append('royalblue')
    elif v in neighbor_list_abi2:
        color_map6.append('red')
    elif v in neighbor_list_abi:
        color_map6.append('yellow')
    elif v in neighbor_list:
        color_map6.append('green')
    elif v in neighbor_list_black:
        color_map6.append('black')
    elif v in red_list:
        color_map6.append('gray')
    else:
        color_map6.append('gray')
         

###########################



neighbor_list_abi_end=[]
len_nei_end= len(neighbor_list_abi3)
for i in range(len_nei_end):
    neighbor_list_abi_end.append(list(nx.all_neighbors(H,neighbor_list_abi3[i])))

print(len(neighbor_list_abi_end))
len_abi_end= len(neighbor_list_abi_end)


for i in range(len_abi_end):
    neighbor_list_abi_end= neighbor_list_abi_end + neighbor_list_abi_end[i]

for i in range (len_abi_end):
    neighbor_list_abi_end.pop(0)

print('this is neighbor list abi_end :', neighbor_list_abi_end)

#hazf ozv haye tekrari az list
list_komaki_end=[]
for i in neighbor_list_abi_end:
    if i not in list_komaki_end:
        list_komaki_end.append(i)

neighbor_list_abi_end=list_komaki_end
print(neighbor_list_abi_end)

#hazfe ozv hayi ke tuye list ha moshabeh hastan
for ozv in neighbor_list_abi_end:
    if ozv in neighbor_list_abi3:
        neighbor_list_abi_end.remove(ozv)

for ozv in neighbor_list_abi_end:
    if ozv in neighbor_list_abi2:
        neighbor_list_abi_end.remove(ozv)

for ozv in neighbor_list_abi_end:
    if ozv in neighbor_list_abi:
        neighbor_list_abi_end.remove(ozv)

for ozv in neighbor_list_abi_end:
    if ozv in neighbor_list:
        neighbor_list_abi_end.remove(ozv)

for ozv in neighbor_list_abi_end:
    if ozv in red_list:
        neighbor_list_abi_end.remove(ozv)


for ozv in neighbor_list_abi3:
    if ozv in neighbor_list_abi_end:
        neighbor_list_abi3.remove(ozv)

for ozv in neighbor_list_abi2:
    if ozv in neighbor_list_abi_end:
        neighbor_list_abi2.remove(ozv)

for ozv in neighbor_list_abi:
    if ozv in neighbor_list_abi_end:
        neighbor_list_abi.remove(ozv)

for ozv in neighbor_list:
    if ozv in neighbor_list_abi_end:
        neighbor_list.remove(ozv)

for ozv in red_list:
    if ozv in neighbor_list_abi_end:
        red_list.remove(ozv)


print(neighbor_list_abi_end)
neighbor_list_black= neighbor_list_abi[:2]

for i in range(1):
    neighbor_list_abi.pop(i)


H7=H
color_map7=[]
for v in H7:
    if v in neighbor_list_abi_end:
        color_map7.append('royalblue')
    elif v in neighbor_list_abi3:
        color_map7.append('red')
    elif v in neighbor_list_abi2:
        color_map7.append('yellow')
    elif v in neighbor_list_abi:
        color_map7.append('green')
    elif v in neighbor_list:
        color_map7.append('black')
    elif v in neighbor_list_black:
        color_map7.append('gray')
    elif v in red_list:
        color_map7.append('gray')
    else:
        color_map7.append('gray')
         


#################################

#random_pos = nx.random_layout( H, seed=42)
#pos = nx.spring_layout(H, pos= fixx )
#random_pos = nx.random_layout( H2, seed=42)
#pos = nx.spring_layout(H2, pos= fixx )
#random_pos = nx.random_layout( H3, seed=42)
#pos = nx.spring_layout(H3, pos=  )

plt.figure(1)
nx.draw(H,node_color= color_map, edge_color = 'gray' ,width=1.2, pos=nx.spring_layout(H))
plt.figure(2)
nx.draw(H2,node_color= color_map2, edge_color='gray',width=1.2 , pos=nx.spring_layout(H2))
plt.figure(3)
nx.draw(H3,node_color= color_map3, edge_color='gray',width=1.2 , pos=nx.spring_layout(H3))
plt.figure(4)
nx.draw(H4,node_color= color_map4, edge_color='gray',width=1.2 , pos=nx.spring_layout(H4))
plt.figure(5)
nx.draw(H5,node_color= color_map5, edge_color='gray',width=1.2 , pos=nx.spring_layout(H5))
plt.figure(6)
nx.draw(H6,node_color= color_map6, edge_color='gray',width=1.2 , pos=nx.spring_layout(H6))
plt.figure(7)
nx.draw(H7,node_color= color_map7, edge_color='gray',width=1.2 , pos=nx.spring_layout(H7))

#,with_labels=True
plt.show()

