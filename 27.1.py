def dist(point1, point2):
    x1,y1,x2,y2 = *point1, *point2
    return ((x1-x2)**2 +(y1-y2)**2)**0.5

def clustInit(basePoint):
    clust = [point for point in aData if dist(basePoint, point) < alpha]
    if clust:
        for point in clust:
            aData.remove(point)
        nextClust = [clustInit(point) for point in clust]
        for i in nextClust:
            clust.extend(i)
    return clust

def clustCenter(cluster):
    massPoint = []
    for point in cluster:
        sumP = sum(dist(point, currentPoint) for currentPoint in cluster)
        massPoint.append((sumP,point))
    return min(massPoint)[1]



aData = []
for i in open('7657b.txt'):
    aData.append(tuple(map(float, i.replace(',','.').split())))
print(len(aData))

clusters = []
alpha = 1

while aData:
    point = aData.pop()
    cluster = [point] + clustInit(point)
    clusters.append(cluster)
    print(len(cluster))

clusters = [clust for clust in clusters if len(clust) > 30]

centers = [clustCenter(clust) for clust in clusters]

px = sum(x for x,y in centers) / len(centers)

py = sum(y for x,y in centers) / len(centers)

print(int(px*100000), int(py*100000))