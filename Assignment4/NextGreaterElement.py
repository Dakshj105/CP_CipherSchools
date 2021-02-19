from queue import LifoQueue as Stack

def NextGreaterElement(li):
    st = Stack()
    st.put(li[0])
    ele = None
    for i in range(1, len(li)):
        next = li[i]
        if st.empty() == False:
            ele = st.get()
            while(ele < next):   
                print(str(ele) + "-->" + str(next))
                if st.qsize() == 0:
                    break
                ele = st.get()
            if ele > next:
                st.put(ele)

        st.put(next)

    while(st.empty() == False):
        ele = st.get()
        next = -1
        print(str(ele) + "-->" + str(next))


li = list(map(int, input().split()))
NextGreaterElement(li)