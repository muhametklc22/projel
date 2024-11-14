Port Tarayıcılar öncelikle Sızma Testi ve Bilgi Toplama için kullanılır. Esasen, iki nedenden dolayı bir ana bilgisayardaki açık bağlantı noktalarını arıyoruz. Sunucularımızın güvenli olmasını sağlamak veya başka birinin sunucularından yararlanmak. Gereksiz yere açılan bir bağlantı noktası, güvenlik açığı anlamına gelir ve güvenlik eksikliğini de beraberinde getirir.
Kütüphaneleri İçe Aktarma

    Belirli bir porttaki ana bilgisayara bağlantı denemelerimizde soket kullanılacaktır.
    İş parçacığı oluşturma, birden fazla tarama işlevini aynı anda çalıştırmamıza olanak tanır.
    Kuyruk, tek bir kaynak üzerindeki birden fazla iş parçacığının erişimini yönetmemize yardımcı olacak bir veri yapısıdır; bizim durumumuzda bunlar port numaraları olacaktır. İş parçacıklarımız aynı anda çalıştığından ve bağlantı noktalarını taradığından, her bağlantı noktasının yalnızca bir kez tarandığından emin olmak için kuyrukları kullanırız.
    IPy, hedefin bir IP adresi mi yoksa Etki Alanı mı olduğunu kontrol etmek için kullanılır. Ve eğer bir Etki Alanı ise IP'sini bulun.

Talimatlar

    Main.py dosyasını çalıştırın
    Hedef olarak sahip olduğunuz veya hackleme izniniz olan bir cihazın IP'sini seçin ve sahte IP adresi olarak rastgele ancak yine de geçerli bir adres seçin.
    Uygun bir mod seçin ve sonucu alacaksınız
