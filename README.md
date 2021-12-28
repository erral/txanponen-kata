# txanponen-kata

Kata bat programazio ariketa bat da, garatzaileon programazio-gaitasunak hobetu eta beste batzuekin batera garatzen ikasteko.

Normalean ariketa sinple-sinpleak izaten dira, bikoteka ebaztekoak eta teknika desberdinak erabiliz elkarren arteko komunikazioa ahalbidetzen dute. Lehenengo fase baten bikoteko batek garatu dezake eta denbora bat pasatuta besteak; edo denbora bat pasatuta beste bikotekide batekin landu dezakezu ariketa. Hainbat modu daude.

Gaurko ariketa txapon sailkatzaile bat egitea da: diru kopuru bat emanda, kopuru hori txanpon ezberdinetan nola banatzen den ikusteko. Adibidez:

- 4 € = 2 €ko 2 txanpon
- 15,32€ = 2 €ko 7 txanplano, € 1eko txanpon 1, 20 zentimoko txanpon 1, 10 zentimoko txanpon 1 eta 2 zentimoko txanpon bat

Gainera ariketan zehar [TDD](https://en.wikipedia.org/wiki/Test-driven_development) erabiltzea ere interesgarria iruditu zait. Teknika honek dioenez ezer programatu aurretik testak programatu beharko lirateke. Ondoren programa eta azkenik testak exekutatu programa ondo dagoela ziurtatzeko. Hori askotan ez da erraza izaten, programatzen zaudela datu-moten inguruko erabakiak hartu behar izaten direlako eta askotan testak idazteko garaian hori kontuan hartu ez delako. Hori dela-eta hurbilpen hibridoa erabiliko dut, lehenengo testa idatzi bai, baina programa eta testa edozein momentutan aldatuz.

Zuzenekoan ikusi ditugun arazo batzuk hemen zerrendatuta:

- [Ariketaren jatorrizko enuntziatua](https://katayuno-app.herokuapp.com/katas/27)
- Koma higikorreko aritmetika: [Wikipediako azalpena](https://en.wikipedia.org/wiki/Floating-point_arithmetic) [pythonen azalpena](https://stackoverflow.com/questions/588004/is-floating-point-math-broken)
- [Test automatikoak exekutatzeko konfigurazioa Github Actions erabiliz](https://github.com/erral/txanponen-kata/blob/master/.github/workflows/python-app.yml)
