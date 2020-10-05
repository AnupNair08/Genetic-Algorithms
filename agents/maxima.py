import numpy as np
import matplotlib.pyplot as plt

populationSize = int(input('Enter population size:\n'))       
genomeSize = 10            
rangeVal = [0, 10]         

#Hyperparameters to decide the rate of crossover and mutation
CROSS_RATE = 0.7         
MUTATION_RATE = 0.004    

def generateFunc(x): 
    return np.sin(5*x)*x + np.cos(2*x)*x     

#Fitness heuristic here is the differene in values between the minimum value and other values
#Maximum fitness score is returned 
def fitness(genome): 
    return genome + 1e-3 - np.min(genome)


# convert binary DNA to decimal and normalize it to a range(0, 10)
def normDNA(pop):
    return pop.dot(2 ** np.arange(genomeSize)[::-1]) / float(2**genomeSize-1) * rangeVal[1]


def select(pop, fitness):    
    ind = np.random.choice(np.arange(populationSize), size=populationSize, replace=True,p=fitness/fitness.sum())
    return pop[ind]


def crossover(parent, pop):     
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, populationSize, size=1)                             
        cross_points = np.random.randint(0, 2, size=genomeSize).astype(np.bool)   
        parent[cross_points] = pop[i_, cross_points]                           
    return parent


def mutate(child):
    for point in range(genomeSize):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child

if __name__ == "__main__":
    #Plotting the initial function that is generated and normalised
    plt.ion()       
    x = np.linspace(*rangeVal, 200)
    plt.plot(x, generateFunc(x))

    #Create the initial population
    pop = np.random.randint(2, size=(populationSize, genomeSize)) 


    #Iterate for a set of generations
    for i in range(150):
        F_values = generateFunc(normDNA(pop))  

        #Get all the values for the functions and scatter plot them
        if 'sca' in globals(): 
            sca.remove()
        sca = plt.scatter(normDNA(pop), F_values, s=200, lw=0, c='green', alpha=0.5); plt.pause(0.1)

        #Calculate fitness and perform selection, crossover and mutation.
        fitnessVal = fitness(F_values)
        print("Generation {}: {}".format(i,pop[np.argmax(fitnessVal), :]))
        pop = select(pop, fitnessVal)
        pop_copy = pop.copy()
        for parent in pop:
            child = crossover(parent, pop_copy)
            child = mutate(child)
            parent[:] = child       

    plt.ioff()
    plt.show()