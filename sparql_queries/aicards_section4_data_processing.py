'''
AI Cards 
4	Data Processing
4-1-	For each data processing
4-1-1-	What is the legal basis?
4-1-2-	What data is processed?
4-1-3-	What is the source of data?

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



#4-1. data processing
data_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX dpv: <https://w3id.org/dpv#>  

SELECT ?processing ?legalBasis ?data ?source
WHERE   { ?system dpv:hasProcessing ?processing .
           ?processing dpv:hasLegalBasis ?legalBasis ;
                        dpv:hasData ?data .
            ?data  dpv:hasDataSource ?source                         
                   
        }
   
"""
for row in g.query(data_query):
    print("Processing: "+getLocal(str(row.processing)) + " , Legal basis: "+ getLocal(str(row.legalBasis)) + " , Data: " + getLocal(str(row.data)) + " ,Data Source:" + getLocal(str(row.source)) )  




    
     