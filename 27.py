def dist(pointA,pointB):
    xa,ya,xb,yb = *pointA,*pointB
    return ((xa - xb)**2 + (ya - yb)**2)**0.5

def clustInit(basePoint):
    clust = [point for point in aData
             if dist(basePoint, point) < alpha]
    if clust:
        for point in clust:
            aData.remove(point)
        nextClust = [clustInit(point)
                     for point in clust]
        for n in nextClust: clust.extend(n)
    return clust

def clustCenter(cluster):
    massPoint = []
    for point in cluster:
        sumR = sum(dist(point, currentPoint)
                   for currentPoint in cluster)
        massPoint.append((sumR, point))
    return min(massPoint)[1]
    




aData = []
for s in open('ano27a.txt'):
    aData.append(tuple(map(float, s.split())))
    
print (len(aData))

clusters = []
alpha = 0.85

while aData:
    point = aData.pop()
    cluster = [point] + clustInit(point)
    clusters.append(cluster)
    print (len(cluster))

clusters = [clust for clust in clusters if len(clust) > 6]
    
centers = [clustCenter(clust)
           for clust in clusters]

px = sum(x for x,y in centers) / len(centers)
py = sum(y for x,y in centers) / len(centers)

print (int(px*10000), int(py*10000))

