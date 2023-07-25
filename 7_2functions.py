def sayHello():
    print("Hello")

sayHello()   # Hello
sayHello()   # Hello
sayHello()   # Hello     burada def ile Hello bilgisini 3 kere ekrana yazdırırız

def sayHello(name):
    print("Hello "+ name)

sayHello("Bünyamin Ömer")    # Bünyamib Ömer
sayHello("Yunus Emre")       # Yunus Emre

# Burada sayHello yanındaki Paranteze ne yazarsak Hello ile birlikte onu da yazdırabiliriz

def sayHello(name = "user"):
    return "Hello "+ name

msg = sayHello("Çınar")             # bu kodda name ile user aynı şey olarak tanımlanmış sonra hello kelimesi üstüne + name yazmış en sayHello yazıp () içine istediği ismi yazar
msg = sayHello("Ada")               # burada iki tane msg tanımlandığı için en son yazılan msg geçerli olur yani Hello Ada yazdırır

print(msg)                # Hello Ada

def total(num1, num2):    # def total dedik ve bir sayıyı ekrana yazdıracağız num1 ve num2 dedik iki sayı alacağız ve bunları toplayıp ekrana yazdıracağız
    return num1 + num2    # en son yazdığım result çalışır çünkü result bir değişkendir değişkenlerde sürekli en son yazılan geçerli olur

result = total(10,20)
result = total(15,20)     # 15 num1 20 ise num2 diye anladım  
print(result)             # 35