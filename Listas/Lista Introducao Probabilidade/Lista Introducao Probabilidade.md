# Lista de Execícios - Introdução a Probabilidade

### 1. Aka Capitulo 5 - Questão 1

![image](https://user-images.githubusercontent.com/15125899/180634758-8db1a865-2542-44f8-a446-68f6b4324ded.png)


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

-----------------------------------

### 2. Aka Capitulo 5 - Questão 2
![image](https://user-images.githubusercontent.com/15125899/180634764-5824b064-ba06-405c-83d7-20e8fe8e0bdc.png)


Q = {5}
N = {1,2,3,4,6}
S = {(Q),(N,Q),(N,N,Q),...,(N,...,N,Q)}
```

-----------------------------------

### 3. Aka Capitulo 5 - Questão 3

![image](https://user-images.githubusercontent.com/15125899/180634768-e0fa85fc-e7ad-4341-8cd5-b02185bdd0e1.png)


```R
S = {AA,BB,CC,ACA,BCB,ACC,BCC,BCAA,ACBB}
```

-----------------------------------

### 4. Aka Capitulo 5 - Questão 4

![image](https://user-images.githubusercontent.com/15125899/180634773-c1de2f08-10f4-415a-832f-a4ba33c8cb69.png)


```python
Moeda 1:
M1 = {H,T}

Moeda 2:
M2 = {H,T}

S = M1 × M2 = {(HH),(TT),(HT),(TH)}
```

-----------------------------------

### 5. Aka Capitulo 5 - Questão 4
![image](https://user-images.githubusercontent.com/15125899/180634774-b964f40b-89dc-4c6b-b8e7-0252909910b0.png)

```python
Moeda:
M = {H,T}

Dado:
D = {1,2,3,4,5,6}

S = M × D = {(T,1),(T,2),(T,3),(T,4),(T,5),(T,6),(H,1),(H,2),(H,3),(H,4),(H,5),(H,6)}
```

-----------------------------------

### 6. Aka Capitulo 5 - Questão 6

![image](https://user-images.githubusercontent.com/15125899/180634780-06180c84-8c27-48f7-b171-7cf1ac3d2c05.png)


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
-----------------------------------

### 7. Aka Capitulo 5 - Questão 7

![image](https://user-images.githubusercontent.com/15125899/180634784-ec422b6d-211a-4305-88ea-bccf3ea1b46b.png)


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

-----------------------------------

### 8. Aka Capitulo 5 - Questão 8

![image](https://user-images.githubusercontent.com/15125899/180634787-e42ff943-36b8-4525-a460-c5ef6e3d421d.png)


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

-----------------------------------

### 9. Aka Capitulo 5 - Questão 9

![image](https://user-images.githubusercontent.com/15125899/180634792-4d2e7371-80c1-4659-a17d-385e59d9c512.png)


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

-----------------------------------

### 10. Aka Capitulo 5 - Questão 10

![image](https://user-images.githubusercontent.com/15125899/180634799-f48b1304-2b00-4c55-a844-a54f44b2394d.png)


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
-----------------------------------

### 11. Aka Capitulo 5 - Questão 11

![image](https://user-images.githubusercontent.com/15125899/180634800-cb566e44-96be-44c3-aeaa-034065ab3d23.png)

![image](https://user-images.githubusercontent.com/15125899/173176147-94abaa4e-6174-49b1-a2c8-e78ad16fbd55.png)

-----------------------------------

### 12. Aka Capitulo 5 - Questão 12

![image](https://user-images.githubusercontent.com/15125899/180634804-54229c8c-3b33-4c2b-ae0a-eab045db5196.png)

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
-----------------------------------
### 13. Aka Capitulo 5 - Questão 13

![image](https://user-images.githubusercontent.com/15125899/180634811-42a3da5f-3791-40e7-9ca0-ea62d3d40579.png)


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
-----------------------------------
### 14. Aka Capitulo 5 - Questão 14

![image](https://user-images.githubusercontent.com/15125899/180634814-01f63ac8-3e77-4796-bba4-28760d619e23.png)

-A

-B

-C
