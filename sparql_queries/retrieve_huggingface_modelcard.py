'''
AI Cards 

'''
import rdflib
import json
from huggingface_hub import ModelCard

g = rdflib.Graph()
g.parse("/Users/delaram/Desktop/Phd/Projects/aicards/sparql_queries/proctify.ttl" , format="turtle")

airo = "https://w3id.org/airo"
g.parse(airo, format="ttl") 

component_info_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX airo: <https://w3id.org/airo#>

SELECT ?model ?doc
    WHERE { 
    ?system a airo:AISystem ;
            airo:hasModel ?model .   
    ?model airo:hasDocumentation ?doc . }

"""
for row in g.query(component_info_query):
    card = ModelCard.load(str(row.doc))
    card_json_string = json.dumps(card.data.to_dict(), indent=-2)
    card_json = json.loads(card_json_string)
    license = card_json["license"]
    print("HuggingFaceModel:", row.doc, "license:", license)











    
     