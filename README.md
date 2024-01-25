AI Assignment
Connor McCabe -20324241
Zeiad Elmallah – 20739091

Our Code Structure:
Imports and global variables at the top. Function to get max and average scores used for displaying results. Mutate list function which randomly changes 1 of the alels. Divide list into sections function which divides the genes into sections depending on a function of number of parents and children. Function mutation which is the main function that covers crossover and calls the sub functions. Random binary list function which makes a random parent within a certain range. Function for fitness, depending on the version the function changes, to define the fitness of each genome max score function which gets the max score of a generation. Then we have our code for each generation and after that we are plotting out the results.

Representations:
Plot showing the max fitness to the generation number.

Fitness function:
Based on the version running a fitness function is ran returning the fitness of the genotype. 

Selection:
Based on the top N parents.

Crossover:
After separating the genotype for all the parents, we equally swap the sections over randomly until the number of children is satisfied. In the mutation function.

Mutation:
Part of the mutation function where it calls the mutation list function for half of the new generation where it randomly swaps a binary number.
Other operations:

Plots: 
Plot showing the max fitness to the generation number using matplotlib.
Description of results:

Sources: N/A
