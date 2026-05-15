n = int(input("Enter hidden number: "))

while True:
    m = int(input("Guess the number: "))
    if m == n:
        print("Correct!")
        break  # tapdı, loop dayanır
    elif m > n:
        print("Too high!")
    else:
        print("Too low!")
        # Bu kod, kullanıcıdan gizli bir sayı girmesini ister ve ardından kullanıcıdan bu sayıyı tahmin etmesini ister. Kullanıcı doğru tahmin yapana kadar döngü devam eder. Her tahminin ardından, program tahminin gizli sayıdan yüksek mi, düşük mü yoksa doğru mu olduğunu bildirir. Doğru tahmin yapıldığında, "Correct!" mesajı görüntülenir ve döngü sona erer.