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


#3-1. Input
input_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?input 
    WHERE { ?system a airo:AISystem ;
                    airo:hasInput ?input .}
"""
input_list = list ()

for row in g.query(input_query):
    if getLocal(str(row.input)) not in input_list:
        input_list.append(getLocal(str(row.input)))

print(f"3-1. Input: {', '.join(input_list)}")  

#3-2. Output 

output_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?output 
    WHERE { ?system a airo:AISystem ;
                    airo:producesOutput ?output .}
"""
output_list = list ()

for row in g.query(output_query):
    if getLocal(str(row.output)) not in output_list:
        output_list.append(getLocal(str(row.output)))

print(f"3-2. Output: {', '.join(output_list)}") 
  

#3-3. Incorporating Component 

component_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT  ?component 
    WHERE { ?system a airo:AISystem .
    {
    ?system airo:hasComponent ?component .
  } UNION {
    ?system ?componentProperty ?component .
    ?componentProperty rdfs:subPropertyOf* airo:hasComponent .
  }}
     
"""
component_list = list ()

for row in g.query(component_query):
    if getLocal(str(row.component)) not in component_list:
        component_list.append(getLocal(str(row.component)))

print(f"3-3. List of incorporating Components: {', '.join(component_list)}") 

#3-4. Component Information
component_info_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

SELECT ?component ?version ?type ?doc
    WHERE { 
    ?system a airo:AISystem .
    ?system ?componentProperty ?component .
    ?componentProperty rdfs:subPropertyOf* airo:hasComponent .
      
  
    ?component rdf:type ?type ;
            airo:hasVersion ?version ;
            airo:hasDocumentation ?doc .       

             }

"""

for row in g.query(component_info_query):
    print("3-4. Component Information:" + getLocal(str(row.component)) + ", version: "+ getLocal(str(row.version)) + ", type: " + getLocal(str(row.type)) +", documentation: "+ str(row.doc))







    
     