# Projekt: Politiets Døgnrapporter af Marcus P og Andreas E.


# 25/3 logbog (første officiele logbog)
1) Vi kan nu vælge datoer (intervaller eller bare startdato), og scrape alt content fra døgnrapporterne ned lokalt i en text-fil. <br/>
2) Har lavet en word counter, for at analysere, hvilke ord ('forbrydelses-keywords') som bruges.
3) Ændret titel på txtfiler baseret på det html-div som viser datoen, og ikke overskiften.

# 31/3 logbog
1) Vi har indset, at clustering fungerer bedre end classification, med de data vi kender, og kan finde. Derfor vil vi ændre vores problembeskrivelse:
> "***Vi vil prøve at forudse forbrydelser på forhånd, for at hjælpe politiet, ved at se mønstrer i begåede forbrydelser***"
2) Forbedring af word counter
3) Forberedelse til 'keyword-identifier' til ML-delen
4) Påbegyndelse af K-means-clustering

# 1/4 logbog
0) Vi har ikke lavet noget i dag, haha aprilsnar!
1) Da vi har gemt data om koordinater og forbrydelser i seperate filer, skal vi finde en måde at importere og redigere disse data, så de har den rigtige formatering til brug i vores algoritme.
2) Udfyld txt-filer med keywords, som er associerede med bestemte forbrydelser
3) Fuldt fokus på k-means-clustering; både 2D og 3D
4) Har fixet fejl i wordcounter, hvor ord, efterfulgt af punktum eller komma (og ligendne) er en del af selve ordet 

# 14/4 logbog
1) Scrape yderligere sider for mere detaljeret word counter
2) Opdater word_counter.py for bedre effektiv
3) Ændret regler for forbrydelseskategorier
4) Keywordlist er udfyldt

# 15/4 logbog
1) Lav liste/csv med forbrydelser, som vi kan matche med en bestemt kategori af forbrydelser, som tyveri og vold mv. (så vi kun kigger på de relevante forbrydelser)
2) Python script som vurderer, hvilket type kriminalitet, der er at gøre med, og derefter tilføjer den til tidligere nævnte liste/csv

# 22/4 logbog
1) Eksperimentering med database. Vi har kigget på SQLite i developmentforløbet, og ville have PostgreSQL i produktion, som man kan integrere gennem web-hosting siden, Heroku. Vi konkluderede dog, at da vi ikke ændre i databasen dynamisk, kan man lige så godt nøjes med en statisk fil.

# 27/4 logbog
1) Vi lavede planer om fremgangsmåde på tavlen

# 28/4 logbog
1) Vi har eksperimenteret med KMeans clustering

# 29/4 logbog
1) Løst problemer med indlæsning af .csv til pandas dataframe
2) Problemer med doublequotes i Dataframe der gjorde konvertering til integers problemeatisk.

# 30/4 logbog
1) Fik både 2D og 3D clustering til at virke
2) Yderligere planlægning af metoder, og vægtning af forbrydelsestyper

