'''
AI Cards 
2	Intended Purpose
2-1	What is the domain in which the AI system intended to used in?
2-2	What is the intended purpose of the AI system?
2-3	What is the capability of the AI system?
2-4	Who is the deployer of the AI system?
2-5	Who is the AI subject?
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

SELECT  ?system ?domain ?purpose ?capability ?deployer ?subject
    WHERE { ?system a airo:AISystem;
                    airo:isAppliedWithinDomain ?domain;
                    airo:hasPurpose ?purpose;
                    airo:hasCapability ?capability;
                    airo:isDeployedBy ?deployer ;
                    airo:hasAISubject ?subject .}
"""

 
for row in g.query(highrisk_query):
     print("System: "+getLocal(str(row.system )))
     print("Domain: "+ getLocal(str(row.domain)))
     print("Purpose: "+getLocal(str(row.purpose)))
     print("AI capability: "+getLocal(str(row.capability)))
     print("User: "+getLocal(str(row.deployer)))
     print("AI subject: "+getLocal(str(row.subject)))




    
     