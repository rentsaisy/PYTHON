import numpy as np

penjualan = np.array([
    [100, 150, 200],
    [80, 120,  160]
])

total_penjualan_wilayah = np.sum(penjualan, axis=0)
