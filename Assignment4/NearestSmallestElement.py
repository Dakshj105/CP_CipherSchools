from queue import LifoQueue as Stack
import queue

def NearestSmallestElement(li):
    st = Stack()
    for i in range(len(li)):
        while(st.empty() == False and st.queue[-1] >= li[i]):
            st.get()
        if st.empty():
            print("_", end = ' ')
        else:
            print(st.queue[-1], end = " ")
        st.put(li[i])


li = list(map(int, input().split()))
NearestSmallestElement(li)