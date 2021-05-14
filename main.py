from time import sleep
import random

import objects.churrumino
import objects.food
import simulationEnvironment.map
import simulationEnvironment.window

mapa = simulationEnvironment.map.Map((40, 20), '.')

objects_spawned = {
    'churruminos': [
        objects.churrumino.Churrumino(
            objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
            objects.members.Body((0.6, 0.2, 0.5), 3, 10),
            objects.members.Legs((0.01, 1, 0.01), 0.05),
            0,
            '#',
            mapa
        ),
        objects.churrumino.Churrumino(
            objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
            objects.members.Body((0.6, 0.2, 0.5), 3, 10),
            objects.members.Legs((0.01, 1, 0.01), 0.05),
            0,
            '@',
            mapa
        ),
    ],
    'foods': [
        objects.food.Food(1, 'A'),
        objects.food.Food(1, 'B'),
        objects.food.Food(1, 'C'),
        objects.food.Food(1, 'D'),
        objects.food.Food(1, 'E'),
        objects.food.Food(1, 'F'),
        objects.food.Food(1, 'G'),
        objects.food.Food(1, 'H'),
        objects.food.Food(1, 'I'),
    ],
}

for object_group in objects_spawned.values():
    for object in object_group:
        mapa.setPosition((random.randint(0, mapa.SIZE[0]-1), random.randint(0, mapa.SIZE[1]-1)), object)

window = simulationEnvironment.window.Window()

while True:
    for churrumino in objects_spawned['churruminos']:
        if not churrumino.target:
            if churrumino.whatNeed() == 'food':
                churrumino.target = random.choice(objects_spawned['foods'])
            
        else: 
            if churrumino.position == churrumino.target.position:
                churrumino.target = None

            else:
                churrumino.walk(churrumino.goTo(churrumino.target))

    window.print(mapa.render())
    sleep(.1)