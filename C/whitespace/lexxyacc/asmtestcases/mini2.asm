something 
tmp_var n° 0 = 10
tid a = elemId 0
something 
tmp_var n° 2 = 17
tid d = elemId 2
something 
tmp_var n° 4 = 1
tid b = elemId 4
something 
tmp_var n° 6 <-> elemId 1
tmp_var n° 7 <-> elemId 3
elemId 6 + elemId 7
adresse de b : 5 
tid b = elemId 6
something 
something 
tmp_var n° 8 <-> elemId 1
something 
tmp_var n° 9 <-> elemId 3
tmp_var n° 10 = 1
elemId 9 + elemId 10
adresse de d : 3 
tid d = elemId 9
something 
tmp_var n° 11 <-> elemId 1
tmp_var n° 12 = 1
elemId 11 - elemId 12
adresse de a : 1 
tid a = elemId 11
something 
something 
something 
something 
tmp_var n° 13 = 24
adresse de d : 3 
tid d = elemId 13
something 
something 
something 
Taille de la llist: 10
Element n° 13: tmp type: int constante: 0 adresse: 13 profondeur: 1 initialisé: 0 
Element n° 11: tmp type: int constante: 0 adresse: 11 profondeur: 2 initialisé: 0 
Element n° 9: tmp type: int constante: 0 adresse: 9 profondeur: 2 initialisé: 0 
Element n° 6: tmp type: int constante: 0 adresse: 6 profondeur: 1 initialisé: 0 
Element n° 5: b type: int constante: 0 adresse: 5 profondeur: 1 initialisé: 1 
Element n° 4: tmp type: int constante: 0 adresse: 4 profondeur: 1 initialisé: 0 
Element n° 3: d type: int constante: 0 adresse: 3 profondeur: 1 initialisé: 1 
Element n° 2: tmp type: int constante: 0 adresse: 2 profondeur: 1 initialisé: 0 
Element n° 1: a type: int constante: 0 adresse: 1 profondeur: 1 initialisé: 1 
Element n° 0: tmp type: int constante: 0 adresse: 0 profondeur: 1 initialisé: 0 
Taille de la liste: 54
AFC   0   10 
STORE 0   0  
LOAD  0   0  
STORE 1   0  
AFC   0   17 
STORE 2   0  
LOAD  0   2  
STORE 3   0  
AFC   0   1  
STORE 4   0  
LOAD  0   4  
STORE 5   0  
LOAD  0   1  
STORE 6   0  
LOAD  0   3  
STORE 7   0  
LOAD  0   6  
LOAD  1   7  
ADD   2   0   1  
STORE 6   2  
LOAD  0   6  
STORE 5   0  
PRI   5  
LOAD  0   1  
STORE 8   0  
LOAD  0   8  
JMPC  48  0  
LOAD  0   3  
STORE 9   0  
AFC   0   1  
STORE 10  0  
LOAD  0   9  
LOAD  1   10 
ADD   2   0   1  
STORE 9   2  
LOAD  0   9  
STORE 3   0  
LOAD  0   1  
STORE 11  0  
AFC   0   1  
STORE 12  0  
LOAD  0   11 
LOAD  1   12 
SUB   2   0   1  
STORE 11  2  
LOAD  0   11 
STORE 1   0  
PRI   1  
PRI   3  
AFC   0   24 
STORE 13  0  
LOAD  0   13 
STORE 3   0  
PRI   3  
