from queue import LifoQueue as Stack

def DuplicateParanthesis(s):
    st = Stack()
    for i in s:
        if i == ")":
            c = 0
            while(st.queue[-1] != "("):
                c += 1
                st.get()
            if c < 1:
                return "Duplicate Found"
            
        else:
            st.put(i)

    return "No Duplicate Found"


s = input()
print(DuplicateParanthesis(s))