# Lista de Execícios - Introdução a Probabilidade

### 1. Aka Capitulo 5 - Questão 1

- Duas bolas brancas;
- Duas bolas pretas;

Ao retirar a boa temos 2 casos:
- (I) Se a bola é branca, então lançar um moeda
- (II) Se a bola é preta, então retirar outra bola

#### Caso (I)
```R
B = bola branca
C = cara
K = coroa

S1 = {BC,BK}
```
#### Caso (II)
```R
B = bola branca
P = bola preta

S2 = {PP,PV}
```
resposta = `S1 U S2 = {BC,BK,PP,PV}`

### 2. Aka Capitulo 5 - Questão 2


Q = {5}
N = {1,2,3,4,6}
S = {(Q),(N,Q),(N,N,Q),...,(N,...,N,Q)}
```

### 3. Aka Capitulo 5 - Questão 3

```R
S = {AA,BB,CC,ACA,BCB,ACC,BCC,BCAA,ACBB}
```

### 4. Aka Capitulo 5 - Questão 4

```python
Moeda 1:
M1 = {H,T}

Moeda 2:
M2 = {H,T}

S = M1 × M2 = {(HH),(TT),(HT),(TH)}
```

### 5. Aka Capitulo 5 - Questão 4

```python
Moeda:
M = {H,T}

Dado:
D = {1,2,3,4,5,6}

S = M × D = {(T,1),(T,2),(T,3),(T,4),(T,5),(T,6),(H,1),(H,2),(H,3),(H,4),(H,5),(H,6)}
```

### 6. Aka Capitulo 5 - Questão 6

- A:
```python
S = {1,2,3,4,5,6} × {1,2,3,4,5,6}
```

- B:
```python
S = {D,DD,DDD,DDD,DDDD,DDD...D}
```

- C:
```python
S = {MMM,MMF,MFF,FFF}
```

- D:
```python
Assinates: A = {1,...,250}
Possui Maquina de Lavar ?: P = {S,N}
S = A × P
```

- E:
```python
S = {1 hora, 2 horas, 3 horas, 4 horas, 5 horas, ...}
```
- F:
```python
- 10 Nomes
- 3 Mulheres
- 7 Homens
S = {(HHHHHHHMMM),(HHHHHHMMM),(HHHHHMMM),(HHHHMMM),(HHHMMM),(HMMM),(MMM)}
```

- G:
```python
S = {(H),(TH),(TTH),...,(T...TH)}
```

- H:
```python
360 / 60 = 60
S = {0,60,120,180,240,300,360}
```

- I:
```python
S = {0...360}
```

- J:
```python
pessoas: P = {A,B,C,D,E}
S = P × P
```

- L:
```python
S = (P × P) - {(A,A),(B,B),(C,C),(D,D),(E,E)}
```

- M:
```python
S =  
```

- N:
```python
Classe: C = {A,B,C,D}
Estado Civil: E = {S,C,V,D}
S = C × E
```

### 7. Aka Capitulo 5 - Questão 7
```python
S = M1 × M2 = {(HH),(TT),(HT),(TH)}
```

-A

```python
{(HH),(HT),(TH)}
```

-B

```python
{(HH)}
```

-C

```python
{(TT),(HT),(TH)}
```

### 8. Aka Capitulo 5 - Questão 8

-A) **A** ocorre mas **B** não ocorre;

```python
 
```

-B) Exatamente um dos eventos **A** e **B** ocorre;

```python
 A U B; reunião de A e B
```

-C) enhum dos dois eventos **A** e **B** ocorre.

```python

```

### 9. Aka Capitulo 5 - Questão 9

- A) Mostre que a soma das probabilidades dos pontos do espaço amostral é 1.

```R
S = {AA,BB,CC,ACA,BCB,ACC,BCC,BCAA,ACBB}

AA   = 1/2 * 1/2             = 1/4
BB   = 1/2 * 1/2             = 1/4
CC   = 1/3 * 1/3             = 1/9
ACA  = 1/2 * 1/3 * 1/2       = 1/12
BCB  = 1/2 * 1/3 * 1/2       = 1/12
ACC  = 1/2 * 1/3 * 1/3       = 1/18
BCC  = 1/2 * 1/3 * 1/3       = 1/18
BCAA = 1/2 * 1/3 * 1/2 * 1/2 = 1/24
ACBB = 1/2 * 1/3 * 1/2 * 1/2 = 1/24

1/4 + 1/4 + 1/9 + 1/12 + 1/12 + 1/18 + 1/18 + 1/24 + 1/24 + ... = 1
```

- B) Calcule a probabilidade de que A vença (um jogador vence quando ganha duas partidas seguidas). Em seguida, calcule a probabilidade de que B vença.

```R
S = {AA,BCAA}
AA = BB = 1/4 
BCAA = ACBB = 1/24
P(A vencer) = 7/24
P(B vencer) = 7/24
```

- C) Qual a probabilidade de que não haja decisão?
```R
ACA = 1/12
BCB = 1/12
ACC = 1/18
BCC = 1/18

P(Sem Vencedor) = 1/12 + 1/12 + 1/18 + 1/18 = 5/18
```

### 10. Aka Capitulo 5 - Questão 10

```R
"5" = 5/6
Q = (1/6)^k
```

-A
![image](https://user-images.githubusercontent.com/15125899/173175830-efe8f1d8-8807-4713-9c4a-0d235a1db9e1.png)

-B
```R
1 Lançameneto)
p = (5/6)⁰(1/6) = 0.16666...

2 Lançamenetos)
p = (5/6)²(1/6) = 0.11574...

3 Lançamenetos)
p = (5/6)³(1/6) = 0.09645...
```

### 11. Aka Capitulo 5 - Questão 11

![image](https://user-images.githubusercontent.com/15125899/173176147-94abaa4e-6174-49b1-a2c8-e78ad16fbd55.png)

### 12. Aka Capitulo 5 - Questão 12

 ```R
A = {(3,6),(4,5),(5,4),(6,3)} 
B = {(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),
     (5,1),(5,2),(5,3),(5,4),(5,5),(5,6),
     (6,1),(6,2),(6,3),(6,4),(6,5),(6,6)}

A ∪ B = {(4, 3), (5, 4), (4, 6), (5, 1), (6, 2),
         (6, 5), (4, 2), (4, 5), (5, 6), (3, 6),
         (5, 3), (6, 1), (6, 4), (4, 1), (5, 2),
         (4, 4), (5, 5), (6, 6), (6, 3)}

A ∩ B = {(4, 5), (6, 3), (5, 4)}

A = {(3,6),(4,5),(5,4),(6,3)} 
```

### 13. Aka Capitulo 5 - Questão 13
**7.**
```python
S = M1 × M2 = {(HH),(TT),(HT),(TH)}
```
-A
```python
{(HH),(HT),(TH)}
```

-B
```python
{(HH)}
```

-C
```python
{(TT),(HT),(TH)}
```
**12.**
```python
P(A ∪ B) = 19/6² = 0,527777...
```
```python
P(A ∩ B) = 3/6² = 0,08333..
```
```python
P(A) = 4/6² = 0,11111...  ERRADO? 
```
### 14. Aka Capitulo 5 - Questão 14

-A

-B

-C
