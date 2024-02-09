AI Assignment
Connor McCabe -20324241
Zeiad Elmallah – 20739091

1.4 A
Our Code Structure:
Imports and global variables at the top. Function to get max and average scores used for displaying results. Mutate list function which randomly changes 1 of the alels. Divide list into sections function which divides the genes into sections depending on a function of number of parents and children. Function mutation which is the main function that covers crossover and calls the sub functions. Random binary list function which makes a random parent within a certain range. Function for fitness, depending on the version the function changes, to define the fitness of each genome max score function which gets the max score of a generation. Then we have our code for each generation and after that we are plotting out the results.

Representations:
The representation involves generating a plot that illustrates the maximum fitness achieved against the generation number. This graphical representation provides valuable insights into the progression of fitness levels across successive generations during the evolutionary process.

Fitness function:
The fitness function is integral to the algorithm, as it determines the fitness of each genotype within the population. The specific version of the algorithm dictates the nature of this function, which is executed to evaluate the fitness of the genotype based on predefined criteria or objectives.

Selection:
Based on the top N parents. Selection involves identifying the top N parents from the current population based on their fitness scores. These parents are chosen as candidates for reproduction and contribute to the next generation's genetic makeup.

Crossover:
After separating the genotype for all the parents, we equally swap the sections over randomly until the number of children is satisfied. In the mutation function. In other words, during the crossover process, the genotypes of selected parents are divided into sections, and these sections are randomly exchanged among parent genotypes to generate offspring. This process ensures genetic diversity among the offspring while maintaining certain characteristics inherited from the parents.

Mutation:
Part of the mutation function where it calls the mutation list function for half of the new generation where it randomly swaps a binary number.

Other operations:


Plots: 
Plot showing the max fitness to the generation number using matplotlib.

Description of results:
look at graphs for 1.1A.png, 1.2A.png and 1.3A.png. Looking at them graphs we can see our results reach the optimal solution getting up to 30 in 1.1, and 29 on 1.2 and 1.3

Sources: N/A

Information on 1.1 running: Please look at 1.1.png.

Information on 1.2 running: Please look at 1.2.png.

Information on 1.3 running: Please look at 1.3.png.
2 B

Representation of Solutions:
The solutions are represented as lists of integers, where each integer represents a bin number. The length of the list corresponds to the number of items, and each item's bin assignment is determined by its corresponding integer in the list. The bin list corresponds to the weight list.

Fitness Function and Operators:
Fitness Function: The fitness function (fitness_fun) evaluates a solution's fitness based on the count of specific values in the list of integers representing bin assignments. It aims to find solutions where each bin contains items where their total weight doesn't exceed 1000, corresponding to a balanced bin packing.
Operators: The main operator used in the code is the mutation operator (mutate_list), which randomly changes the bin assignment of each item within a solution. This operator introduces diversity into the population of solutions and allows exploration of different bin configurations.

Insights into the Problem Landscape:
The problem landscape is characterized by discrete and combinatorial nature due to the bin packing problem. Each solution represents a specific arrangement of items into bins, and the fitness landscape is likely rugged with numerous local optima. The fitness landscape favors solutions where items are evenly distributed among the bins, balancing the load across bins to achieve an optimal bin packing configuration. The challenge lies in efficiently exploring this landscape to find solutions that satisfy the bin packing constraints.

Information on 2B running: Please look at 2B.png
