# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:18:44 2022

@author: lxpperfect
"""
import time
import os
import copy

file_iname = 'input.txt'
file_oname = 'output.txt'


def get_data(file_iname):
    f = open(file_iname,'r')
    txt = []
    for line in f.readlines():
        curline=line.strip().split(",")
        txt.append(curline[:])
    m, ele_A, n, ele_B = int(txt[0][0]), txt[1], int(txt[2][0]), txt[3]
    ele_A = list(map(float, ele_A))
    ele_B = list(map(float, ele_B))
    if (len(ele_A) > 200) | (len(ele_B) > 200):
            print("error! ")
    f.close()
    ele_A = ele_A.sort(cmp=None, key=None, reverse=False)
    ele_B = ele_B.sort(cmp=None, key=None, reverse=False)
    return ele_A, ele_B



def write_ans(file_name):
    f = open(file_name,'w')
    for i in range(len(allocations)):
        idx = allocations[i]
        an_A = ele_A[idx]
        f.writelines("%d,%d,%d\n" % (i+1, idx+1, an_A))
    f.close()
    
#bucket = [-1 for i in range(len(ele_B))]
ans = 10000
cut_off = 0
def cut_iter_all(pos, bucket, tmp_ans, A, B):
    #pos: 当前遍历的产品
    #A:部件材料； B:产品
    global ans, allocations,cut_off
    if tmp_ans > ans:
        cut_off += 1
        return
    
    if max(B) > max(A):
        cut_off += 1
        return
    
    if pos == len(B):
        if tmp_ans < ans:
            ans = tmp_ans
            allocations = copy.deepcopy(bucket)
        return
    
    if pos < len(B):
        b= B[pos]
        for i in range(len(A)):                
            if A[i] >= b:
                A[i] -= b
                bucket[pos] = i

                if A[i]+b == ele_A[i]:
                    tmp_ans += ele_A[i]

                cut_iter_all(pos + 1, bucket, tmp_ans ,A, B)

                if A[i] + B[pos] == ele_A[i]:
                    tmp_ans -= ele_A[i]

                bucket[pos] = -1
                A[i] += b

if __name__ == '__main__':
    ele_A, ele_B = get_data(file_iname)
    A = copy.deepcopy(ele_A)
    B = copy.deepcopy(ele_B)
    bucket = [-1 for i in range(len(B))]
    cut_iter_all(0, bucket, 0, A, B)
    end = time.time()
    write_ans(file_oname)
