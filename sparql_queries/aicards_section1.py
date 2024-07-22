'''
AI Cards 
1. General Inforamtion 
1a.	What is the version of the AI system?
1b.	What is the modality of the AI system?
1c.	What techniques used in the AI system?
1d.	Who is the AI provider?
1e.	Who is the AI developer?
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

highrisk_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?system ?version ?modality ?technique ?provider ?developer ?purpose
    WHERE { ?system a airo:AISystem;
                    airo:hasPurpose ?purpose ;
                    airo:hasVersion ?version ;
                    airo:hasModality ?modality ;
                    airo:usesTechnique ?technique ;
                    airo:isProvidedBy ?provider ;
                    airo:isDevelopedBy ?developer .   }
"""

 
modality_list = list ()
technique_list = list ()
provider_list = list ()
developer_list = list ()
  
for row in g.query(highrisk_query):
    if getLocal(str(row.modality)) not in modality_list:
        modality_list.append(getLocal(str(row.modality)))

for row in g.query(highrisk_query):
    if getLocal(str(row.technique)) not in technique_list:
        technique_list.append(getLocal(str(row.technique)))

for row in g.query(highrisk_query):
    if getLocal(str(row.provider)) not in provider_list:
        provider_list.append(getLocal(str(row.provider)))

 
for row in g.query(highrisk_query):
    if getLocal(str(row.developer)) not in developer_list:
        developer_list.append(getLocal(str(row.developer)))

print("System: "+getLocal(str(row.system )))     
print("1a. Version: "+ getLocal(str(row.version)))
print(f"1b. Modality: {', '.join(modality_list)}")  
print(f"1c. Technique: {', '.join(technique_list)}")
print(f"1d. Provider: {', '.join(provider_list)}")
print(f"1e. Developer: {', '.join(developer_list)}")  





    
     