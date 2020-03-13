something 
something 
tmp_var n° 4 = 3
adresse de i : 0 
tid i = elemId 4
something 
tmp_var n° 5 = 4
adresse de j : 1 
tid j = elemId 5
something 
tmp_var n° 6 = 8
adresse de k : 2 
tid k = elemId 6
something 
something 
tmp_var n° 7 <-> elemId 0
tmp_var n° 8 <-> elemId 1
elemId 7 + elemId 8
tmp_var n° 9 <-> elemId 0
tmp_var n° 10 <-> elemId 2
tmp_var n° 11 <-> elemId 1
elemId 10 / elemId 11
elemId 9 + elemId 10
elemId 7 * elemId 9
adresse de r : 3 
tid r = elemId 7
something 
something 
something 
Taille de la llist: 8
Element n° 7: tmp type: int constante: 0 adresse: 7 profondeur: 1 initialisé: 0 
Element n° 6: tmp type: int constante: 0 adresse: 6 profondeur: 1 initialisé: 0 
Element n° 5: tmp type: int constante: 0 adresse: 5 profondeur: 1 initialisé: 0 
Element n° 4: tmp type: int constante: 0 adresse: 4 profondeur: 1 initialisé: 0 
Element n° 3: r type: int constante: 0 adresse: 3 profondeur: 1 initialisé: 1 
Element n° 2: k type: int constante: 0 adresse: 2 profondeur: 1 initialisé: 1 
Element n° 1: j type: int constante: 0 adresse: 1 profondeur: 1 initialisé: 1 
Element n° 0: i type: int constante: 0 adresse: 0 profondeur: 1 initialisé: 1 
Taille de la liste: 42
AFC   0   3  
STORE 4   0  
LOAD  0   4  
STORE 0   0  
AFC   0   4  
STORE 5   0  
LOAD  0   5  
STORE 1   0  
AFC   0   8  
STORE 6   0  
LOAD  0   6  
STORE 2   0  
PRI   0  
LOAD  0   0  
STORE 7   0  
LOAD  0   1  
STORE 8   0  
LOAD  0   7  
LOAD  1   8  
ADD   2   0   1  
STORE 7   2  
LOAD  0   0  
STORE 9   0  
LOAD  0   2  
STORE 10  0  
LOAD  0   1  
STORE 11  0  
LOAD  0   10 
LOAD  1   11 
DIV   2   0   1  
STORE 10  2  
LOAD  0   9  
LOAD  1   10 
ADD   2   0   1  
STORE 9   2  
LOAD  0   7  
LOAD  1   9  
MUL   2   0   1  
STORE 7   2  
LOAD  0   7  
STORE 3   0  
PRI   3  
