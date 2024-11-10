modal = 100000000
laba_per_bulan = [0, 0, 1, 1, 5, 5, 5, 3]
total_laba = 0

for i, laba in enumerate(laba_per_bulan, start=1):
    laba_bulan = (laba / 100) * modal
    total_laba += laba_bulan    
    if i <= 2:
        print(f"Laba bulan ke-{i} sebesar: {int(laba_bulan)}")
    else:
        print(f"Laba bulan ke-{i} sebesar: {laba_bulan:.1f}")

print(f"Total laba adalah: {total_laba:.1f}")

