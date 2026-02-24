K = int(input())
"goku"

plata_total = 0
for dia in range(1, K + 1):
    plata_total += dia



oro_total = 0
for dia in range(2, K + 1, 2):
    oro_total += dia


desbalance = abs(oro_total - plata_total)
print(f"{oro_total} - {plata_total} = {desbalance}")
