def biconditional_logic():
    print("=== Biconditional (Bi-implication) ===")
    p = True
    q = False
    # Bikondisional (p <-> q) terjadi ketika p dan q memiliki nilai yang sama
    biconditional = (p and q) or (not p and not q)
    print(f"p: {p}, q: {q}, p <-> q: {biconditional}")
    print("=====================================\n")

def inference():
    print("=== Inference ===")
    p = True
    q = False
    # Inferensi: Jika p -> q dan p benar, maka q juga harus benar
    implication = not p or q
    print(f"p: {p}, q: {q}, p -> q: {implication}")
    if p and implication:
        print(f"Dengan p benar, q harus: {q}")
    print("=====================================\n")

def argument():
    print("=== Argument ===")
    p = True
    q = False
    r = True
    # Argumen dalam logika, contoh sederhana:
    # Jika p -> q dan q -> r, maka p -> r
    premise_1 = not p or q     # p -> q
    premise_2 = not q or r     # q -> r
    conclusion = not p or r    # p -> r

    print(f"Premise 1 (p -> q): {premise_1}")
    print(f"Premise 2 (q -> r): {premise_2}")
    print(f"Conclusion (p -> r): {conclusion}")
    print("=====================================\n")

def axioms_theorems():
    print("=== Axioms, Theorems, Lemma, and Corollary ===")

    # Axiom: Pernyataan dasar yang diasumsikan benar tanpa pembuktian
    axiom = True # Contoh Aksioma yang selalu benar
    print(f"Axiom: {axiom} (selalu dianggap benar)")

    # Theorem: Pernyataan yang dibuktikan benar berdasarkan aksioma atau proposisi lain
    theorem = axiom and True # Teorema dibuktikan dari aksioma
    print(f"Theorem: {theorem} (berdasarkan aksioma)")

    # Lemma: Pernyataan pembantu yang digunakan untuk membuktikan teorema
    lemma = theorem # Lemma adalah bagian pembuktian teorema
    print(f"Lemma: {lemma} (digunakan untuk membantu membuktikan teorema)")
    
    # Corollary: Pernyataan yang mengikuti langsung dari teorema
    corollary = theorem # Corollary adalah konsekuensi langsung dari teorema
    print(f"Corollary: {corollary} (konsekuensi langsung dari teorema)")
    print("=====================================\n")
   
if __name__ == "__main__":
    biconditional_logic()
    inference()
    argument()
    axioms_theorems()