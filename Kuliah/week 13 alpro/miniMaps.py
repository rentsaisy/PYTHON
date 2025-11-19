print("Program menentukan rute terdekat antar dua titik pada mini maps")

# Input jarak dari titik A ke titik lainnya
AB = int(input("Masukkan jarak A ke B: "))
AC = int(input("Masukkan jarak A ke C: "))
AD = int(input("Masukkan jarak A ke D: "))
BC = int(input("Masukkan jarak B ke C: "))
BD = int(input("Masukkan jarak B ke D: "))
CD = int(input("Masukkan jarak C ke D: "))

print("\n" + "=" * 60)
titik_awal = input("Masukkan titik awal (A/B/C/D): ").upper()
titik_tujuan = input("Masukkan titik tujuan (A/B/C/D): ").upper()

# Validasi input
if titik_awal not in ['A', 'B', 'C', 'D'] or titik_tujuan not in ['A', 'B', 'C', 'D']:
    print("Error: Titik harus A, B, C, atau D!")
elif titik_awal == titik_tujuan:
    print("Error: Titik awal dan tujuan tidak boleh sama!")
else:
    # Buat graf jarak antar titik
    jarak = {
        'A': {'B': AB, 'C': AC, 'D': AD},
        'B': {'A': AB, 'C': BC, 'D': BD},
        'C': {'A': AC, 'B': BC, 'D': CD},
        'D': {'A': AD, 'B': BD, 'C': CD}
    }
    
    # Algoritma Dijkstra untuk mencari jalur terpendek
    def dijkstra(graph, start, end):
        # Inisialisasi jarak tak terhingga untuk semua titik
        shortest = {node: float('inf') for node in graph}
        shortest[start] = 0
        previous = {}
        unvisited = list(graph.keys())
        
        while unvisited:
            # Cari titik dengan jarak terpendek
            current = min(unvisited, key=lambda node: shortest[node])
            
            if shortest[current] == float('inf'):
                break
                
            for neighbor, distance in graph[current].items():
                new_distance = shortest[current] + distance
                if new_distance < shortest[neighbor]:
                    shortest[neighbor] = new_distance
                    previous[neighbor] = current
            
            unvisited.remove(current)
        
        # Rekonstruksi jalur
        path = []
        current = end
        while current in previous:
            path.insert(0, current)
            current = previous[current]
        path.insert(0, start)
        
        return path, shortest[end]
    
    # Cari rute terpendek
    rute, jarak_total = dijkstra(jarak, titik_awal, titik_tujuan)
    
    # Tampilkan hasil
    print("\n" + "=" * 60)
    print("HASIL PENCARIAN RUTE TERDEKAT:")
    print("=" * 60)
    print(f"Dari titik {titik_awal} ke titik {titik_tujuan}")
    print(f"Rute terdekat: {' → '.join(rute)}")
    print(f"Total jarak: {jarak_total}")
    
    # Tampilkan detail rute
    if len(rute) > 2:
        print("\nDetail perjalanan:")
        for i in range(len(rute) - 1):
            from_point = rute[i]
            to_point = rute[i + 1]
            distance = jarak[from_point][to_point]
            print(f"  {from_point} → {to_point}: {distance}")    