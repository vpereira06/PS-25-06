#Ex. 1

texto = "Numa terra fantástica e única, chamada Terra-Média, um hobbit recebe de presente de seu tio o Um Anel, um anel mágico e maligno que precisa ser destruído antes que caia nas mãos do mal. Para isso o hobbit Frodo (Elijah Woods) terá um caminho árduo pela frente, onde encontrará perigo, medo e personagens bizarros. Ao seu lado para o cumprimento desta jornada aos poucos ele poderá contar com outros hobbits, um elfo, um anão, dois humanos e um mago, totalizando 9 pessoas que formarão a Sociedade do Anel."

def resumir(texto):
    if len(texto) <= 140:
        texto_resumido = texto
        return texto_resumido
    else:
        texto_resumido = texto[:140] + "..."
        return texto_resumido

print(resumir(texto))

#Ex. 2

valor = "2596061015"

def ler_digito(valor):
    if valor[0] == "1":
        valor_dec = valor[:3]
        valor_dec = valor_dec[0] + "," + valor_dec[1] + valor_dec[2] + " Bilhão"
        return valor_dec
    else:
        valor_dec = valor[:3]
        valor_dec = valor_dec[0] + "," + valor_dec[1] + valor_dec[2] + " Bilhões"
        return valor_dec

print(ler_digito(valor))

#Ex. 3

filmes = {
    "1997": {
        "Titanic": 2187463944
        },
    "2009": {
        "Avatar": "2787965087"
        },
    "2011": {
        "Harry Potter and the Deathly Hallows – Part 2": "1341693157"
        },
    "2012": {
        "Marvel's The Avengers": "1518812988"
        },
    "2013": {
        "Frozen": "1276480335"
        },
    "2015": {
        "Avengers: Age Of Ultron": "1405403694", "Star Wars: The Force Awakens": "2068223624", "Furious 7": "1516045911", "Jurassic World": "1671713208"
        },
    "2017": {
        "Star Wars: The Last Jedi": "1332539889", "Beauty and the Beast": "1263521126"
        },
    "2018": {
        "Black Panther": "1346913161", "Avengers: Infinity War": "2048359754", "Jurassic World: Fallen Kingdom": "1309484461"
        },
    "2019": {
        "Avengers: Endgame": "2750667499"
        }
    }
