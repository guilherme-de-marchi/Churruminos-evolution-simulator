from time import sleep
import random

import objects.churrumino
import objects.food
import simulationEnvironment.map
import simulationEnvironment.window

mapa = simulationEnvironment.map.Map((40, 20), '.')

spawned = {
    'churrumino': [
        objects.churrumino.Churrumino(
            objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
            objects.members.Body((0.6, 0.2, 0.5), 3),
            objects.members.Legs((0.01, 1, 0.01), 0.05),
            0,
            '#',
            mapa
        ),
        objects.churrumino.Churrumino(
            objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
            objects.members.Body((0.6, 0.2, 0.5), 3),
            objects.members.Legs((0.01, 1, 0.01), 0.05),
            0,
            'O',
            mapa
        ),
        objects.churrumino.Churrumino(
            objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
            objects.members.Body((0.6, 0.2, 0.5), 3),
            objects.members.Legs((0.01, 1, 0.01), 0.05),
            0,
            'M',
            mapa
        ),
        objects.churrumino.Churrumino(
            objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
            objects.members.Body((0.6, 0.2, 0.5), 3),
            objects.members.Legs((0.01, 1, 0.01), 0.05),
            0,
            '@',
            mapa
        ),
    ],
    'food': [
        objects.food.Food(10, '^') for i in range(30)
    ],
}

for object_group in spawned.values():
    for object in object_group:
        mapa.setPosition((random.randint(0, mapa.SIZE[0]-1), random.randint(0, mapa.SIZE[1]-1)), object)

window = simulationEnvironment.window.Window()

while True:
    for churrumino in spawned['churrumino']:
        what_need = churrumino.whatNeed()

        if churrumino.target == None:
            churrumino.target = random.choice(spawned[what_need])
            continue
            
        if churrumino.target in spawned[what_need]:
            churrumino.walk(churrumino.goTo(churrumino.target))
        
        else:
            churrumino.target = None
            continue

        if churrumino.position == churrumino.target.position:
            churrumino.useTarget()

            if what_need == 'food':
                spawned[what_need].remove(churrumino.target)

            churrumino.target = None

    window.print(
        mapa.rendered(),
        str(spawned['churrumino'][1].body.ENERGY_STORAGE_CAPACITY),
        str(spawned['churrumino'][1].body.stored_energy),
        str(spawned['churrumino'][1].whatNeed()),
    )
    sleep(.1)