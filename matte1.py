#2.1

m_ställning_idag = int(input("Mätarställning idag? "))
m_ställning_1år = int(input("Mätarställning för ett år sedan? "))

körda_mil = m_ställning_idag - m_ställning_1år

print("Antal körda mil: ",körda_mil)


liter_bensin = int(input("Antal liter bensin: "))

förbrukning = liter_bensin/körda_mil

print(f"Förbrukning per mil: {förbrukning}")



