import re 
import numpy as np
import fnmatch
import os




class FileParser:

        def __init__(self,chemin):
        
                self.path=self.PathFinding(chemin)
                test=self.ReadNbOfEnnemies(self.path[0])
                print(test)
                
                
                
                
                
        def PathFinding(self,chemin):
        
                m_cheminObjectTypePattern='*[Oo][bB][jJ][eE][cC][tT][tT][Yy][pP][eE]*.csv'
                m_cheminObjectTypeIsFound=False
                m_cheminObjectTypePath=''
                
                m_cheminObjectChoicePattern='*[Oo][Bb][Jj][eE][cC][tT][cC][hH][oO][iI][cC][eE]*.csv'
                m_cheminObjectChoiceIsFound=False
                m_cheminObjectChoicePath=''
                
                m_cheminNbOfEnnemiesPattern='*[nN][bB][oO][fF][eE][nN][nN][eE][mM][iI][eE][sS]*.csv'
                m_cheminNbOfEnnemiesIsFound=False
                m_cheminNbOfEnnemiesPath=''
                
                
                
                with os.scandir(chemin) as entries:
                        
                        for entry in entries:
                                

                                if fnmatch.fnmatch(entry,m_cheminNbOfEnnemiesPattern):
                                        m_cheminNbOfEnnemiesPath=entry.path
                                        m_cheminNbOfEnnemiesIsFound=True
                                        
                                elif fnmatch.fnmatch(entry,m_cheminObjectChoicePattern):
                                        m_cheminObjectChoicePath=entry.path
                                        m_cheminObjectChoiceIsFound=True
                                        
                                elif fnmatch.fnmatch(entry,m_cheminObjectTypePattern):
                                        m_cheminObjectTypePath=entry.path  
                                        m_cheminObjectTypeIsFound =True
                                                
                                                
                allIsThere=[m_cheminNbOfEnnemiesIsFound,m_cheminObjectChoiceIsFound,m_cheminObjectTypeIsFound]
                paths=[m_cheminNbOfEnnemiesPath,m_cheminObjectChoicePath,m_cheminObjectTypePath]
                
                if all(allIsThere):
                        print("Tous les fichiers sont là")
                        return paths
                        
                        
                        
                else:
                        print("un des fichiers n'est pas trouvé")
                        return None
                        
                            
        def ReadNbOfEnnemies(self,path):
                flux=open(path,'r')
                lignes=flux.readlines()
                i=0
                blocs=[]
                sousBlocs=[]
                
                NomsEnnemis=[]
                ObjetsEnnemis=[]
                
                while i<len(lignes):
                        if lignes[i]=='\n':
                                blocs.append(sousBlocs)
                                sousBlocs=[]
                        else:
                                sousBlocs.append(lignes[i][0:-1])

                        i+=1
                        
                
                for bloc in blocs:
                        if bloc[0][0:6]=='Ennemi':
                                name,rank=bloc[0].split('(')
                                
                                
                                rank=rank[5:-2]
                                boundsLower,boundsUpper=rank.split(" à ")
                                boundsLower=int(boundsLower)
                                boundsUpper=int(boundsUpper)
                                
                                ranks=np.arange(boundsLower,boundsUpper+1,1)
                                                         
                                
                                loot=[]
                                for i in range(2,len(bloc)):
                                        loot.append(int(bloc[i].split('\t')[1]))

                                
                                NomsEnnemis.append(name)
                                ObjetsEnnemis.append(Ennemy(name,loot,ranks))
                                

                        elif bloc[0][0:6]=='nombre':
                        	
                        	print(bloc)

                                #noms=[]
                                #valeur=[]
                                #for i in range (1,len(bloc)):
                                #        noms.append(bloc[i].split('\t')[0])
                                #        valeur.append(bloc[i].split('\t')[1])
                                #        
                                #print(noms)
                                #print(valeur)

                                     
                DicoEnnemi=dict(zip(NomsEnnemis,ObjetsEnnemis))
                
                print([DicoEnnemi['Ennemis Mineur '].ObtainNbOfLoot(9),DicoEnnemi['Ennemis Mineur '].ObtainRanks()])
                print([DicoEnnemi['Ennemis Majeur '].ObtainNbOfLoot(7),DicoEnnemi['Ennemis Majeur '].ObtainRanks()])
                        
                return DicoEnnemi
                

                
        def ReadObjectType(path):
                return None
                
        def ReadObjectChoice(path):
                return None
                
                
class Ennemy:
        def __init__(self,name,lootTable,ranks):
        
                self.name=name
                self.ranks=ranks
                self.lootTable=lootTable
                
        def __str__(self):
                return self.name
        def ObtainNbOfLoot(self,numberOfEnnemies):
        
                return self.lootTable[numberOfEnnemies-1]
        def ObtainRanks(self):
                return self.ranks
                
                
class Chest:
        def __init__(self,name,DicoEnnemy,):
                
                self.name=name
                self.listeOfEnnemies
                
        def __str__(self):
                return self.name
                
        def ObtainNbOfLoot(self,numberofChest):
                pass
                
                
                
                
        
        
                        
a=FileParser("../Données")                               
                                                
                                        
                                        
                
        
        
