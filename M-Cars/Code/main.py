import time
from Cars import *
from search import *

f = open('date_4.txt', 'w')

def main():
    marime_parcare =4
    marime_parcare_aux = marime_parcare

    date_intrare = list()  # initial_state
    date_iesire = list()  # goal_state
    for i in range(marime_parcare):
        date_intrare.append(i + 1)
    for i in range(marime_parcare * (marime_parcare - 1)):
        date_intrare.append(0)
    for i in range(marime_parcare * (marime_parcare - 1)):
        date_iesire.append(0)
    for i in range(marime_parcare):
        date_iesire.append(marime_parcare_aux)
        marime_parcare_aux -= 1
    carsMiss=CarsMiss(tuple(date_intrare), marime_parcare, tuple(date_iesire))
    carsMht=CarsMht(tuple(date_intrare), marime_parcare, tuple(date_iesire))
    t1 = time.time()
    path = depth_first_graph_search(carsMht)
    t2 = time.time()
    t = t2 - t1
    # pentru marime_parcare <=4 path se calculeaza cu astear_search si folosim tot distanta Manhattan pentru a face comparatie cu depth_first_graph_search(carsMht)
    #pentru marime_parcare>4 path se calculeaza cu depth_first_graph_search si  Funcția euristică implicită utilizată este
    #          h (n) = numărul de plăci greșite
    f.write("\nFolosind Depth_first_graph_search")
    f.write("\nDimensiunea parcarii este : " + str(marime_parcare) + "x" + str(marime_parcare))
    f.write("\nStarea initiala este: " + str(tuple(date_intrare)))
    f.write("\nObiectivul este: " + str(tuple(date_iesire)))
    f.write("\nActiunile executate cu ajutorul Missplaced Tiles sunt: " +str(path.solution()))
    f.write("\nTimpul executat este de " + str(t) + "s")
    f.write("\nCostul caii (Manhatten distance ) este: " + str(path.path_cost))

    t1 = time.time()
    path2 = astar_search(carsMht)
    t2 = time.time()
    t = t2 - t1
    f.write("\nFolosind Depth_first_graph_search")
    f.write("\nDimensiunea parcarii este : " + str(marime_parcare) + "x" + str(marime_parcare))
    f.write("\nStarea initiala este: " + str(tuple(date_intrare)))
    f.write("\nObiectivul este: " + str(tuple(date_iesire)))
    f.write("\nActiunile executate cu ajutorul Distantei Manhattan  sunt: " + str(path2.solution()))
    f.write("\nTimpul executat este de " + str(t) + "s")
    f.write("\nCostul caii este: " + str(path2.path_cost))

"""
    compare_searchers(problems=[carsMht, carsMht],
                      header=['Searcher', 'A* h1(n)',
                              'A* h2(n)'], searchers=[
           depth_first_graph_search,
           astar_search])"""

if __name__ == "__main__":
    main()

