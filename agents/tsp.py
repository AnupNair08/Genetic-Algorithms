import numpy as np
import matplotlib.pyplot as plt

populationSize = int(input('Enter population size:\n'))
city_no = int(input('Enter number of cities:\n'))
# Hyperparamters to control rate of crossover and mutaiton
CROSS_RATE = 0.2
MUTATE_RATE = 0.06


class environment:
    cities = []

    def __init__(self, cities):
        self.cities = np.random.rand(cities, 2)

    def plot(self):
        plt.cla()
        plt.scatter(self.cities[:, 0].T, self.cities[:, 1].T, s=100)
        plt.ion()

# DNA contains city numbers that have respective coordinates
# city = (x,y)
# city[,:0] = all elements along first column i.e x coords
# city[:,1] = all elements along second column i.e y coords
# x and y are NX1 numpy arrays
# Return lines joining the cities


def getRoutes(DNA, cities):
    # create temp lines of the same shape and datatype as DNA(cities)
    x = np.empty_like(DNA, dtype="float64")
    y = np.empty_like(DNA, dtype="float64")
    for i in range(len(DNA)):
        city = cities[DNA[i]]  # get coords of city number i
        x[i, :] = city[:, 0]
        y[i, :] = city[:, 1]
    return x, y


def fitness(x, y):
    dist = np.empty(x.shape[0], dtype="float64")
    for i in range(len(x)):
        xi, yi = x[i], y[i]
        dist[i] = np.sum(
            np.sqrt(np.square(np.diff(xi)) + np.square(np.diff(yi))))
    score = np.exp(city_no * 2 / dist)
    return score, dist


def select(pop, fitness):
    ind = np.random.choice(np.arange(
        populationSize), size=populationSize, replace=True, p=fitness/fitness.sum())
    return pop[ind]


def crossover(parent, pop):
    if(np.random.rand() < CROSS_RATE):
        i = np.random.randint(0, populationSize, size=1)
        cross_points = np.random.randint(0, 2, city_no).astype(np.bool)
        # calculate the city number that is better and swap with the non best city
        keep_city = parent[~cross_points]
        swap_city = pop[i, np.isin(pop[i].ravel(), keep_city, invert=True)]

        parent[:] = np.concatenate((keep_city, swap_city))
    return parent


def mutate(child):
    for i in range(city_no):
        if(np.random.rand() < MUTATE_RATE):
            j = np.random.randint(0, city_no)
            a, b = child[i], child[j]
            child[i], child[j] = b, a
    return child


if __name__ == "__main__":
    print('Travelling Salesman simulation')
    e = environment(city_no)
    # numpy array that is an array of random permutation of integers from 0 to size
    population = np.vstack([np.random.permutation(city_no)
                            for _ in range(populationSize)])
    for i in range(200):
        x, y = getRoutes(population, e.cities)
        fit, score = fitness(x, y)
        population = select(population, fit)
        for parent in population:
            child = crossover(parent, population)
            child = mutate(child)
            parent[:] = child
        print('Generation : {} | Optimal distance : {} \nFitness: {}'.format(
            i, score[np.argmax(fit)], fit[np.argmax(fit)]))
        plt.cla()
        e.plot()
        plt.plot(x[np.argmax(fit)].T, y[np.argmax(fit)].T, 'r-')
        plt.xlim((-0.1, 1.1))
        plt.ylim((-0.1, 1.1))
        plt.pause(0.01)

    plt.ioff()
    plt.show()
