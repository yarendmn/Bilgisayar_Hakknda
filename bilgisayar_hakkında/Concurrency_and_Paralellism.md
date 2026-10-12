**💻 8 çekirdekli işlemcilere sahipken neden hâlâ yazılımlarımız donuyor?**



Selamlar,



Performans ve hızın biz yazılımcılar için ne kadar önemli olduğu aşikâr. Özellikle gömülü sistemler üzerinde çalışan veya sistem kaynaklarını mümkün olduğunca verimli kullanmak isteyenler için bu konu daha da önemli hale geliyor.



Peki perde arkasında neler oluyor?



Biraz **Concurrency \& Parallel Programming** kavramlarına bakalım.



🔹 **Concurrency (Eşzamanlılık)**



Concurrency, birden fazla işin aynı zaman aralığında ilerlemesinin yönetilmesidir.



Tek çekirdekli bir işlemcide bile birden fazla işin yürütülmesi mümkün olabilir. İşlemci, görevler arasında o kadar hızlı geçiş yapar ki kullanıcı açısından işler eş zamanlı gerçekleşiyormuş gibi görünebilir.



Örneğin:



\*\*Process A → Process B → Process A → Process C → Process B...\*\*



Burada önemli olan nokta, işlerin mutlaka fiziksel olarak aynı anda çalışması değil, birden fazla işin ilerlemesinin yönetilmesidir.



🔹 **Parallelism (Paralellik)**



Parallelism'de ise işler gerçekten aynı anda yürütülebilir.



Çok çekirdekli bir işlemcide farklı thread'ler farklı CPU çekirdeklerinde aynı anda çalışabilir. Bu nedenle concurrency ve parallelism birbirine yakın kavramlar olsa da aynı şey değildir.



Peki birden fazla thread aynı veriye aynı anda erişmeye çalışırsa?



İşte burada **Race Condition** problemi ortaya çıkabilir.



Örneğin iki thread'in aynı sayaç üzerinde aynı anda işlem yaptığını düşünelim. İki thread'in işlemleri birbirleriyle çakışırsa, programın sonucu thread'lerin hangi sırayla çalıştığına bağlı hale gelebilir. Bu da beklenmeyen sonuçlara yol açabilir.



Bu tür problemleri önlemek için **Synchronization (Senkronizasyon)**mekanizmalarından yararlanıyoruz.



🔒 **Lock (Kilit)**



Bir thread ortak bir kaynağın kritik bölümünde işlem yaparken erişimi geçici olarak sınırlandırır. Diğer thread'ler bu bölgeye erişmek için beklemek zorunda kalabilir.



🔐 **Mutex (Mutual Exclusion)**



Mutex, paylaşılan bir kaynağa aynı anda yalnızca bir thread'in erişmesini sağlayan bir senkronizasyon mekanizmasıdır. Mutex'in önemli özelliklerinden biri de sahiplik mantığıdır: mutex'i kilitleyen thread, normal kullanım modelinde kilidi kendisi serbest bırakır.



🎟️ **Semaphore**



Semaphore ise mutex'ten farklı olarak aynı anda birden fazla thread'in kaynağa erişmesine izin verebilir.



Örneğin bir kaynağı aynı anda en fazla 3 thread'in kullanmasına izin vermek istiyorsak:



Semaphore = 3



şeklinde düşünebiliriz.



Böylece ilk 3 thread kaynağı kullanabilirken, diğer thread'ler bir yer açılmasını bekler. Onlara bir yer açılınca da içeri girme hakkı kazanırlar.



Kısacası;



8 çekirdekli bir işlemciye sahip olmak, yazılımın otomatik olarak hızlı veya akıcı olacağı anlamına gelmiyor.



İşleri paralel çalıştırmak kadar, bu işlerin birbirleriyle nasıl iletişim kurduğu ve ortak kaynaklara nasıl eriştiği de önemli.



Yanlış tasarlanmış bir concurrency yapısı;



➡️ Race Condition

➡️ Deadlock

➡️ Gereksiz beklemeler

➡️ Senkronizasyon maliyeti

➡️ Hatta performans kaybı



gibi problemlere yol açabilir.



Yani çok çekirdekli sistemlerden gerçekten faydalanabilmek için mesele yalnızca "daha fazla çekirdek değil.



Asıl mesele, elimizdeki kaynakları doğru şekilde kullanabilmek.



\\#SoftwareEngineering #CPlusPlus #Concurrency #ParallelProgramming #Multithreading #Programming #ComputerScience #SoftwareDevelopment #EmbeddedSystems







