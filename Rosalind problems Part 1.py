#Rosalind problems

#Rabbits and Recurrence Relations 
#The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
#every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
n= 32
k=2
pairs= 1
offspring2=0
print(n)
while n>1:
    offspring1= pairs*k #each set of pairs, produces k offspring
    pairs+=offspring2 #the offspring grow up to become pairs
    n-=1 
    offspring2= offspring1
print(pairs)

