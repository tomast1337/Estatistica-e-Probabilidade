## 1.
![image](https://user-images.githubusercontent.com/15125899/182244974-8c8afdc8-1554-4608-a725-d5e49a12293e.png)

![image](https://user-images.githubusercontent.com/15125899/171267451-907b8320-ca4e-4468-8bb7-c031d1cc4879.png)

x|P(X)    |P(X) Decimal|
-|--------|------------|
0|	1/56	|0.01785     |
1|	15/56	|0.26785     |
2|	15/28	|0.53571     |
3|	5/28	|0.17857     |

## 2.
![image](https://user-images.githubusercontent.com/15125899/182244984-3e51960f-d4e3-4233-a7df-a7bf3becc12b.png)

![image](https://user-images.githubusercontent.com/15125899/171269460-013cddc5-ece9-42ba-993f-4b0b5cefd7f8.png)
x|	P(X)	|P(X) Decimal|
-|--------|------------|
0|27/512	|0.052734375 |
1|135/512	|0.263671875 |
2|225/512	|0.439453125 |
3|125/512	|0.244140625 |

## 3.
![image](https://user-images.githubusercontent.com/15125899/182245008-1a6a5281-ff0a-4fee-829c-023c9d9c8597.png)

![image](https://user-images.githubusercontent.com/15125899/171325106-f1938e3e-4729-429e-83f4-0e6a3480bb9e.png)

## 4.
![image](https://user-images.githubusercontent.com/15125899/182245017-9ec0f978-6063-412f-a796-b84dc4cfaa60.png)

![image](https://user-images.githubusercontent.com/15125899/171317492-12d0e1f8-8c96-4074-b7d1-9f9a0d113699.png)

x|	P(X) |P(X) Decimal |Combinaação|
-|-------|-------------|-----------|
0|	(½)⁰ |1	           |t          |
1|	(½)² |0.5          |ht         |
2|	(½)² |0.25         |hht        |
n|	(½)^n|	…          |h..ht      |

## 5. e 6. ?
![image](https://user-images.githubusercontent.com/15125899/182245027-0a3a1e3f-f397-4a54-a695-fee390f8160c.png)
![image](https://user-images.githubusercontent.com/15125899/182245035-de144f39-0f4f-4f40-9469-2df6d0ce1fc0.png)

![image](https://user-images.githubusercontent.com/15125899/171326371-8bb1c731-c42a-4402-88cf-3243602b5481.png)

## 7.
![image](https://user-images.githubusercontent.com/15125899/182245051-7cd84349-d110-4885-a1b5-0380f942c848.png)

![image](https://user-images.githubusercontent.com/15125899/173209725-d52b4b74-0b57-4235-bede-45941a5e41d9.png)
![image](https://user-images.githubusercontent.com/15125899/173209734-0d8082cb-277d-45f7-86ee-122d65502550.png)

1)
```R
E(X) = (0*1/56)+(1*15/56)+(2*15/28)+(3*5/28) = 1+(7/8) = 1.875
```
```R
Var(X) = ([0 - (1+(7/8))]² * 1/56 )+([1 - (1+(7/8))]² * 15/56)+([2 - (1+(7/8))]² * 15/28)+([3 - (1+(7/8))]² * 5/28 ) = 225/448 = 0.5022
```
2)
```R
E(X) = (0*27/512)+(1*135/512)+(2*225/512)+(2*125/512)	 = 1+(323/512) = 1.630
```
```R
Var(X) = ([0 + (1+(323/512))]²* 27/512)+([1 + (1+(323/512))]²*135/512)+([2 + (1+(323/512))]²*225/512)+([2 + (1+(323/512))]²*125/512) = 0.474609375
```
## 8.
![image](https://user-images.githubusercontent.com/15125899/182245066-1dd359f9-b1a2-4f5a-815b-f3f77fdbea85.png)

E(Y) = ![image](https://user-images.githubusercontent.com/15125899/173210380-c4f4a530-b1f2-46ec-970e-c239a1bff41a.png)
= 1 ???
```R
Var(Y)
```
## 9.
![image](https://user-images.githubusercontent.com/15125899/182245086-98289832-a54f-44b1-870b-709ab7a7537d.png)



## 10.
![image](https://user-images.githubusercontent.com/15125899/182245095-3af8a8cb-a4b7-4a72-9a01-1246ba376fb7.png)

```R
X = {(CCC),(CCR),(CRR),(RRR)}
   3caras 2caras 1cara 0caras
Y = {(CRC,RCR),(CCR,RRC,RCC,CRR),(CCC,RRR)}
         3    ,        2        ,    1 sequencias
```

X|P(X)             |P(X) real|
-|-----------------|---------|
0|½ * ½ * ½ = 1/8  | 0.125   |
1|(½ * ½ * ½)*2 = ¼| 0.25    |
2|(½ * ½ * ½)*2 = ¼| 0.25    |
3|½ * ½ * ½ = 1/8  | 0.125   |

Y |P(Y)              |P(Y) real|
--|------------------|---------|
0 |(½ * ½ * ½)*2 = ¼ |0.25     |
1 |(½ * ½ * ½)*4 = ½ |0.5      |
2 |(½ * ½ * ½)*2 = ¼ |0.25     |

```R
E(X) = (0*(1/8))+(1*(1/4))+(2*(1/4))+(3*(1/8)) = 1.125
Var(X) = [0-1.125]²*(1/8)+[1-1.125]²*(1/4)+[2-1.125]²*(1/4)+[3-1.125]²*(1/8) = 0.875
```

```R
E(Y) = (0*(1/4))+(1*(1/2))+(2*(1/4)) = 1
Var(Y) = [0-1]²*(1/4)+[1-1]²*(1/2)+[2-1]²*(1/4) = 0.5
```
## 11.
![image](https://user-images.githubusercontent.com/15125899/182245109-1f7293f3-9d82-447a-b0a9-305a8cbc29db.png)



## 12.
![image](https://user-images.githubusercontent.com/15125899/182245118-333bf25d-6918-4010-871b-007ee851fe84.png)



## 13.
![image](https://user-images.githubusercontent.com/15125899/182245132-2a2b3ba9-4f4f-4121-9b5f-83f09ac1d3b9.png)



## 14.
![image](https://user-images.githubusercontent.com/15125899/182245147-000f24f9-3bad-4eaf-b425-6df6c3ce98f2.png)



## 15.
![image](https://user-images.githubusercontent.com/15125899/182245156-16f52467-ed6a-493a-aa44-7c1e608327b0.png)



## 16.
![image](https://user-images.githubusercontent.com/15125899/182245164-052bb19c-cab1-4d6f-bcb1-e76ccc7d241d.png)



## 17.
![image](https://user-images.githubusercontent.com/15125899/182245189-4d0ae0d8-2294-4321-88f7-78f1164624c1.png)

(a)

(b)



## 18.
![image](https://user-images.githubusercontent.com/15125899/182245206-d3689e72-eb46-4c3e-a8f7-b99926266643.png)



## 19.
![image](https://user-images.githubusercontent.com/15125899/182245213-35483403-ee4a-418a-8c50-9b449f3826e2.png)



## 20.
![image](https://user-images.githubusercontent.com/15125899/182245236-a34533b1-40dc-4a07-99ec-83e254d29121.png)

(a)

(b)

(c)

(d)

(e)


## 21.
![image](https://user-images.githubusercontent.com/15125899/182245257-c9d247da-f242-4ae9-9e32-14e7dd448495.png)

(a)

(b)

(c)

(d)

(e)

(f)

(g)


## 22.
![image](https://user-images.githubusercontent.com/15125899/182245274-80b64c97-1fb9-43b8-a07c-10f33fbf186d.png)

(a)

(b)

(c)

(d)



## 23.
![image](https://user-images.githubusercontent.com/15125899/182245293-b5b14712-6821-4cc7-a77b-6227fb4f11fc.png)



## 24.
![image](https://user-images.githubusercontent.com/15125899/182245299-4dc9ffa7-48d7-477a-8a6b-a86ab21cd278.png)



## 25.
![image](https://user-images.githubusercontent.com/15125899/182245317-84fc039f-e4e6-454c-9067-15e059dbcf91.png)



## 26.
![image](https://user-images.githubusercontent.com/15125899/182245333-0180ed84-7093-4325-92ba-141ddc9a7096.png)



## 27.

![image](https://user-images.githubusercontent.com/15125899/182245350-8f2dc0ec-9975-44b3-be8f-4495e99c2842.png)


## 28.
![image](https://user-images.githubusercontent.com/15125899/182245370-644b2e67-0396-415d-b50c-9cf2bfd41e10.png)


