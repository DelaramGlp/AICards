'''
AI Cards 
7-1	For each of the system's quality 
7-1-1-	What is the quality?
7-1-2-	What is the measurement?
    

'''
import rdflib
import pandas as pd
import plotly.express as px

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



#7-1. Quality
quality_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo: <https://w3id.org/airo#>
PREFIX vair: <https://w3id.org/vair#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX dqv: <http://www.w3.org/ns/dqv#>

SELECT  ?metric ?value
WHERE   { ?system  dqv:hasQualityMeasurement  ?qualityMeasurment .
           ?qualityMeasurment dqv:isMeasurementOf ?metric ;
                                dqv:value ?value .

                   
        }
   
"""

result = []
for row in g.query(quality_query):
    result.append((getLocal(str(row.metric)), getLocal(str(row.value))))

df = pd.DataFrame(result, columns=['metric', 'value'])




fig = px.line_polar(df,  r='value', theta='metric', line_close=True)
fig.show()
#fig = px.line_polar(df, metric='metric', value='value', line_close=True)
#fig.show()

for row in g.query(quality_query):
    print("Quality: "+getLocal(str(row.metric)) + " , Value: "+ getLocal(str(row.value)))  




    
     