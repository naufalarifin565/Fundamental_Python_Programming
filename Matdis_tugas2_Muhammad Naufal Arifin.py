#1.3 nomor 10
# a) [¬p ∧ (p ∨ q)] → q
# b) [(p → q) ∧ (q → r)] → (p → r)
# c) [p ∧ (p → q)] → q
# d) [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r
def conjunction(p, q): #dan
    return p and q
def implication(p, q): #implikasi
    return (not p) or q
def disjunction(p, q): #atau
    return p or q
#10(a)
# a) [¬p ∧ (p ∨ q)] → q
print("p        q        ¬p      (p ∨ q)    ¬p ∧ (p ∨ q)    [¬p ∧ (p ∨ q)] → q")
for p in [True,False]:
    for q in [True,False]:
            negasi_p = not p
            pq = disjunction(p,q)
            dan = conjunction(negasi_p,pq)
            implikasi = implication(dan,q)
            print(f"{p}   {q}      {negasi_p}     {pq}         {dan}           {implikasi}")
print(f"dapat di simpulkan bahwa pernyataan di atas merupakan tautology karena hasil dari pernyataan di atas adalah true")
    
#10(b)
# b) [(p → q) ∧ (q → r)] → (p → r)
print("p        q       r     (p → q)      (q → r)    (p → q) ∧ (q → r)    (p → r)    [(p → q) ∧ (q → r)] → (p → r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = implication(p,q)
            qr = implication(q,r)
            dan = conjunction(pq,qr)
            pr = implication(p,r)
            hasil = implication(dan,pr)
            print(f"{p}   {q}   {r}   {pq}        {qr}              {dan}           {pr}               {hasil}")
print(f"dapat di simpulkan bahwa pernyataan di atas merupakan tautology karena hasil dari pernyataan di atas adalah true")
    
#10(c)    
# c) [p ∧ (p → q)] → q
print("p        q        (p → q)      p ∧ (p → q)     [p ∧ (p → q)] → q")
for p in [True,False]:
    for q in [True,False]:
        pq = implication(p,q)
        a = conjunction(p,pq)
        hasil = implication(a,q)
        print(f"{p}   {q}       {pq}          {a}                {hasil}")
print(f"dapat di simpulkan bahwa pernyataan di atas merupakan tautology karena hasil dari pernyataan di atas adalah true")

#10(d)    
# d) [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r    
print("p        q       r     (p ∨ q)      (p → r)    (p ∨ q) ∧ (p → r)    (q → r)    (p ∨ q) ∧ (p → r) ∧ (q → r)     [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
           pq = disjunction(p,q)
           pr = implication(p,r)
           dan_1 = conjunction(pq,pr)
           qr = implication(q,r)
           dan_2 = conjunction(dan_1,qr)
           hasil = implication(dan_2,r)
           print(f"{p}   {q}   {r}   {pq}        {pr}              {dan_1}           {qr}               {dan_2}                             {hasil}")
print(f"dapat di simpulkan bahwa pernyataan di atas merupakan tautology karena hasil dari pernyataan di atas adalah true")
    
#1.3 no 32
# Show that (p ∧ q) → r and (p → r) ∧ (q → r) are not logically equivalent

def conjunction(p, q): #dan
    return p and q
def implication(p, q): #implikasi
    return (not p) or q

print("p        q       r    (p ∧ q)  (p ∧ q) → r    (p → r)    (q → r)     (p → r) ∧ (q → r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = conjunction(p,q)
            implikasi_1 = implication(pq,r)
            pr = implication(p,r)
            qr = implication(q,r)
            implikasi_2 = conjunction(pr,qr)
            print(f"{p}   {q}   {r}  {pq}       {implikasi_1}         {pr}        {qr}         {implikasi_2}")
print(F"dapat di lihat pada tabel di atas bahwa kedua pernyataan tidak lah equivalent")