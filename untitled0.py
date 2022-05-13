# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:18:44 2022

@author: lxpperfect
"""
import time
import os
import numpy

file_name = 'input.txt'

f = open(file_name,'r')
txt = []
for line in f.readlines():
    curline=line.strip().split(",")
    txt.append(curline[:])
m, ele_A, n, ele_B = int(txt[0][0]), txt[1], int(txt[2][0]), txt[3]
ele_A = list(map(float, ele_A))
ele_B = list(map(float, ele_B))

if (len(ele_A) > 200) | (len(ele_B) > 200):
    print("error! ")
else:return 

def iter_all(pos, bucket, A,  B):
    global ans,step, methods_count, file_name
    if False not in already_arr:
        methods_count += 1
        temp_ans = 0
        for i in range(len(bucket)):
            if bucket[idx]:
                temp_ans += A[i]
        if temp_ans < ans:
            print("Update ans:{} to {}. Traveled methods:{}. ".format(ans, temp_ans,methods_count))
            print("Step is {}.".format(step))
            ans = temp_ans
            write_ans(step, file_name)
            return
    if pos < len(B):
        b = B[pos]
        for i in range(len(A)):
            if b + bucket[i] <= A[i]:
                bucket[i] += b
                already_arr[pos] = True
                step += [pos + 1, i + 1, A[i]]
                iter_all(pos + 1, bucket, A, B)
                step = step[ :-3]
                already_arr[pos] = False
                bucket[i] -= b


file_name = 'output.txt'

def write_ans(step, file_name):
    f = open(file_name,'w')
    f.writelines(step)
    f.close()
    
already_arr[n] = False
def cut_iter_all(pos,bucket, temp_ans, A, B):
    global ans,step,methods_cont,cut_off,file_name
    if temp_ans > ans:
        cut_off += 1
        return
    if False not in already_arr:
        methods_count = 1
        if temp_ans < ans:
            print("update ans:{} to {}. Traveled methods:{}. Cut off times:{}. ".format(ans, temp_ans, methods_count, cut_off))
            #print("step is {}.".format(step))
            ans = temp_ans
            write_ans(step, file_name)
            return
    if pos < len(B):
        b= B[pos]
        for i in range(len(A)):
            if b + bucket[i] <= A[i]:
                bucket[i] =b
                if bucket[i] == b:
                    temp_ans += A[i]
                already_arr[pos] = True
                step += [pos + 1, i + 1, A[i]]
                cut_iter_all(pos + 1, bucket, temp_ans ,A, B)
                step = step[ :-3]
                already_arr[pos] = False
                bucket[i] -= b
            if bucket[i] == 0:
                temp_ans -=A[i]

init_data(sort_arr=True,name="cut_iter_sorted")
start = time.time()
cut_iter_all(0,bucket, 0, A, B)
print("consume:{}. ".format(time.time() - start))
print( "Total Traveled methods:{}.".format(methods_count))
