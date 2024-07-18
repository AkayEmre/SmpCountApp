import time

print(f"Güncel Saat: {time.strftime('%X')}")

def simple_counter(seconds):
    for i in range(seconds,0,-1):
        print(i)
        time.sleep(1)  # 1 saniye bekler

# Sayaç süresi (saniye)
counter_duration = int(input(f"Sayaç Süresini giriniz: "))


# Sayaç başlatma
simple_counter(counter_duration)

print("Süre Doldu")