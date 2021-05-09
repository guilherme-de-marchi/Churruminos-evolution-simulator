import objects.churrumino
import objects.members
import objects.food
import simulationEnvironment.map

mapa = simulationEnvironment.map.Map((10, 10))
carlito = objects.churrumino.Churrumino(
    objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
    objects.members.Body((0.6, 0.2, 0.5), 3, 100),
    objects.members.Legs((0.01, 1, 0.01), 0.05),
    objects.members.Eyes((0.05, 0.05, 0.05), 0.01),
    0,
    mapa
)

mapa.setPosition((7, 0), carlito)
carlito.walk((-1, 0))

print(mapa)

'''
print('Carlito\nGasto de energia por movimento: {}\nBeleza: {}\nCapacidade maxima de geração de proli: {}\nCapacidade maxima de armazenamento de energia: {}\nVelocidade máxima: {}\nRaio de visao: {}'.format(
    carlito.ENERGY_EXPENDITURE_PER_MOVIMENT,
    carlito.attractiveness,
    carlito.reproductive_organ.MAXIMUM_GENERATION_CAPACITY,
    carlito.body.ENERGY_STORAGE_CAPACITY,
    carlito.legs.MAXIMUM_SPEED,
    carlito.eyes.VISION_RANGE
))
'''