##

## This program creates the tree for the iterations of the Artichoke Deep Dreaming from Google

##importing the libraries needed for this project##
import random
import treelib
from treelib import Node, Tree
import time
import pickle
import os.path
import json



##creating a list with all the letters of the alphabet so we can call a
##letter using a number using the variable alphabet[n] where n is a
##number.
alphabet=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

treerecreate=[]



### Creating a data file if none exists ###
if os.path.isfile("aatr_treerecreate.dat")==False:
		open("aatr_treerecreate.dat",mode='x').close()
		drawrandom=True
else:

		openfile=open("aatr_treerecreate.dat")
		print(pickle.load(open("aatr_treerecreate.dat","rb")))
		treerecreate=pickle.load(open("aatr_treerecreate.dat","rb"))
		drawrandom=False
###
###
#generating 11 images in tree and generating the list variable
tree = Tree()
tree.create_node(0,"base")
listvariable = []
i=1
while i<12:
	tree.create_node(alphabet[i],i-1,parent="base")
	i+=1
	listvariable.append(str(i))
						
        
#print("Here is the base for the tree")
#print(tree)

print()
print()
drawmaxnumber=len(listvariable)

continuemating=True
matecount=0
recreationcount=0

while continuemating==True:
            
    if drawrandom==True:
            ##generating random number for the parents of the new artichoke
            draw1=random.randint(0,drawmaxnumber-1)
            draw2=random.randint(0,drawmaxnumber-1)
            matecount=matecount+1
            treerecreate.append(draw1)
            treerecreate.append(draw2)
    else:
            draw1=treerecreate[recreationcount]
            recreationcount=recreationcount+1
            draw2=treerecreate[recreationcount]
            recreationcount=recreationcount+1
            if recreationcount>len(treerecreate)-1:
                    drawrandom=True
                    
    ##checking if the draw has two different parents
    if draw1!= draw2:
        ##checking how many children does the parent already have.
        ##With this information, we will be able to give a name to the
        ##new kid following the naming scheeme (aa, ab, ac, ad, etc.)
        childrenofdraw1=tree.children(draw1)
        numberofchildren=len(childrenofdraw1)

        ##Setting the name of the new child
        newchildrenname=str(tree[draw1].tag+str(alphabet[numberofchildren+1]))
        print("New artichoke called ", newchildrenname)
        #time.sleep(1)
        print("that kid was made from ", tree[draw1].tag, " with ",tree[draw2].tag)
        #time.sleep(1)
        print()
        #time.sleep(1)
        print()
        #time.sleep(1)
        
        ###################### WRONG IDEA ################################
        ###newchildrenname=str(newchildrenname)+" ("+tree[draw2].tag+")"##
        ##################################################################

        ##adding the child to the tree
        tree.create_node(newchildrenname,drawmaxnumber,parent=draw1)

        ##adding child to the list variable
        listvariable.append(str(drawmaxnumber))
        drawmaxnumber=drawmaxnumber+1

        
    if matecount==1:
            continuemating=False


print(tree)



### Saving all the different variables
#print(treerecreate)
openfile=open("aatr_treerecreate.dat", "wb")
pickle.dump(treerecreate, openfile)
openfile.close()
