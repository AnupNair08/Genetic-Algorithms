import random
target = input('Enter target string:\n')

# All possible generation size
gene = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
populationSize = int(input('Enter population size:\n'))

# Function to calculate the fitness score of each individual


def fitness(genome):
    score = 0
    for i in range(len(genome)):
        if(genome[i] != target[i]):
            score += 1
    return score

# Function to randomly mutate the gene of a individual


def mutate():
    global gene
    genome = ''
    for _ in range(len(target)):
        genome += (random.choice(gene))
    return genome

# Function that produces an offspring from two differnt parents


def crossover(p1, p2):
    child = ''
    for _ in range(len(p1)):
        p = random.random()
        if(p < 0.5):
            child += p1[i]
        elif(p > 0.9):
            child += p2[i]
        else:
            child += random.choice(gene)
    return child


if __name__ == "__main__":
    print('Word Matcher simulation')

    # A tunable hyper parameter in [0,1] that can be varied to select max number of fittest individuals without crossovers
    hyperParam = 0.2

    generation = 0
    finish = 0
    population = []
    # generate the initial population
    for i in range(populationSize):
        population.append(mutate())

    while not finish:
        # Lower the fitness score fitter the individual
        population = sorted(population, key=lambda x: fitness(x))
        # Match found
        if(fitness(population[0]) == 0):
            finish = 1
            print(generation, population[0], fitness(population[0]))
            break
        # Create the new generation by selection and crossover
        newgen = []
        for i in range(int(hyperParam * populationSize)):
            newgen.append(population[i])
        for i in range(int((1 - hyperParam) * populationSize)):
            p1 = random.choice(population[:50])
            p2 = random.choice(population[:50])
            newgen.append(crossover(p1, p2))
        population = newgen
        print(generation, population[0], fitness(population[0]))
        generation += 1

    print("Computed matching string in {} generations" .format(generation))
