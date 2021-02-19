from queue import LifoQueue as Stack

def ParanthesisChecker(s):
    d = {"]":"[", "}":"{", ")":"("}
    st = Stack()
    for i in s:
        if (st.empty() and i not in d) or i not in d:
            st.put(i)
        else:
            if i in d:
                if st.empty() or st.queue[-1] != d[i]:
                    return False
                else:
                    st.get()

    return st.qsize() == 0


s = input()
print(ParanthesisChecker(s))