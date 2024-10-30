'''
AI Cards 

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



#6-1. Input
risk_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT ?system ?risk ?consequence ?impact ?control { 
        ?system a airo:AISystem ;
                    airo:hasRisk ?risk .
        ?risk a airo:Risk ;
                 airo:hasConsequence ?consequence .
        ?consequence a airo:Consequence ;                     
                     airo:hasImpact ?impact .  
        ?impact a airo:Impact ;
                airo:hasImpactOnArea vair:RightToNondiscrimination .

        ?control  a airo:RiskControl, vair:TestingMeasure .
        ?riskRelation rdfs:subPropertyOf* airo:modifiesRiskConcept .

        {
        ?control  ?riskRelation  ?risk .
        }
        UNION {
        ?control ?riskRelation  ?consequence .
        }
        UNION {
        ?control ?riskRelation  ?impact .
        }
               


        }

   
"""
#USE filter to retrive the ones that only have impact on ... 

for row in g.query(risk_query):
    #print(row)
    print("_______:" + getLocal(str(row.system)) + ", risk: "+ getLocal(str(row.risk)) + ", cons: " + getLocal(str(row.consequence)) +", impact: "+ getLocal(str(row.impact))+", control: "+ getLocal(str(row.control)))




    
     