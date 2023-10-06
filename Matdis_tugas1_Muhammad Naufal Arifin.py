#1.1 nomor 37
def conjunction(p, q): #dan
  return p and q
def implication(p, q): #implikasi
  return not p or q
def disjunction(p, q): #atau
    return p or q
def bi_implication(p, q): # bi-implikasi
  return p == q
  
# p → (¬q ∨ r)
# b) ¬p → (q → r)
# c) (p → q) ∨ (¬p → r)
# d) (p → q) ∧ (¬p → r)
# e) (p ↔ q) ∨ (¬q ↔ r)
# f ) (¬p ↔ ¬q) ↔ (q ↔ r)

# 37(A)
print("p       q       r    ¬q ∨ r    p → (¬q ∨ r) ")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            qr = disjunction(not q,r)
            a = implication(p,qr)
            print(f"{p}   {q}   {r}    {qr}       {a}")


# 37(B)
print("¬p       q       r     q → r   ¬p → (q → r) ")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            qr = implication(q,r)
            a = implication(not p,qr)
            print(f"{p}   {q}   {r}    {qr}       {a}")

    
# 37(C)
print("p       q       r     p → q   ¬p → r   (p → q) ∨ (¬p → r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = implication(p,q)
            pr = implication(not p,r)
            a = disjunction(pq,pr)
            print(f"{p}   {q}   {r}    {pq}       {pr}         {a}")


# 37(D)
print("p       q       r     p → q   ¬p → r   (p → q) ∨ (¬p → r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = implication(p,q)
            pr = implication(not p,r)
            a = conjunction(pq,pr)
            print(f"{p}   {q}   {r}    {pq}       {pr}         {a}")
            
            
# 37(E)
print("p       q       r     p <=> q   ¬q <=> r   (p ↔ q) ∨ (¬q ↔ r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = bi_implication(p,q)
            qr = bi_implication(not q,r)
            a = disjunction(pq,qr)
            print(f"{p}   {q}   {r}    {pq}       {qr}         {a}")
            
            
# 37(F)
print("p       q       r     ¬p <=> ¬q   q <=> r   (¬p↔¬q)↔(q↔r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = bi_implication(not p,not q)
            qr = bi_implication(q,r)
            a = bi_implication(pq,qr)
            print(f"{p}   {q}   {r}    {pq}       {qr}         {a}")

#1.1 nomor 42 
# What is the value of x after each of these statements is
# encountered in a computer program, if x = 1 before the
# statement is reached?
# a) if x + 2 = 3 then x := x + 1
        """hasil yang akan di keluarkan adalah 2
        -soal menjelaskan bahwa x = 1
        -kondisi percabangan x + 2 = 3 setelah dimasukan x = 1 menjadi True
        -program akan mengeksekusi nilai x = 1 ke x := x + 1 
        -hasil x = 2
        """
# b) if (x + 1 = 3) OR (2x + 2 = 3) then x := x + 1
        """program tidak akan mengeluarkan hasil, karena kedua pernyataan di atas bernilai false.
        """
# c) if (2x + 3 = 5) AND (3x + 4 = 7) then x := x + 1
        """hasil dari program di atas adalah 2, karena kedua pernyataan di atas bernilai True
        sehingga program akan di eksekusi dan menampilkan angka 2 sebagai hasil. 
        """
# d) if (x + 1 = 2) XOR (x + 2 = 3) then x := x + 1
        """program tidak akan menampilkan hasil, walaupun kedua kondisi bernilai True, tetapi operator Xor(Exclusive Disjunction)
        ini hanya akan bernilai True jika salah satu dari kedua pernyataan bernilai True.
        """
# e) if x < 2 then x := x + 1
        """hasil dari program adalah 2, karena pernyataan di atas bernilai benar, bahwa x = 1 bernilai lebih kecil dari pada 2
        sehingga program akan di eksekusi dan menampilkan angka 2 sebahai hasil.
        """
            