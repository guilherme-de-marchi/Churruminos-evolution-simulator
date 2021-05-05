import objects
import simulationEnvironment

carlito = objects.churrumino.Churrumino(
    objects.members.ReproductiveOrgan((0.2, 0.1, 0.1), 0.3),
    objects.members.Body((0.6, 0.2, 0.5), 3, 100),
    objects.members.Legs((0.01, 1, 0.01), 0.05),
    objects.members.Eyes((0.05, 0.05, 0.05), 0.01),
    0
)

mapa = simulationEnvironment.map.Map((10, 10))
mapa.setPosition((0, 0), carlito)

for linha in mapa.map:
    print(linha)

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