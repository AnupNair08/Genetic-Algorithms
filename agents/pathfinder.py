import numpy as np
import matplotlib.pyplot as plt

populationSize = int(input('Enter population size:\n'))
generations = 200

#Hyperparameters for mutation and crossover
CROSS_RATE = 0.7
MUTATE_RATE = 0.001

#The state space consisting of a 2D grid with start point end point and obstacle
class environment():
    def __init__(self,start,end,obs):
        self.start = start
        self.end = end
        self.obs = obs

    def plotenv(self):
        plt.scatter(*self.start)
        plt.scatter(*self.end)
        plt.plot([self.obs[0][0],self.obs[1][0]],[self.obs[0][1],self.obs[1][1]])
        plt.ion()
        # plt.show()


#Normalise population and convert into [0,.25]
def normPop(population,start,region):
    population = (population - 0.5 )/ 2
    population[:, 0], population[:, region] = start[0], start[1]
    x = np.cumsum(population[:,region:],axis = 1)
    y = np.cumsum(population[:,:region], axis = 1)
    return x,y

def fitness(x,y,goal,obs):
    #Eucildean distance of all points on the lines followed by normalising in [0,1]
    dist = ((x[:,-1] - goal[0])**2 + (y[:,-1] - goal[1])**2)**0.5
    score = np.power(1/(1+dist) , 2)
    points = (x > obs[0][0] - 0.5) & (x < obs[1][0] + 0.5)
    y_values = np.where(points, y, np.zeros_like(y) - 100)
    #Avoiding obstacles and assigning low value to crossing population
    bad_lines = ((y_values > obs[0][1]) & (y_values < obs[1][1])).max(axis=1)
    score[bad_lines] = 1e-6
    return score

#Randomly choose fit individuals from the population
def select(population, fitness):
    ind = np.random.choice(np.arange(populationSize), size=populationSize, replace=True,p=fitness/fitness.sum())
    return population[ind]

#Crossover with a parent and a random fit individual
def crossover(parent, population, size):
    if np.random.rand() < CROSS_RATE:
        i = np.random.randint(0, populationSize, size=1) 
        cross_points = np.random.randint(0, 2, size).astype(np.bool)   
        parent[cross_points] = population[i, cross_points]          
    return parent

#Mutate the gene with a random bit
def mutate(child,size):
    for i in range(size):
        if np.random.rand() < MUTATE_RATE:
            child[i] = np.random.randint(2)
    return child

if __name__ == "__main__":
    
    region = 100  #Region length to be convered by the lines

    start = [0,0]
    goal = [1,8]
    obs = [[1.5,-2.5] , [1.5,5]]

    #Initialize the population and the environment
    env = environment(start,goal,obs)
    population = np.random.randint(2, size=(populationSize, region*2))


    #Fitness -> Selection -> crossover -> mutate
    for i in range(generations):
        x,y = normPop(population,[0,0],region)
        fitnessVal = fitness(x,y,goal, obs)
        population = select(population,fitnessVal)
        for individual in population:
            child = crossover(individual,population,region*2)
            child = mutate(child,region*2)
            individual[:] = child
        print("Generation : {} | Fitness : {}".format(i,np.argmax(fitnessVal)))
        plt.cla()
        env.plotenv()
        plt.plot(x.T, y.T,c="r")
        plt.xlim((-5, 10))
        plt.ylim((-5, 10))
        plt.pause(0.001)
    
    plt.ioff()   
    plt.show()