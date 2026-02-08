# Rumus: ukuran penampang kabel = (jarak x daya) / (daya hantar jenis x rugi tegangan x tegangan)

jarak = float(input("Jarak mesin dan panel distribusi dalam satuan meter: "))
daya = float(input("Masukkan daya dalam satuan Watt: "))
rugi = float(input("Tentukan rugi tegangan dalam satuan Volt: "))
tegangan = float(input("Tentukan tegangan dalam satuan Volt: "))

# Menggunakan konstanta daya hantar jenis tembaga (56)
rumus = (jarak * daya) / (56 * rugi * tegangan)

print("Anda perlu membeli kabel diameter: ", rumus, " mm")

#output
# Jarak mesin dan panel distribusi dalam satuan meter: 1000
# Masukkan daya dalam satuan Watt: 1000
# Tentukan rugi tegangan dalam satuan Volt: 10
# Tentukan tegangan dalam satuan Volt: 220
# Anda perlu membeli kabel diameter:  1.0 mm
