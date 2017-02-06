import numpy as np
import matplotlib.pyplot as plt

# movielens1m data
# collrank method on illidan server
# lambda = 5000, rank = 100
# iteration, training time (sec), objective function, pairwise error, ndcg@10
c_1t = [
[0, 0.014226, 25494550.188233, 0.356036, 0.457780],
[1, 31.899794, 18070075.054893, 0.204608, 0.745929],
[2, 63.818527, 18003042.186983, 0.202303, 0.748551],
[3, 95.764201, 17941598.161777, 0.198654, 0.758924],
[4, 127.712485, 17795889.030501, 0.191464, 0.770918],
[5, 159.593582, 17747357.739165, 0.188805, 0.777788],
[6, 191.480352, 17700173.424462, 0.185636, 0.785190],
[7, 223.383548, 17670627.306505, 0.183271, 0.790773],
[8, 255.260254, 17658315.151481, 0.181983, 0.794647],
[9, 287.112158, 17651657.855200, 0.181323, 0.797104],
[10, 318.963556, 17647637.443278, 0.181058, 0.797377],
[11, 350.816773, 17645063.647047, 0.180819, 0.798198],
[12, 382.784562, 17643224.088021, 0.180650, 0.798650],
[13, 414.794234, 17641906.343370, 0.180537, 0.798840],
[14, 446.792886, 17640992.346403, 0.180409, 0.798986],
[15, 478.783363, 17640355.917973, 0.180343, 0.798981],
[16, 510.805560, 17639894.213451, 0.180290, 0.799042],
[17, 542.777494, 17639542.296452, 0.180277, 0.798968],
[18, 574.638806, 17639265.309337, 0.180208, 0.799136],
[19, 606.493601, 17639045.335300, 0.180220, 0.798965],
[20, 638.350998, 17638871.221516, 0.180196, 0.799108]
]

c_4t = [
[0, 0.014327, 25483557.632731, 0.354829, 0.465013],
[1, 14.994168, 18069937.928872, 0.204624, 0.746822],
[2, 31.071499, 18002675.279658, 0.202333, 0.748651],
[3, 48.749428, 17939413.945008, 0.198546, 0.759457],
[4, 65.328401, 17793011.032526, 0.191254, 0.770923],
[5, 82.204156, 17742840.018412, 0.188454, 0.778238],
[6, 98.890669, 17697475.429573, 0.185386, 0.785927],
[7, 115.334921, 17670919.519497, 0.183306, 0.790218],
[8, 131.884471, 17659118.369818, 0.182103, 0.794139],
[9, 148.121683, 17652351.617632, 0.181479, 0.796630],
[10, 164.427761, 17648027.556925, 0.181093, 0.797248],
[11, 180.094690, 17645351.249259, 0.180904, 0.797937],
[12, 196.768542, 17643577.815064, 0.180754, 0.798455],
[13, 212.687606, 17642316.131606, 0.180525, 0.798626],
[14, 228.679155, 17641398.691386, 0.180446, 0.798797],
[15, 245.325215, 17640733.745310, 0.180331, 0.799046],
[16, 261.583989, 17640244.852639, 0.180349, 0.799148],
[17, 278.093859, 17639861.799938, 0.180293, 0.799114],
[18, 294.458553, 17639548.942396, 0.180290, 0.798994],
[19, 310.466980, 17639290.948105, 0.180270, 0.798986],
[20, 326.164057, 17639069.846367, 0.180204, 0.798905]
]

c_8t = [
[0, 0.014691, 25457082.406247, 0.349212, 0.501290],
[1, 9.308171, 18070303.227007, 0.204666, 0.746574],
[2, 18.801602, 18002946.540883, 0.202337, 0.747594],
[3, 28.317024, 17942057.093120, 0.198666, 0.758964],
[4, 37.888555, 17795084.124201, 0.191438, 0.770610],
[5, 47.399776, 17744491.996983, 0.188571, 0.777981],
[6, 56.901890, 17698438.356250, 0.185463, 0.785918],
[7, 66.256884, 17670247.285813, 0.183259, 0.790819],
[8, 75.515892, 17658625.709414, 0.182074, 0.794144],
[9, 84.949537, 17651967.635091, 0.181413, 0.796245],
[10, 93.946702, 17647538.031336, 0.181025, 0.797369],
[11, 103.056750, 17644835.803942, 0.180805, 0.798029],
[12, 111.861487, 17643117.489505, 0.180650, 0.798749],
[13, 121.181189, 17641936.037146, 0.180486, 0.798651],
[14, 130.471636, 17641112.038778, 0.180387, 0.798644],
[15, 139.716131, 17640509.749607, 0.180357, 0.798951],
[16, 149.081767, 17640043.374561, 0.180274, 0.799033],
[17, 158.847670, 17639683.366726, 0.180231, 0.798943],
[18, 168.255120, 17639391.769698, 0.180253, 0.799203],
[19, 177.308082, 17639161.188733, 0.180204, 0.799016],
[20, 186.802298, 17638972.001939, 0.180161, 0.798988]
]


# our method
w_1c = [
[0, 0.0, 3.4923972344709754e7, 0.3510205089577718, 0.4753335862187586],
[1, 5.332196085, 2.065018648247157e7, 0.23643604844121305, 0.733801658808334],
[2, 13.091907170999999, 1.7919937083181847e7, 0.1927016951718535, 0.7781138146180607],
[3, 21.811701022, 1.7707365601119094e7, 0.18474258794462156, 0.7910377289550884],
[4, 31.334984936, 1.7663148705281977e7, 0.18201973339141664, 0.796294944993741],
[5, 40.746903716000006, 1.764978595047792e7, 0.1809857839424875, 0.7980915688394775],
[6, 49.387522897000004, 1.7644575966865093e7, 0.18045180573422978, 0.7994476981028341],
[7, 58.007118238000004, 1.7642084638151847e7, 0.1802438940370599, 0.7994307352179486],
[8, 65.99910661, 1.764072544686018e7, 0.1801828890743176, 0.7995226071699875],
[9, 73.874508049, 1.7639913387628738e7, 0.18009714037256452, 0.7994483908820548],
[10, 81.066998735, 1.7639394567674518e7, 0.18006125722267952, 0.7995192587547784],
[11, 88.963728929, 1.7639045468658887e7, 0.18004377492931398, 0.7993668362434537],
[12, 96.111140754, 1.7638800772987466e7, 0.1800488808296141, 0.7993365503582156],
[13, 103.38127204700001, 1.763862346178225e7, 0.18003996064359473, 0.7992946859162385],
[14, 110.657706821, 1.763849138721964e7, 0.18002141814511022, 0.7993777123325684],
[15, 117.92603502300001, 1.763839069198585e7, 0.1800447959942229, 0.7993090974153798],
[16, 125.15525162000002, 1.7638312377446912e7, 0.18005663149272694, 0.7992865959409045],
[17, 132.34415090500002, 1.7638250413392056e7, 0.18006222649187578, 0.7992638469850094],
[18, 139.55790316500003, 1.7638200646258056e7, 0.18006452751016358, 0.7994079770398347],
[19, 146.67374746300004, 1.7638160146403465e7, 0.180072617302539, 0.799448248521254],
[20, 153.82586990900003, 1.763812680276606e7, 0.1800671486306438, 0.7994139929314301]
]

# Avoid |Omega| complexity by exploiting training data only has rating
w2_1c = [
[0, 0.0, 3.4923972344714075e7, 0.3510205089577718, 0.4753335862187586],
[1, 3.890737663, 2.0650186482471567e7, 0.23643604844121305, 0.733801658808334],
[2, 9.871741794, 1.7919937083181843e7, 0.1927016951718535, 0.7781138146180607],
[3, 16.307962327, 1.7707365601119082e7, 0.18474258794462156, 0.7910377289550884],
[4, 23.579663728, 1.7663148705281988e7, 0.18201973339141664, 0.796294944993741],
[5, 30.033057022, 1.7649785950477924e7, 0.1809857839424875, 0.7980915688394775],
[6, 35.415093025000004, 1.7644575966865093e7, 0.18045180573422978, 0.7994476981028341],
[7, 41.291073448000006, 1.764208463815185e7, 0.1802438940370599, 0.7994307352179486],
[8, 46.59924277100001, 1.7640725446860168e7, 0.1801828890743176, 0.7995226071699875],
[9, 51.662319999000005, 1.7639913387628738e7, 0.18009714007327338, 0.7994483908820548],
[10, 56.594536711, 1.7639394567674506e7, 0.18006125722267952, 0.7995192587547784],
[11, 61.765958399000006, 1.7639045468658887e7, 0.18004377492931398, 0.7993668362434537],
[12, 66.675016196, 1.7638800772987455e7, 0.1800488808296141, 0.7993365503582156],
[13, 71.698221738, 1.7638623461782254e7, 0.18003996064359473, 0.7992946859162385],
[14, 75.916974961, 1.7638491387219645e7, 0.18002141814511022, 0.7993777123325684],
[15, 80.132229568, 1.7638390691985846e7, 0.1800447959942229, 0.7993090974153798],
[16, 84.29285501, 1.7638312377446916e7, 0.18005663149272694, 0.7992865959409045],
[17, 89.019792915, 1.763825041339206e7, 0.18006222649187578, 0.7992638469850094],
[18, 94.230977895, 1.763820064625806e7, 0.18006452751016358, 0.7994079770398347],
[19, 99.580065769, 1.7638160146403477e7, 0.180072617302539, 0.799448248521254],
[20, 104.26664986, 1.7638126802766066e7, 0.1800671486306438, 0.7994139929314301]
]

w_4c = [
[0, 0.0, 3.492397234471353e7, 0.3510205089577718, 0.4753335862187586],
[1, 2.572523551, 2.0650186482471563e7, 0.23643604844121305, 0.733801658808334],
[2, 6.13738894, 1.7919937083181813e7, 0.1927016951718535, 0.7781138146180607],
[3, 10.343473899, 1.770736560111908e7, 0.18474258794462156, 0.7910377289550884],
[4, 15.140543381999999, 1.766314870528199e7, 0.18201973339141664, 0.796294944993741],
[5, 19.736707367999998, 1.7649785950477928e7, 0.1809857839424875, 0.7980915688394775],
[6, 23.911522956, 1.7644575966865066e7, 0.18045180573422978, 0.7994476981028341],
[7, 28.016793921999998, 1.7642084638151824e7, 0.1802438940370599, 0.7994307352179486],
[8, 31.802699206999996, 1.7640725446860146e7, 0.1801828890743176, 0.7995226071699875],
[9, 35.575490783, 1.763991338762876e7, 0.18009714037256452, 0.7994483908820548],
[10, 38.952303334, 1.7639394567674503e7, 0.18006125692338834, 0.7995192587547784],
[11, 42.750670927, 1.7639045468658876e7, 0.18004377492931398, 0.7993668362434537],
[12, 46.297971587, 1.763880077298745e7, 0.1800488808296141, 0.7993365503582156],
[13, 49.887858613, 1.763862346178225e7, 0.18003996064359473, 0.7992946859162385],
[14, 53.334286653, 1.7638491387219645e7, 0.18002141814511022, 0.7993777123325684],
[15, 56.809931562, 1.7638390691985823e7, 0.1800447959942229, 0.7993090974153798],
[16, 60.281148256, 1.7638312377446935e7, 0.18005663149272694, 0.7992865959409045],
[17, 63.803169374, 1.7638250413392063e7, 0.18006222649187578, 0.7992638469850094],
[18, 67.116502008, 1.7638200646258082e7, 0.18006452751016358, 0.7994079770398347],
[19, 70.373956018, 1.763816014640346e7, 0.180072617302539, 0.799448248521254],
[20, 73.83482356500001, 1.763812680276607e7, 0.1800671486306438, 0.7994139929314301]
]

w_8c = [
[0, 0.0, 3.4923972344713524e7, 0.3510205089577718, 0.4753335862187586],
[1, 1.934896184, 2.065018648247156e7, 0.23643604844121305, 0.733801658808334],
[2, 4.921051885, 1.7919937083181817e7, 0.1927016951718535, 0.7781138146180607],
[3, 8.024466873, 1.7707365542990938e7, 0.18474251261588157, 0.7910377289550884],
[4, 11.317003322, 1.766314868911016e7, 0.18201982618260037, 0.796294944993741],
[5, 14.866951335, 1.7649789502899703e7, 0.18098548826277125, 0.7981135183955234],
[6, 18.266708142, 1.7644576390812118e7, 0.18045107544637698, 0.7994459612227653],
[7, 21.793615099, 1.764208458013668e7, 0.18024374705777516, 0.7994142730509142],
[8, 24.958983028, 1.7640725415179472e7, 0.18018223593060648, 0.7995226071699875],
[9, 28.194104060999997, 1.763991337219656e7, 0.18009706188300162, 0.7994483908820548],
[10, 31.049797970999997, 1.763939456237428e7, 0.18006117103366698, 0.7995192587547784],
[11, 34.198990916999996, 1.7639045469291523e7, 0.18004379459442768, 0.7993668362434537],
[12, 37.268439304, 1.7638806104689427e7, 0.18004681688945276, 0.7993493198496582],
[13, 40.377195907, 1.763862380680913e7, 0.18004067307653185, 0.7992989221356565],
[14, 43.458508791, 1.7638491459850267e7, 0.1800202914351845, 0.7993777123325684],
[15, 46.45219685, 1.7638390740064457e7, 0.18004480644445053, 0.79931045422068],
[16, 49.177108643, 1.763831236607994e7, 0.18005714815307394, 0.7992856257326934],
[17, 52.101614571999995, 1.7638250396311637e7, 0.18006234024079554, 0.7992638469850094],
[18, 55.342836989999995, 1.763820814298926e7, 0.18006678584908736, 0.7994367526330972],
[19, 58.741081769, 1.763816093679012e7, 0.18006884509014087, 0.7994687825732972],
[20, 61.781832503, 1.76381271210646e7, 0.1800693924501682, 0.7994163952425706]
]

# > 8 cores does not increase performance

# data
c_1t = np.array(c_1t)
c_4t = np.array(c_4t)
c_8t = np.array(c_8t)
w_1c = np.array(w_1c)
w_4c = np.array(w_4c)
w_8c = np.array(w_8c)
w2_1c = np.array(w2_1c)

# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,4], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,4], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,4], 'c', label='primal 8 cores')
ax.plot(c_1t[:,1], c_1t[:,4], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,4], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,4], 'm', label='collrank 8 threads')
ax.plot(w2_1c[:,1], w_1c[:,4], 'b', label='primal++ 1 core')
ax.set_title('MovieLens1m, 200 ratings/user, rank 100, lambda = 5000')
ax.set_xlabel('Time')
ax.set_ylabel('NDCG')
ax.axis([0, 200, 0.4, 0.85])
legend = ax.legend(loc='lower right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()

fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,3], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,3], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,3], 'c', label='primal 8 cores')
ax.plot(c_1t[:,1], c_1t[:,3], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,3], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,3], 'm', label='collrank 8 threads')
ax.plot(w2_1c[:,1], w_1c[:,3], 'b', label='primal++ 1 core')
ax.set_title('MovieLens1m, 200 ratings/user, rank 100, lambda = 5000')
ax.set_xlabel('Time')
ax.set_ylabel('Pairwise_Error')
ax.axis([0, 200, 0.15, 0.4])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()


fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,2], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,2], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,2], 'c', label='primal 8 cores')
ax.plot(c_1t[:,1], c_1t[:,2], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,2], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,2], 'm', label='collrank 8 threads')
ax.plot(w2_1c[:,1], w_1c[:,2], 'b', label='primal++ 1 core')
ax.set_title('MovieLens1m, 200 ratings/user, rank 300, lambda = 5000')
ax.set_xlabel('Time')
ax.set_ylabel('Objective_Function')
ax.axis([0, 100, 1.5e7, 4e7])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()









# lambda = 1000, rank = 300
c_1t = [
[0, 0.040943, 21825803.646466, 0.347980, 0.480674],
[1, 64.147222, 14388848.815762, 0.195136, 0.757527],
[2, 127.424883, 9748406.336299, 0.192632, 0.756019],
[3, 189.089222, 8798931.112283, 0.193864, 0.762636],
[4, 252.106122, 8534023.583846, 0.190305, 0.771005],
[5, 315.276446, 8482506.263701, 0.190221, 0.771431],
[6, 376.267024, 8457790.383830, 0.190266, 0.771957],
[7, 437.290968, 8444490.270344, 0.190120, 0.772125],
[8, 502.522509, 8436774.611238, 0.190189, 0.772290],
[9, 570.476003, 8432029.715833, 0.190118, 0.771922],
[10, 638.009784, 8428975.380706, 0.190131, 0.771733],
[11, 704.309711, 8426939.625972, 0.190089, 0.771794],
[12, 771.328187, 8425541.653401, 0.190076, 0.771971]
]

c_4t = [
[0, 0.042510, 21841543.050841, 0.353283, 0.474598],
[1, 24.993024, 14384794.413963, 0.194634, 0.758562],
[2, 51.174556, 9736691.813413, 0.191476, 0.760952],
[3, 76.798166, 8795207.558318, 0.193324, 0.765353],
[4, 102.639535, 8535064.666926, 0.189859, 0.771076],
[5, 128.320098, 8482875.511060, 0.189728, 0.770967],
[6, 153.904350, 8457863.791529, 0.189880, 0.771925],
[7, 179.211830, 8444409.448658, 0.189870, 0.772699],
[8, 204.035656, 8436647.493079, 0.189873, 0.773224],
[9, 229.109934, 8431902.422936, 0.189931, 0.772665],
[10, 254.042182, 8428874.133494, 0.189956, 0.772685],
[11, 279.276947, 8426862.269404, 0.189951, 0.772880],
[12, 304.198080, 8425484.819605, 0.189991, 0.773006],
[13, 328.859982, 8424523.748353, 0.190023, 0.772789],
[14, 353.721561, 8423846.334397, 0.190070, 0.772704],
[15, 379.209778, 8423333.162782, 0.190039, 0.772728],
[16, 404.441363, 8422964.009265, 0.190042, 0.772807],
[17, 428.822811, 8422677.968384, 0.190076, 0.772971],
[18, 454.251723, 8422468.140690, 0.190079, 0.773321],
[19, 479.518567, 8422299.882631, 0.190123, 0.773253],
[20, 504.978962, 8422171.333801, 0.190098, 0.772869]
]
c_8t = [
[0, 0.042283, 21812899.883244, 0.343316, 0.492770],
[1, 15.075399, 14407327.573392, 0.195710, 0.757718],
[2, 30.378366, 9745002.281438, 0.193189, 0.757279],
[3, 45.954996, 8802883.274101, 0.194338, 0.761147],
[4, 61.331029, 8536809.465252, 0.190431, 0.770414],
[5, 76.373427, 8484223.305757, 0.190394, 0.770756],
[6, 91.247650, 8458857.086799, 0.190269, 0.771255],
[7, 106.610865, 8445183.259830, 0.190299, 0.771346],
[8, 122.137733, 8437230.438524, 0.190319, 0.772033],
[9, 137.683732, 8432348.954286, 0.190263, 0.772269],
[10, 152.644165, 8429203.608629, 0.190274, 0.772359],
[11, 167.843415, 8427122.151264, 0.190302, 0.772916],
[12, 183.446838, 8425712.352307, 0.190239, 0.773150],
[13, 198.782475, 8424727.341223, 0.190198, 0.773002],
[14, 214.024120, 8423986.530714, 0.190199, 0.772676],
[15, 229.720527, 8423468.802433, 0.190162, 0.772858],
[16, 244.934965, 8423085.570108, 0.190195, 0.772787],
[17, 260.283703, 8422782.429156, 0.190241, 0.772532],
[18, 275.294305, 8422566.928295, 0.190251, 0.772696],
[19, 290.391209, 8422396.003142, 0.190258, 0.772667],
[20, 305.386285, 8422267.481857, 0.190239, 0.772617]
]

w_1c = [
[0, 0.0, 3.0357818523871504e7, 0.35211772440099826, 0.4753160623163859],
[1, 29.313523892, 1.0682719616912821e7, 0.25859065898671707, 0.691681502978013],
[2, 63.920414653, 9.009262342941739e6, 0.19950706174332203, 0.7593444104074563],
[3, 98.109167673, 8.678944881814035e6, 0.19225733584927554, 0.771013833583392],
[4, 133.209045499, 8.555157452063877e6, 0.1902110143380687, 0.7733156170819961],
[5, 168.333785424, 8.497913484825356e6, 0.18961963309594962, 0.7746509810292195],
[6, 203.23730795900002, 8.46813011977514e6, 0.1895342040601351, 0.7741454261176766],
[7, 238.036531399, 8.451379396148669e6, 0.1894978588132885, 0.7742003506734846],
[8, 273.17018557200004, 8.441400728598438e6, 0.18957152264441737, 0.7739665744035481],
[9, 311.11963864100005, 8.435181195726883e6, 0.189646379982292, 0.7736297318912704],
[10, 350.69279695100005, 8.431160226117328e6, 0.1898138973019813, 0.7732561525643622],
[11, 390.507238205, 8.42848082041119e6, 0.1898879613325366, 0.7729346257398895],
[12, 430.03880645500004, 8.42664915956546e6, 0.18997102729373366, 0.7733267652106369],
[13, 469.950838743, 8.425369013965398e6, 0.18997179094758038, 0.772933462686752],
[14, 510.189442659, 8.424456650132822e6, 0.18999969882688136, 0.7728629156106979],
[15, 549.83391833, 8.423794857829763e6, 0.18999923112141176, 0.7730986681185409],
[16, 589.3160509669999, 8.423306964074679e6, 0.19002293620383193, 0.7730151569861125],
[17, 628.4929126039999, 8.422941942792622e6, 0.19001352438150548, 0.7733340888359409],
[18, 663.834953363, 8.42266507295294e6, 0.19003980818194105, 0.7731431408212972],
[19, 697.573322141, 8.422452395781705e6, 0.19009378918811412, 0.7730902791783293],
[20, 731.3630792719999, 8.422287073614769e6, 0.1901055485360227, 0.7729291176121458]
]

w_4c = [
[0, 0.0, 3.0357818523864355e7, 0.35211772440099826, 0.4753160623163859],
[1, 12.601484223, 1.0682719616912805e7, 0.25859065898671707, 0.691681502978013],
[2, 28.597288391, 9.00926234294171e6, 0.19950706174332203, 0.7593444104074563],
[3, 44.799248663, 8.678944881814029e6, 0.19225733584927554, 0.771013833583392],
[4, 60.457237418, 8.55517107911031e6, 0.19019939186237664, 0.7733511676788676],
[5, 76.35995602999999, 8.497917013917519e6, 0.18961846342135288, 0.7746118074903598],
[6, 92.380830365, 8.468132412272967e6, 0.18953198008219177, 0.7742241380152223],
[7, 108.34500672499999, 8.451380878183793e6, 0.189484120714732, 0.7742359414407393],
[8, 124.61136077999998, 8.441401699022723e6, 0.18957009311680664, 0.7740178918192757],
[9, 140.774002917, 8.435181823770877e6, 0.18964758044603455, 0.7736166042146873],
[10, 157.36293247199998, 8.431160646502681e6, 0.18982186735074538, 0.7732473483269164],
[11, 173.49688738199998, 8.4284811175014e6, 0.18988823246535452, 0.7729750817174712],
[12, 189.37429310399997, 8.426649382354293e6, 0.18996978544989016, 0.7733249038237217],
[13, 205.60694542699997, 8.425369189303132e6, 0.1899744574294259, 0.7729254935316153],
[14, 221.23471479399998, 8.42445679334534e6, 0.19000080511490922, 0.7728319883541362],
[15, 236.93100385499997, 8.423794978907656e6, 0.18999758282754237, 0.773078282446352],
[16, 252.58312764, 8.423307068837345e6, 0.19002195943884775, 0.7729885809598767],
[17, 268.863212563, 8.42294203415528e6, 0.1900147211726567, 0.773332773611565],
[18, 284.677891053, 8.422665153099254e6, 0.19004262160450797, 0.7731454577784544],
[19, 300.775960875, 8.422452466331143e6, 0.19009686939555212, 0.773091982711572],
[20, 316.66352429200003, 8.422287135725224e6, 0.19010355348716465, 0.772918082236544]
]

w_8c = [
[0, 0.0, 3.0357818523864355e7, 0.35211772440099826, 0.4753160623163859],
[1, 8.087369504, 1.0682719616912816e7, 0.25859065898671707, 0.691681502978013],
[2, 18.4248191, 9.009294584763687e6, 0.1994819077140947, 0.7593558674902534],
[3, 28.731039787, 8.678948934817716e6, 0.19225378935104673, 0.771000348384406],
[4, 39.768654118, 8.555159075243488e6, 0.1902071717473999, 0.7732818762713789],
[5, 49.928204884, 8.49791486607158e6, 0.1896138240870143, 0.7747110588130718],
[6, 60.220079594000005, 8.468130482265871e6, 0.18953861572743969, 0.774130232684052],
[7, 70.41086047900001, 8.451393944286149e6, 0.18947874435155673, 0.7742711597797242],
[8, 81.126148083, 8.441402327827074e6, 0.1895564944662706, 0.773987844695165],
[9, 91.391727487, 8.435189370582115e6, 0.18963925083300184, 0.7736626700169235],
[10, 101.66992959699999, 8.431160864981085e6, 0.18980841141933566, 0.7732807644940869],
[11, 111.927875382, 8.428511961906873e6, 0.18986539175103115, 0.7728863799470875],
[12, 122.099570313, 8.426655596675167e6, 0.1899577788749339, 0.7734874895463669],
[13, 133.332674372, 8.42537626856887e6, 0.18997918622485443, 0.7729025879574921],
[14, 143.70135772900002, 8.424465237483643e6, 0.19000602774097464, 0.7729444301545666],
[15, 153.84684251200002, 8.423794987830536e6, 0.18998266476133732, 0.7731459625727882],
[16, 165.01896710600002, 8.42367715080398e6, 0.18998639992181113, 0.7731599333460033],
[17, 175.95354546800002, 8.423140056324465e6, 0.18999080679379485, 0.7733094687223436],
[18, 186.08039684000002, 8.42280466201651e6, 0.19002745434456222, 0.7733915649950646],
[19, 198.33685962100003, 8.422783354260867e6, 0.19004102312217555, 0.7732304084914594],
[20, 209.91290877500003, 8.422602479869133e6, 0.1900474968226522, 0.7731765283572789]
]

# data
c_1t = np.array(c_1t)
c_4t = np.array(c_4t)
c_8t = np.array(c_8t)
w_1c = np.array(w_1c)
w_4c = np.array(w_4c)
w_8c = np.array(w_8c)
# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,4], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,4], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,4], 'c', label='primal 8 cores')
ax.plot(c_1t[:,1], c_1t[:,4], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,4], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,4], 'm', label='collrank 8 threads')
ax.set_title('MovieLens1m, 200 ratings/user, rank 300, lambda = 5000')
ax.set_xlabel('Time')
ax.set_ylabel('NDCG')
ax.axis([0, 300, 0.4, 0.85])
# Now add the legend with some customizations.
legend = ax.legend(loc='lower right', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()


fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,3], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,3], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,3], 'c', label='primal 8 cores')
ax.plot(c_1t[:,1], c_1t[:,3], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,3], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,3], 'm', label='collrank 8 threads')
ax.set_title('MovieLens1m, 200 ratings/user, rank 300, lambda = 5000')
ax.set_xlabel('Time')
ax.set_ylabel('Pairwise_Error')
ax.axis([0, 300, 0.15, 0.4])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()


fig, ax = plt.subplots()
ax.plot(w_1c[:,1], w_1c[:,2], 'r--', label='primal 1 core')
ax.plot(w_4c[:,1], w_4c[:,2], 'k-.', label='primal 4 cores')
ax.plot(w_8c[:,1], w_8c[:,2], 'c', label='primal 8 cores')
ax.plot(c_1t[:,1], c_1t[:,2], 'm:', label='collrank 1 thread')
ax.plot(c_4t[:,1], c_4t[:,2], 'm-.', label='collrank 4 threads')
ax.plot(c_8t[:,1], c_8t[:,2], 'm', label='collrank 8 threads')
ax.set_title('MovieLens1m, 200 ratings/user, rank 300, lambda = 5000')
ax.set_xlabel('Time')
ax.set_ylabel('Objective_Function')
ax.axis([0, 300, 8e6, 3.3e7])
legend = ax.legend(loc='upper right', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()










