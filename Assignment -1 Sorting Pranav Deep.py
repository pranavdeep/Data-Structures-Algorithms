#!/usr/bin/env python
# coding: utf-8

# In[120]:


import math


# In[121]:


#Insertin Sort
def InsertionSort(array):
    for i in range(1,len(array)):
        current = array[i]
        j = i-1
        while(j>=0 and array[j]>current):
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = current

    #print(array)
    


# In[122]:


def Merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
   
    L = [None] * (n1) 
    R = [None] * (n2) 
   
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    
    i = 0    
    j = 0    
    k = l
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
   
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  


# In[123]:



import math
def MergeSort(array,p,r):
    if (p<r):
        q = math.floor((p+r)/2)
        #print(q)
        MergeSort(array,p,q)
        #print(array)
        MergeSort(array,q+1,r)
        #print(array)
        Merge(array,p,q,r)
        


# In[124]:


def MaxHeapify(arr, n , i): 
    largest = i   
    l = 2 * i + 1     #(left sub tree index)
    r = 2 * i + 2     #(right sub tree index)
  
    # If left child of root exists and is greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # If right child of root exists and is  greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
     
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  #Similar to swap a,b=b,a (Python easy swap style) 
        MaxHeapify(arr, n, largest)
        
def HeapSort(arr): 
    n = len(arr) 
    for i in range(n // 2 - 1, -1, -1): 
        MaxHeapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # Easy swap. Remember this works ony in python. Write swap() a swap function for other languages
        MaxHeapify(arr, i, 0) 


# In[129]:


print("Enter List of numbers")
list1=list(map(int,input().split())) #List without knowing the size of n
list2 = list1.copy()



# In[130]:


print("Enter 1 for Insertion sort")
print("Enter 2 for Merge sort")
print("Enter 3 for Heap sort")
temp = int(input())
#print(q)


# In[131]:


if(temp==1):
    InsertionSort(list1)
    print("Insertion Sort")
elif (temp ==2):
    MergeSort(list1,0,len(list1)-1)
    print("Merge Sort")
elif(temp==3):
    print("Heap Sort")
    HeapSort(list1)
    
print("Original List = ",list2)
print("Sorted List = ",list1)
        


# In[ ]:





# In[ ]:




