# Genetic-Algorithms (Project work for the course CT-17001)

Genetic Algorithms are a class of heuristics for solving optimization and search based problems based on **Darwin's Theory of Natural Selection.** The crux of the algorithm is "_Fittest survive_" and it uses this as the central idea in problem solving. The algorithms employ a series of steps like mutation, selection and crossover which eventually run until there is convergence of the population. The population size remains static and hence the less fit species eventually die and the fitter ones are given opportunity to propogate into the next generation.

## Biological overview of Genetic Algorithms

The idea behind Natural Selection is summarized collectively as follows:
* An initial population of species is given.
* The individuals that survive from this population are said to have superior genes.
* These are passed onto the next generation resulting in more mutations due to crossovers.
* The individuals with superior genes are selected for the next generation.
* The end result is a set of individuals that have superior genes which evolved over time.


## Formulation of Genetic Algorithms into Problem Solving Agents

The basic goal of using genetic algorithms is to simulate an artificially intelligent agent that can be used to solve or optimize faster. The state space in any problem can be viewed as a set of individuals in a generation. Every individual is represented as a chromosome(vector of varying parameters). The varying parameters are basically the genes of the individual. The collection of individuals together forms the population of a generation. Idividuals(chromosomes) represent solutions and thus the best individual(fittest) is chosen to the next generation.

#### Transition model operators
On generation of a population one of the following methods can be used to create the next successive population:
1. **Selectors**: Selectors choose the individuals(solutions) with the best fitness score.
2. **Crossovers**: Mating between two fit individuals to produce an offspring with better fitness.
3. **Mutation**: Changing genes(variables) in a random manner to prevent premature convergence of the solution space.

#### To summarize:

```
State Space : Population
Initial State : Generation 0
Transition model : Natural Selection(Selection of fittest)
Goal test : Convergence of population fitness
Goal state : Desired final state of the problem
```

## Agents specifications to be added soon

##### Agent 1: Word matching 
The algorithm is used to generate a string pattern by repeatedly doing crossovers and selections. The agent here has to find the target string by deciding for itself which choice of strings will lead to the goal. The initial population is the state space and then the agent does crossovers and mutations to select the fittest from each generation until the goal is reached. We define a fitness function that computes the number of mismatched characters and serves as a heuristic for the problem.

## Algorithm
The basic outline of the algorithm is as follows:
```
1. Initialize initial population
2. Assign fitness to each individual
3. While population does not converge:
        select fittest individuals
        crossover of fittest individuals
        mutation of individuals
        calculate new fitness values 
```