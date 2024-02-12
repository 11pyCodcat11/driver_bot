import osmnx as ox

graph = ox.graph_from_place('Moscow oblast, Russia', network_type='drive')

nodes = list(graph.nodes.keys())

file = open('C:\\Users\\tvasi\\OneDrive\Рабочий стол\\tim_py.cod\\Cods\\VSC\\driver_bot\\Moscow.txt','w')
for node in nodes:
    file.write(str(node) + "\n")
file.close()

print("Список всех точек сохранен в файл Moscow.txt")