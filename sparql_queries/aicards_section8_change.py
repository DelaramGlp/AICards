'''
AI Cards 
8	Pre-determined change
8-1	For each pre-determined change 
    8-1-1-	Does the change impact performance?
    8-1-2-	Which entity is changed?
    8-1-3-	What is the frequency of change?
    

'''
import rdflib
 

def getLocal(uri):
    pos = -1
    pos = uri.rfind('#')
    if pos < 0 :
        pos = uri.rfind('/')
    #if pos < 0 :
     #   pos =  uri.rindex(':')
    return uri[pos+1:]





g = rdflib.Graph()
g.parse("https://raw.githubusercontent.com/DelaramGlp/airo/main/usecase/proctify.ttl" , format="turtle")

airo = "https://w3id.org/airo"
g.parse(airo, format="ttl") 



#8-1. Change
change_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX dpv: <https://w3id.org/dpv#>  

SELECT  ?change ?changedSubject ?frequency ?purpose 
WHERE   { ?system airo:hasPreDeterminedChange ?change .
            ?change airo:hasFrequency ?frequency ;
                airo:hasChangedEntity ?changedSubject ;
                airo:hasPurpose ?purpose .                     
                   
        }
   
"""
for row in g.query(change_query):
    print("Changed entity: "+getLocal(str(row.changedSubject)) + " , Purpose of change: "+getLocal(str(row.purpose)) + " , Frequency: " + getLocal(str(row.frequency)))  




    
     