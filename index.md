# Python
Aby mohly automatizované testy běžet, na stroji musí být nainstalován Python, a to jak na localu, tak na serveru. Python je možno stáhnout na oficiálních stránkách https://www.python.org/downloads/. V instalačním průvodci je nutno zvolit volbu instalace pro všechny uživatele a také přidat python do environment variables, díky čemuž bude možno spouštět python scripty jednoduše příkazem:
 ```python [path to file]/[filename].py```

Rovněž to usnadní konfiguraci integračního serveru.

## Moduly

Aby byly testy funkční, je třeba doinstalovat níže uvedené moduly, které nejsou součásti standardního balíčku:

* **selenium**
  * základní modul pro psaní automatizovaných testů pomocí nástroje Selenium
* **webdriver_manager**
  * modul, který usnadňuje správu webdriverů tím, že patřičný driver automaticky vyhledá a stáhne
* **ddt**
  * modul pro Data Driven Testing, s jehož pomocí lze testům předávat různé sady dat
* **html-testRunner**
  * rozšíření pro standardní modul unittest (základní modul pro unit testing), který umožňuje vytvářet customizovatelné test reporty v html formátu

Moduly se nainstalují pomocí nástroje pip, který modul dle jeho názvu automaticky vyhledá a nainstaluje i se všemi závislostmi. Moduly je možno nainstalovat dvěma způsoby:

1. jednotlivě pomocí příkazu 

```pip install [název modulu]```

2. hromadně pomocí textového souboru, jenž obsahuje názvy modulů

```pip install -r [path to file]/[filename].txt```

Naneštěstí, modul ```html-testRunner``` je třeba ručně upravit. Modul v základu neumožňuje kombinovat reporty (mít jeden test report z více test class). Tato funkcionalita byla implementována v separátní branchi, která však nebyla zmergována s masterem. Zdrojový kód je umístěn zde https://github.com/oldani/HtmlTestRunner/pull/32/files. 

# Struktura projektu
![základní struktura projektu](/assets/img/index_strukturaProjektu.png)

## main.py
Základní modul, který slouží ke spuštění automatizovaných testů. Probíhají zde následující činnosti:

1. Před spuštěním testů
   1. smazání adresářů ```reports/```, ```screenshots/```, ```output/```
   2. Přečtení parametru pro určení prostředí a jeho ověření
2. Spuštění testů
3. Po spuštění testů
   1. Zazipování screenshotů s chybami, pokud existují, pro jejich odeslání emailem

Při spuštění testů je třeba předat parametr pro určení prostředí. Parametr se značí ```--env```, nebo ve zkrácené podobě ```-e``` a může nabývat následujících hodnot: ```dev, test, stage``` a ```prod```. 

Hlavní modul se tedy spustí například příkazem: 
```python main.py -e dev```

*Pozn.: Takto lze modul spouštět v pouze v případě, že byl domovský adresář Pythonu přidán mezi environment variables.*

## configs
Adresář slouží k umístění všech konfiguračních souborů. Všechny soubory jsou popsány níže.

#### config.py
Obsahuje základní hodnoty nutné pro běh testů. K těmto hodnotám je přistupováno při spouštění testů i při jejich běhu. Je zde uloženo pole pro dostupné browsery, cesta k testovacím datům a url adresy jednotlivých prostředí.

#### locators.py
Soubor obsahuje lokátory všech element, se kterými se v rámci testů pracuje. Jsou využívány v POMs (POM = Page Object Models). Elementy jsou organizovány do tříd. Každá třída patří k jednomu POM.

#### suite.py
Soubor slouží k určení toho, které testovací třídy se mají v rámci testování spustit. Je zde uvedeno jednak pole všech testů (```allTests```) a také pole, které obsahuje seznam tříd, které se reálně načtou do testovací sady (```currentSuite```).
K tomuto řešení bylo přistoupeno kvůli možnosti neprovádět vždy všechny testy, což se hodí hlavně při debuggingu a tvorbě testů, kdy spouštění všech testů zdržuje. Při změnách ```currentSuite``` stačí překopírovat potřebné názvy tříd z ```allTests```.

#### requirements.txt
Soubor obsahuje seznam všech modulů, které je nutné doinstalovat, aby mohly testy běžet. Je ho možno využít pro hromadné nainstalování všech modulů, jak bylo uvedeno v části *Moduly*.

Tento soubor je možné využít i v rámci jobu na integračním serveru.

## data
Adresář obsahuje všechna testovací data. Data jsou uložena ve formátu ```json``` a jsou načítána pomocí modulu ```ddt```, který je parsuje do testovacích metod. Každý soubor se váže k jednomu testu, tedy k testovací metodě v testovací třídě. Kolik je záznamů v souboru, tolikrát se testovací metoda spustí s patřičnými test daty. Data jsou v adresáři organizována tak, aby struktura odpovídala struktuře adresářů POMs a testů. 

## pages
Adresář slouží k ukládání POMs. POM uchovává strukturu webové stránky, se kterou je možné pracovat.  Při vytvoření instance POM jsou načteny definované elementy stránky, jejich lokátory jsou načteny z modulu locators.py. Jsou zde rovněž definovány metody pro práci s jednotlivými elementy, které jsou pak dále slučovány do složitějších metod, jako například vyplnění formuláře, který se na stránce zobrazuje. Jednotlivé modely jsou v adresáři strukturovány podle jednotlivých funkčních celků.

## tests
V tomto adresáři jsou uloženy jednotlivé testovací třídy, které obsahují jednotlivé testy (testovací metody), a také ```BaseTest```, který je rodičem všech testů, které tak dětí jeho metody a atributy, aby se kód neopakoval. V případě, že test vyžaduje odlišné chování, jsou potřebné metody překryty.

## utils
Adresář obsahuje všechny pomocné funkce a třídy, které jsou volány v ostatních modulech. Obsahuje modul ```utilsMain.py```, ve kterém jsou implementovány funkce, které slouží k řízení celého programu. V modulu ```utilsTests.py``` jsou funkce, které jsou využívány v testech. Dále obsahuje třídy, které jsou rovněž využívány v testech.

# Jenkins
Integrační server Jenkins slouží k řízení chodu testů na serveru. Testy jsou napsány tak, aby byly funkční stejný způsobem na localu i na serveru. Není tedy potřeba měnit žádné nastavení. Testy jsou řízeny pomocí tzv. jobů, který definuje po sobě jdoucí kroky, které se musí provést.

## Instalace
Instalační soubor pro windows je možno stáhnout na oficiálních stránkách na adrese https://jenkins.io/download/. Při instalaci není nutno měnit výchozí nastavení. Radím však zkontrolovat, že se Jenkins naistaluje pro všechny uživatele. Jenkins by se měl nainstalovat jako windows service, což umožňuje testy spouštět bez závislosti na konkrétním uživatelském účtu a testy tak běží na pozadí. 

Při prvním spuštění je uživatel dotázán na pluginy, které se mají nainstalovat. Mohou být ponechány výchozí pluginy + doinstalovat plugin pro git a plugin s názvem *Email Extension Plugin*, který umožňuje detailní konfiguraci emailů, které se mají posílat při různých výsledcích buildu v jobu.

Dále je nutné zadat prvotní administorské heslo, které je při instalaci vygenerováno. Cesta k heslu je Jenkinsem zobrazena. Dále se nastavuje nový administrátorský účet.

## Nastavení systému
V nastavení systému je třeba nastavit pouze jednu věc, a to určit smtp server, který bude využit k odesílání emailových notifikací. Do nastavení systému je možno se dostat z úvodní stránky Jenkinse pomocí cesty *Administrace -> Nastavení systému*. SMTP server se nastaví v části *Extended E-mail Notification*. Konfiguraci proveďte dle obrázku níže. Heslo k emailu je uloženo na *Tria Wiki v Teams* v části *Přístupy*.

![jenkins_smtpKonfiguration](/assets/img/index_jenkins_smtpKonfiguration.png)

## Globální konfigurace
V globální konfiguraci toho rovněž není třeba nastavovat mnoho. Do globální konfigurace je možno se dostat z úvodní stránky Jenkinse následující cestou *Administrace -> Global tool configuration*.

Git by měl být nastaven automaticky. Nastavení je znázorněno na obrázku níže.

![jenkins_gitKonfiguration](/assets/img/index_jenkins_gitKonfiguration.png)

Za předpokladu, že byl cesta k python.exe přidána do Windows Environment Variables není potřeba provádět nastavení Pythonu. V opačném případě je cestu nutno nastavim rovněž v *Global Tool Configuration*. Také je možné vytvořit environment variable přímo v Jenkinsovi v Nastavení systému

## Vytvoření jobu
Nový job je možno vytvořit na hlavní stránce Jenkinse kliknutím na položku Nové v levém menu. Automatizované testy jsou koncipovány tak, že se dají pustit pouze na jedno konkrétní prostředí. Pro spouštění na dalších prostředích je tedy nutné vytvořit pro každé prostředí jeden job. Dále doporučuji vytvořit další job pro testovací účely, aby zbytečně nebyly notifikováni všechny zúčastněné osoby při každém spuštění jobu. Postačí vytvořit jeden testovací job, nebo může být vytvořen testovací job pro každé prostředí, což je však nadbytečné, jelikož postačí pouze změnit jeden parametr v jobu. Níže jsou popsány jednotlivé části jobu, které se musí nastavit.

### Source Code Management
V této části se nastavují údaje potřebné k získání zdrojového kódu testů. Konfigurace je jednoduchá. Stačí vybrat druh VCS, v našem případě tedy Git, dále druh repozitáře, tedy gitlab, URL adresu repozitáře, kterou je https://gitlab.com/cognevo.eu/tria/tria_ui_tests.git a přístupové údaje k němu, které zde nejsou z důvodu bezpečnosti uvedeny. Přístupové údaje je nutné přidat kliknutím na *Add* a poté je přidat ze seznamu. Jenkins sám hned ověří, zda je možné vytvořit spojení a pokud ne, zobrazí chybovou hlášku. Jako poslední věc je nutné uvést název branche, ze které se má kód stáhnout. Defaultně je vybrána hodnota master. V případě testovacího jobu by zde mělo být uvedeno například ```dev```. Konfigurace je znázorněna na obrázku níže.

![jobConfiguration_SourceCodeManagement](/assets/img/index_jobConfiguration_SourceCodeManagement.png)

### Build Triggers
V této částě se nastavují události, při kterých se má job spustit. Nyní je job nastaven tak, aby se spustil periodicky kolem půlnoci. Volba ```@midnight``` nedefinuje čas přesně. To je užitečné v případě, že je tato volba nastavena u více jobů. Jenkins tak nespustí všechny joby ve stejný čas. Celá konfigurace je znázorněna na obrázku níže.

![jobConfiguration_BuildTriggers](/assets/img/index_jobConfiguration_BuildTriggers.png)

Pro dalším vývoji je možné nastavit job tak, aby se spustil v momentě, kdy je pushnut zdrojový kód Trii do jejího repozitáře. V takovém případě by se musel vytvořit nový job, kde by byl v části Source Code Management nastaven přístup k repozitáři Trii a v části *Build Triggers* vybrána volba *Build when a change is pushed to…* V jobu pro spuštění testů by pak byla v části *Build Triggers* vybrána volba *Build after other projects are built* a vyplnil by se název jobu, který hlídá repozitář Trii. 

### Build Environment
V části *Build Environment* je vhodné zaškrtnout volbu *Delete workspace before build starts*, aby se vždy začalo s čistým štítem

### Build
V části *Build* se testy již spouští. Je možno je spustit pomocí příkazu využitím volby *Execute Windows batch command*. Celá konfigurace je znázorněna na obrázku níže. Provádí se zde 2 příkazy. První z nich nainstaluje potřebné moduly včetně všech závislostí. Tato možnost byla již dříve zmiňována, avšak platí zde i uvedené omezení u ```html-testRunner``` a při prvním spuštění jobu dojde k chybě kvůli parametru ```combine-reports```. Po nainstalování modulu je třeba manuálně změnit obsah uvedených souborů a při dalším spuštění by měl job projít.
Další příkaz slouží k vlastnímu spuštění testů. Je zde navíc uvedena volba ```-u```, bez které není možno vypisovat informace do Jenkins konzole. 

![jobConfiguration_Build](/assets/img/index_jobConfiguration_Build.png)

### Post-build Actions
V části *Post-build Actions* je nastaveno odesílání notifikací emailem. Nejdříve je třeba přidat step *Editable Email Notification*. V přídaném stepu se pak v *Advanced Settings...* nastaví triggery. Triggery je třeba nastavit 2. Jeden pro úspěšný build a jeden pro neúspěšný build. Neúspěšný build znamená, že nastala nějaká chyba v programu a testy nedoběhly, nebo se vůbec nespustily. Při úspěšném testu se všechny testy provedly a jejich výsledek je buď *failed* nebo *passed*.

V části *Triggers* se tedy přidá trigger *Success* a *Failure - Any*. V poli *Send To* můžeme nastavit odeslání emailu na konkrétní adresy, nebo na vytvořené skupiny. V našem případě byla zvolena možnost *Recipient List* a ve stejně pojmenovaném poli se pak vyplní příslušné adresy. 

U Triggeru *Success* jsou v části *Attachments* k emailu přiloženy test reporty a zazipované screenshoty chyb. Build log nemusí být přiložen.

![jobConfiguration_NotificationSuccess](/assets/img/index_jobConfiguration_NotificationSuccess.png)

U Triggeru *Failure - Any* naopak nemá smysl přikládat test reporty, jelikož nebyly vytvořeny, ale je nutné přiložit build log, kde se dá vyčíst chyba, která způsobila pád programu.

![jobConfiguration_NotificationFailure](/assets/img/index_jobConfiguration_NotificationFailure.png)
