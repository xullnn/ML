import numpy as np
from matplotlib import pyplot as plt
import random
import utils

features = np.array([1,2,3,5,6,7])
labels = np.array([155,197,244,356,407,448])

utils.plot_points(features, labels)

def square_trick(base_price, price_per_room, num_rooms, price, learning_rate):
  predicated_price = base_price + price_per_room * num_rooms
  price_per_room += learning_rate * num_rooms * (price - predicated_price)
  base_price += learning_rate * (price - predicated_price)
  return price_per_room, base_price

import random

random.seed(0)

def linear_regression(features, labels, learning_rate = 0.1, epochs = 1000):
  price_per_room = random.random()
  base_price = random.random()

  for epoch in range(epochs):
    if epoch <= 50:
      utils.draw_line(price_per_room, base_price, starting=0, ending=8)

    i = random.randint(0, len(features) - 1)
    num_rooms = features[i]
    price = labels[i]
    price_per_room, base_price = square_trick(base_price, price_per_room, num_rooms, price, learning_rate = learning_rate)


  utils.draw_line(price_per_room, base_price, 'black', starting=0, ending=8)
  utils.plot_points(features, labels)
  print("Price per room:", price_per_room)
  print("Base price:", base_price)
  return price_per_room, base_price

plt.ylim(0, 500)

linear_regression(features, labels, learning_rate=0.01, epochs=20)
plt.show()

