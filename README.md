# Компьютерные сети (семинары)

## Урок 7. NAT. GRE

1. Cтраницы по HTTP и HTTPS по публичному адресу Router3 в веб-браузере клиентов Office3 (с РС1 и РС0)

    PC0: port 80
    <img src="hw-7/pc0_80.png" alt="pc0-80" widt="1024">

    PC0: port 443
    <img src="hw-7/pc0_443.png" alt="pc0-443" widt="1024">

    PC1: port 80
    <img src="hw-7/pc1_80.png" alt="pc1-80" widt="1024">

    PC1: port 443
    <img src="hw-7/pc1_443.png" alt="pc1-443" widt="1024">

    Вывод show ip nat translation c Router1

    <img src="hw-7/r1_nat_transl.png" alt="r1_nat" widt="1024">

2. Трейс с Laptop0 до Server2

    <img src="hw-7/gre.png" alt="trace" widt="1024">

3. Публичный IP до и после подключения через VPN

    <img src="hw-7/pub_ip.png" alt="ip" widt="1024">

    Вывод команды ip addr на сервере:

     <img src="hw-7/ip-a-after_ovpn.png" alt="ip a" widt="1024">

     Вывод команды ifconfig на клиенте:

     <img src="hw-7/client-int.png" alt="ip a" widt="1024">
