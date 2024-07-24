'''
AI Cards 

9	Compliance & Certification
9-1-	Which regulations does the system comply with?
9-2-	Which standards does the system conform to?
9-3-	Which codes of conducts does the system follow?

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



#9-1. regulation
reg_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX dpv: <https://w3id.org/dpv#>  

SELECT  ?regulation ?jurisdiction   { 
        ?system a airo:AISystem ;
                    airo:compliesWithRegulation ?regulation .
        ?regulation dpv:hasJurisdiction ?jurisdiction .                    
                   
        }
   
"""
for row in g.query(reg_query):
    print("Jurisdiction: "+getLocal(str(row.jurisdiction)) + " Regulation: " + getLocal(str(row.regulation)))  


#9-2. standard 
standard_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?standard   { 
        ?system a airo:AISystem ;
                    airo:conformsToStandard ?standard .
                   
        }
       
   
"""
standard_list = list ()

for row in g.query(standard_query):
    if getLocal(str(row.standard)) not in standard_list:
        standard_list.append(getLocal(str(row.standard)))

print(f"9-. Standard: {', '.join(standard_list)}")  

#9-3. codes of conduct 
standard_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?code   { 
        ?system a airo:AISystem ;
                    airo:followsCodeOfConduct ?code .
                   
        } 
         
"""

code_list = list ()

for row in g.query(standard_query):
    if getLocal(str(row.code)) not in code_list:
        code_list.append(getLocal(str(row.code)))

print(f"9-3. Codes of Conduct: {', '.join(code_list)}") 


    
     