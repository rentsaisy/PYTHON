def propositional_logic():
    print("====================================\n")
    print("=== Propositional Logic ===\n")
    p = True # Contoh Proposisi p
    q = False # Contoh Proposisi q
    print(f"Proposisi p: {p}") # p adalah True
    print(f"Proposisi q: {q}") # q adalah False
    print(f"Not p: {not p}") # Negasi dari p
    print(f"p AND q: {p and q}") # Konjungsi 
    print(f"p OR q: {p or q}") # Disjungsi
    print("=====================================\n")
    
def conjunction():
    print("=== Conjunction ===")
    p = True
    q = False
    print(f"p : {p}, q : {q}, p AND q: {p and q}")  # Menampilkan hasil Konjungsi 
    print("=====================================\n")

def disjunction():
    print("=== Disjunction ===")
    p = True
    q = False
    print(f"p : {p}, q : {q}, p OR q: {p or q}")  # Menampilkan hasil Disjungsi 
    print("=====================================\n")
        
def implication():
    print("=== Implication ===")
    p = True
    q = False
    print(f"p : {p}, q : {q}, p -> q: {not p or q}")  # Menampilkan hasil Implikasi 
    print("=====================================\n") 
# before (1)    
def biconditional():
    print("=== Biconditional ===")
    p = True
    q = False
    print(f"p : {p}, q : {q}, p <-> q: {(p and q) or (not p and not q)}")  
    print("=====================================\n")  
# after (1)  
def biconditional():
    print("=== Biconditional ===")
    p = False
    q = True
    print(f"p : {p}, q : {q}, p <-> q: {(p and q) or (not p and not q)}")  
    print("=====================================\n")  
# before (2)        
def exclusive_disjunction():
    print("=== Exclusive Disjunction ===")
    p = True
    q = False
    # Disjungsi Eksklusif (XOR)
    xor_result = (p or q) and not (p and q) # XOR operator
    print(f"p : {p}, q : {q}, p XOR q: {xor_result}") # Menampilkan hasil XOR
    print("=====================================\n")
# after (2)
def exclusive_disjunction():
    print("=== Exclusive Disjunction ===")
    p = False
    q = True
    # Disjungsi Eksklusif (XOR)
    xor_result = (p or q) and not (p and q) # XOR operator
    print(f"p : {p}, q : {q}, p XOR q: {xor_result}") # Menampilkan hasil XOR
    print("=====================================\n")

def combine_propositions():
    print("=== Combine Propositions ===")
    p = True
    q = False
    r = True
    # Mengggunakan operator logika
    combined = (p and q) or (not r)  # Kombinasi beberapa proposisi
    print(f"p : {p}, q : {q}, r : {r}, (p AND q) OR (NOT r): {combined}") 
    print("=====================================\n")
        
def truth_table():
        print("=== Truth Table ===")
        print("p\tq\tp AND q\t\tp OR q\t\tNot p\t\tp -> q\t\tp <-> q")
        for p in [True, False]:
            for q in [True, False]:
                conjunction = p and q
                disjunction = p or q
                implication = not p or q
                biconditional = (p and q) or (not p and not q)
                print(f"{p}\t{q}\t{conjunction}\t\t{disjunction}\t\t{not p}\t\t{implication}\t\t{biconditional}")
        print("===========================================================================\n")

if __name__ == "__main__":
        
        # Course_contract()
        propositional_logic()

        conjunction()
        disjunction()
        implication()
        biconditional()
        
        exclusive_disjunction()
        combine_propositions()

        truth_table()

