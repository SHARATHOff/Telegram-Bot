''''l1 = [9,10,7]

for i in l1:
    true = 0
    temp = i
    for j in l1 :
        if temp<=j:
            true+=1
        else:
            pass

    if true==len(l1):
        print(i ,' is min')
    else:
        pass
'''

def A(n):
    if n==1:
        print('krishna')
    A()
    print("sharath")

import  sys
sys.setrecursionlimit(10000)
def hanoi( N , source , temp , target):
    if N == 0:
        return                                                                                          # 3 , a,b,c
        #print(f'the disk {N} is moved from {source} to {target}')                                      # 3-1=2 ,a,c,b
    else:                                                                                               #
        if N == 1:
            print(f'the disk {N} is moved from {source} to {target} ')

        else:
            hanoi(N-1,source,target,temp)
            print(N)
            print(f'the disk {N} is moved from {source} to {target}  ')

            hanoi(N-1,temp,source,target)

n = 3
#hanoi(n,'A','B','C')
import threading
import  time

def A():
    while True:
        c = "hello"
        print(c)
        time.sleep(1)
def B():
    while True:
        c ='hai'
        print(c)
        time.sleep(1)

#t1 = threading.Thread(target=A)
#t2 = threading.Thread(target=B)

#t1.start()
#t2.start()



from googlesearch import search

from googlesearch import search


def google_search(query):
    try:
        search_results = search(query)
        return search_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


while (True):
    query = input("Enter your query :")
    results = google_search(query)
    if results:
        print("Search Results:")
        for result in results:
            print(result)
    elif (query == "a"):
        break
    else:
        print("Inavalid prompt")





