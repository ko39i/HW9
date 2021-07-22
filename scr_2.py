import pickle
import statistics

file = open("task2", "rb")
obj = pickle.load(file)
print(type(obj))
print(obj)
print(statistics.mean(obj))

file.close()



