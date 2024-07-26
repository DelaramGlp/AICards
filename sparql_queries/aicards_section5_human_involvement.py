'''
AI Cards 
5	Human Involvement
5-1-	What is the level of automation?
5-2-	For each AI subject/ AI end-user
5-2-1-	Are they intended?
5-2-2-	Are they active?
5-2-3-	Are they informed?
5-2-4-	Type of their control over output
    

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


#5-1. Level of automation
automation_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?system  ?automationLevel
WHERE   { 
        ?system  airo:hasAutomationLevel  ?automationLevel .
         
        }
   
"""



#5-2. AI end-users
user_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?system ?endUser ?involvement ?control
WHERE   {     ?system  airo:hasAIUser ?endUser .
              ?endUser  airo:hasHumanInvolvement ?involvement ;
                airo:hasControlOverAIOutput ?control .  
        }
   
"""

#5-2. AI subject
subject_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?system ?subject ?involvement ?control
WHERE   {    ?system  airo:hasAISubject ?subject .  
             ?subject  airo:hasHumanInvolvement ?involvement ;
                      airo:hasControlOverAIOutput ?control .  

              
              
        }
   
"""


for row in g.query(automation_query):
    print("Level of automation: "+getLocal(str(row.automationLevel)))  

for row in g.query(user_query):
    print("End-user: "+ getLocal(str(row.endUser))+" , Involvement: " + getLocal(str(row.involvement)) + " , control: " + getLocal(str(row.control)))   

for row in g.query(subject_query):
    print("Subject: "+ getLocal(str(row.subject))+" , Involvement: " + getLocal(str(row.involvement)) + " , control: " + getLocal(str(row.control)))



    
     