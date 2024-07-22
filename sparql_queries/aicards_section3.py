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

#3-1. Output 

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
  







    
     