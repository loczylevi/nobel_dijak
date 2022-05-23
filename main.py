#év;típus;keresztnév;vezetéknév

class Nobel_dijak:
  def __init__(self,sor):
    ev,tipus,keresztnev,vezeteknev = sor.strip().split(";")
    self.ev = int(ev)
    self.tipus = tipus
    self.keresztnev = keresztnev
    self.vezeteknev = vezeteknev
 
with open("nobel.csv","r",encoding="utf-8") as f:
  fejlec = f.readline()
  lista = [Nobel_dijak(sor) for sor in f]

milyen_dij = [sor.tipus for sor in lista if sor.keresztnev == "Arthur B." and sor.vezeteknev == "McDonald"][0]

print(f"3.feladat: {milyen_dij}")

irodalmi = [sor.keresztnev for sor in lista if sor.ev == 2017 and sor.tipus == "irodalmi"][0]
irodalmi2 = [sor.vezeteknev for sor in lista if sor.ev == 2017 and sor.tipus == "irodalmi"][0]

print(f"4.feladat: {irodalmi} {irodalmi2}")
vezteke = ""

nobel_beke = [sor for sor in lista if sor.ev > 1990 and sor.vezeteknev == ""]

print("5.feladat: ")

[print(f"      {sor.ev}: {sor.keresztnev}") for sor in nobel_beke]

curie = [sor for sor in lista if "Curie" in sor.vezeteknev or "Curie" in sor.keresztnev]

print("6.feladat: ")

[print(f"      {sor.ev} {sor.keresztnev} {sor.vezeteknev}({sor.tipus})") for sor in curie]

stat = dict()
print("7.feladat: ")
for sor in lista:
  tipus = sor.tipus
  stat[tipus] = stat.get(tipus,0) + 1
for tipus,darab in stat.items():
  print(f"         {tipus} - {darab} db.")

print("8.feladat: orvosi.txt")


with open("orvosi.txt","w",encoding="utf-8") as f2:
  orvosi = [sor for sor in lista if sor.tipus == "orvosi"]
  orvosi.sort(key=lambda x:x.ev) #reverse=True
  for sor in orvosi:
    f2.write(f"{sor.ev}: {sor.keresztnev} {sor.vezeteknev}\n")
  
  

