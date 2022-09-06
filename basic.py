import rdflib
from rdflib.graph import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, XML
from rdflib.plugins.stores.memory import Memory
 

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
construct_query="""
    PREFIX ma: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    PREFIX dbpprop: <http://dbpedia.org/property/>
      
     CONSTRUCT {
        ?film rdf:type ma:Movies .
        ?film ma:names ?name .
        ?film ma:directed_by ?direct .
        ?direct rdf:type ma:director .
        ?film ma:produced_by ?prod .
        ?prod rdf:type ma:producer .
        ?film ma:starring_in ?actor .
        ?actor rdf:type ma:cast_member .
        ?film ma:edited_by ?edit .
        ?edit rdf:type ma:editor .
        ?film ma:cinematography_by ?cg .
        ?cg rdf:type ma:cinematographer .
        ?film ma:sponsoring ?distributor .
        ?distributor rdf:type ma:company .
        ?film ma:sponsoring ?studio .    
        ?studio rdf:type ma:channel .
        ?film ma:shot_in_country ?country .
        ?country rdf:type ma:Country .
        ?film ma:has_language ?lang .
        ?lang rdf:type ma:Language .
        ?film ma:Budget ?budget .
        ?film ma:Box_office ?gross .
        ?film ma:summary ?abstract .
        ?film ma:Release_date ?date .
        ?film ma:run_time ?duration .  
        ?film ma:created_by ?create . 
        ?create rdf:type ma:creator .
        ?film ma:composed_by ?compose . 
        ?compose rdf:type ma:composer . 
        ?film ma:has_genre ?gn .
        ?gn rdf:type ma:genre .
        
    }
    WHERE {
        ?film rdf:type dbpedia-owl:Film .
        ?film foaf:name ?name .

        OPTIONAL {?film dbpedia-owl:director ?direct}
        OPTIONAL {?film dbpedia-owl:producer ?prod}
        OPTIONAL {?film dbpedia-owl:starring ?actor}
        OPTIONAL {?film dbpedia-owl:editing ?edit} 
        OPTIONAL {?film dbpedia-owl:cinematography ?cg}
        OPTIONAL {?film dbpedia-owl:distributor ?distributor}
        OPTIONAL {?film dbpedia-owl:studio ?studio}    
        OPTIONAL {?film dbpedia-owl:country ?country}
        OPTIONAL {?film dbpedia-owl:language ?lang}
        OPTIONAL {?film dbpprop:budget ?budget}
        OPTIONAL {?film dbpprop:gross ?gross} 
        OPTIONAL {?film dbpedia-owl:abstract ?abstract} 
        OPTIONAL {?film dbpedia-owl:releaseDate ?date}
        OPTIONAL {?film dbpprop:runtime ?duration}
        OPTIONAL {?film dbpedia-owl:creator ?create}
        OPTIONAL {?film dbpedia-owl:developer ?create}
        OPTIONAL {?film dbpedia-owl:composer ?compose}
        OPTIONAL {?film dbpedia-owl:genre ?gn}

        FILTER (LANG(?abstract)="en")
      
    
    } 


    """


construct_query1= """ 

    PREFIX ma: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    PREFIX dbpprop: <http://dbpedia.org/property/>

        CONSTRUCT {
        ?tv rdf:type ma:TV_series .
        ?tv ma:names ?name .
        ?tv ma:directed_by ?direct .
        ?direct rdf:type ma:director .
        ?tv ma:produced_by ?prod .
        ?prod rdf:type ma:producer .
        ?tv ma:produced_by ?exp .
        ?exp rdf:type ma:executiveProducer .
        ?tv ma:starring_in ?actor .
        ?actor rdf:type ma:cast_member .
        ?tv ma:edited_by ?edit .
        ?edit rdf:type ma:editor .
        ?tv ma:cinematography_by ?cg .
        ?cg rdf:type ma:cinematographer .
        ?tv ma:sponsoring ?studio .
        ?studio rdf:type ma:company .
        ?tv ma:sponsoring ?distributor .    
        ?distributor rdf:type ma:channel .
        ?tv ma:shot_in_country ?country .
        ?country rdf:type ma:Country .
        ?tv ma:has_language ?lang .
        ?lang rdf:type ma:Language .
        ?tv ma:Budget ?budget .
        ?tv ma:Box_office ?gross .
        ?tv ma:summary ?abstract .
        ?tv ma:Release_date ?date .
        ?tv ma:run_time ?duration .   
        ?tv ma:has_episodes ?ne .
        ?tv ma:has_seasons ?ns . 
        ?tv ma:has_genre ?gn .
        ?gn rdf:type ma:genre . 
        ?tv ma:created_by ?create . 
        ?create rdf:type ma:creator .
        ?tv ma:composed_by ?compose . 
        ?compose rdf:type ma:composer . 
        ?tv ma:has_format ?a_for . 
        ?a_for rdf:type ma:audioFormat.
        ?tv ma:has_format ?p_for . 
        ?p_for rdf:type ma:pictureFormat.
        ?tv ma:has_format ?cam . 
        ?cam rdf:type ma:camera.
        
        
        
       
    }
    WHERE {
        ?tv rdf:type dbpedia-owl:TelevisionShow .
        ?tv foaf:name ?name .

        OPTIONAL {?tv dbpedia-owl:director ?direct}
        OPTIONAL {?tv dbpedia-owl:producer ?prod}
        OPTIONAL {?tv dbpedia-owl:starring ?actor}
        OPTIONAL {?tv dbpedia-owl:editing ?edit} 
        OPTIONAL {?tv dbpedia-owl:cinematography ?cg}
        OPTIONAL {?tv dbpedia-owl:channel ?distributor}
        OPTIONAL {?tv dbpedia-owl:distributor ?distributor}
        OPTIONAL {?tv dbpedia-owl:company ?studio}    
        OPTIONAL {?tv dbpedia-owl:country ?country}
        OPTIONAL {?tv dbpedia-owl:language ?lang}
        OPTIONAL {?tv dbpprop:budget ?budget}
        OPTIONAL {?tv dbpprop:gross ?gross} 
        OPTIONAL {?tv dbpedia-owl:abstract ?abstract} 
        OPTIONAL {?tv dbpedia-owl:releaseDate ?date}
        OPTIONAL {?tv dbpprop:runtime ?duration}
        OPTIONAL {?tv dbpedia-owl:executiveProducer ?exp}
        OPTIONAL {?tv dbpedia-owl:numberOfEpisodes ?ne}
        OPTIONAL {?tv dbpedia-owl:numberOfSeasons ?ns}
        OPTIONAL {?tv dbpprop:numEpisodes ?ne}
        OPTIONAL {?tv dbpprop:numSeasons ?ns}
        OPTIONAL {?tv dbpedia-owl:genre ?gn}
        OPTIONAL {?tv dbpedia-owl:creator ?create}
        OPTIONAL {?tv dbpedia-owl:developer ?create}
        OPTIONAL {?tv dbpedia-owl:composer ?compose}
        OPTIONAL {?tv dbpedia-owl:audioFormat ?a_for}
        OPTIONAL {?tv dbpedia-owl:pictureFormat ?p_for}
        OPTIONAL {?tv dbpedia-owl:camera ?cam}
       

        FILTER (LANG(?abstract)="en")
       
    } 

 """

sparql.setQuery(construct_query)
sparql.setReturnFormat(XML)



memory_store = Memory()
graph_id = URIRef("http://www.semanticweb.org/store/movie")
g = Graph(store = memory_store, identifier = graph_id)


print("  It may take some time....")


g = sparql.query().convert()

print("  Working ....")


g.parse("final report.owl")

print(" final report generated, creating final basic report ....")


g.serialize(" final report basic.owl", "xml")

print("  Working ....")


sparql.setQuery(construct_query1)
sparql.setReturnFormat(XML)

print("  Dealing with multiple queries....")


memory_store = Memory()
graph_id = URIRef("http://www.semanticweb.org/store/movie")
g = Graph(store = memory_store, identifier = graph_id)

g = sparql.query().convert()

print("  Finilizing and finishing....")



g.parse(" final report basic.owl")

g.serialize(" final report basic.owl", "xml")


print("  ...All done!")
print("")
