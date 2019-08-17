w = input()
s = 0
while True:
    st = input()
    if st == "END_OF_TEXT": break
    s += st.lower().split().count(w)
print(s)
    

