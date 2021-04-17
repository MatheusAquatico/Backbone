import math

class VetorHeap:
    def __init__(self):
        self.vetor=[]
        self.tamanho=int(len(self.vetor))
        self.tamanhoHeap=0
    def addNo(self,peso,indice):
        self.vetor.append([peso,indice])
        self.tamanhoHeap+=1
        
class grafo:

    def __init__(self,vertices):
        self.vertices=vertices
        self.grafo=[[0] * self.vertices for i in range(self.vertices)] 
    def addAresta(self,verticeInicio,verticeFim,peso):
        self.grafo[verticeInicio][verticeFim]=peso
        self.grafo[verticeFim][verticeInicio]=peso
        

    def dijikstra(self,origem,vetorHeap,vetorVisitado,vetorListaAdjacencia,gGrafo,vetorCusto,vetorCaminho,vetorPai):
        visitado=vetorVisitado
        listaAdjacencia=vetorListaAdjacencia
        custo=vetorCusto
        grafo=gGrafo
        caminho=vetorCaminho
        pos=0
        pai=vetorPai
        while vetorHeap.tamanhoHeap >0:
            buildMinHeap(vetorHeap)
            caminhoMin, v= extractMinHeap(vetorHeap)
            visitado[v]=1
            for l in listaAdjacencia[v]:
                if visitado[l]==0:
                    if int(int(caminho[v][0]) + int(custo[v][l])) < int(caminho[l][0]):
                        for z in range(len(vetorHeap.vetor)):
                            if int(vetorHeap.vetor[z][1])==l:
                                pos=z
                                break
                        caminho[l]= [caminho[v][0] + custo[v][l],v]
                        vetorHeap.vetor[pos]=[caminho[l][0],l]
                        pai[l]=self.vertices
        return caminho

def minHeapfy(vetorHeap, indice):
        e=9999999999
        d=9999999999
        if (indice*2)-1 < len(vetorHeap.vetor):
                e=(indice*2)-1
                if indice*2 < len(vetorHeap.vetor):
                    d=indice*2
                else:
                    d=9999999999
        tam=vetorHeap.tamanhoHeap
        menor=9999999999
        if e <= tam and int(vetorHeap.vetor[e][0]) < int(vetorHeap.vetor[indice-1][0]):
            menor=e
        else:
            menor = indice-1
        if d <= tam and int(vetorHeap.vetor[d][0]) < int(vetorHeap.vetor[menor][0]):
            menor = d
        if vetorHeap.vetor[menor] != vetorHeap.vetor[indice-1]:
            aux=vetorHeap.vetor[indice-1]
            vetorHeap.vetor[indice-1]=vetorHeap.vetor[menor]
            vetorHeap.vetor[menor]=aux
            minHeapfy(vetorHeap, menor)
    
def buildMinHeap(vetorHeap):
    t=math.floor((int(len(vetorHeap.vetor))/2))
    for i in range(t,0,-1):
        minHeapfy(vetorHeap, i)

def heapsort(vetorHeap):
    buildMinHeap(vetorHeap)
    tam=len(vetorHeap.vetor)-1
    for i in range(tam,2,-1):
        aux=vetorHeap.vetor[0]
        vetorHeap.vetor[0]=vetorHeap.vetor[i]
        vetorHeap.vetor[i]=aux
        minHeapfy(vetorHeap,1)

def extractMinHeap(vetorHeap):
    if vetorHeap.tamanhoHeap<1:
        print("Acabou o heap")
    min=vetorHeap.vetor[0]
    vetorHeap.vetor[0]=vetorHeap.vetor[(vetorHeap.tamanhoHeap)-1]
    vetorHeap.tamanhoHeap-=1
    minHeapfy(vetorHeap,1)
    return min

def main():
    
    lines=[]
    try:   
        while True:
            lines.append(input())
    except:
        pass
    
    linha=lines[0].split(' ')
    vertices=int(linha[0])
    arestas=int(linha[1])
    listaAdjacencia= [[] * vertices for n in range(vertices)]
    custo=[]

    for i in range (vertices):
        line=[]
        for j in range(vertices):
            if i==j:
                line.append(0)
            else:
                line.append(-1)
        custo.append(line)

    partida=lines[arestas+1]
    string=lines[1].split(' ')
    if string[0]!=partida:
        for i in range(2,len(lines)):
            s=lines[i].split(' ')
            if s[0]==partida:
                sub=lines[1]
                lines[1]=lines[i]
                lines[i]=sub
                break

       
    infinito=9999999999
    g=grafo(vertices)
    paises={}
    cont=0
    for k in range(1,arestas+1):
        l=lines[k].split(' ')
        paisInicio=l[0]
        paisFim=l[1]
        if (paisInicio in paises)==False:
            paises.update({paisInicio:cont})
            cont+=1
        if (paisFim in paises)==False:
            paises.update({paisFim:cont})
            cont+=1
        
        verticeInicio=int(paises.get(paisInicio))
        verticeFim=int(paises.get(paisFim))
        c=int(l[2])
        listaAdjacencia[verticeInicio].append(verticeFim)
        listaAdjacencia[verticeFim].append(verticeInicio)
        custo[verticeInicio][verticeFim]=c
        custo[verticeFim][verticeInicio]=c
        g.addAresta(verticeInicio,verticeFim,c)

    visitado= [0] * vertices
    caminho= [[infinito,infinito]] * vertices
    caminho[0]=[0,0]
    vetorHeap= VetorHeap()
    
    for a in range(0,vertices):
        vetorHeap.addNo(caminho[a][0],a)
    pai= vertices * [-1]
    key=lines[arestas+1].strip()
    partida=paises.get(key)
    chegada=lines[arestas+2]
    modoUnico=bool(int(lines[arestas+3]))
    out=g.dijikstra((partida-1),vetorHeap,visitado,listaAdjacencia,g,custo,caminho,pai)
    for i in range(0,len(out)):
        distancia=int(out[i][0])
        valor=int(out[i][1])
        for p,v in paises.items():
            if v==valor:
                break
        paisVizinho=p 
        for p,v in paises.items(): 
            if v==i:
                break
        paisChegada=p
        if modoUnico!=False:
            if chegada!=paisChegada:
                continue
            else:
                print(paisChegada,end=': ')
                print(distancia,end=' <- ')
                print(paisVizinho)
        else:
            print(paisChegada,end=': ')
            print(distancia,end=' <- ')
            print(paisVizinho)
if __name__ == '__main__':
    main()
