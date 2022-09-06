import rdflib
from rdflib import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, XML
from rdflib.plugins.stores.memory import Memory
 

sparql = SPARQLWrapper("http://dbkwik.webdatacommons.org/sparql") 
construct_query="""
    PREFIX ma: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>     
    PREFIX dbkwik: <http://dbkwik.webdatacommons.org>   
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      
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
        ?film rdf:type dbkwik:Film .
        ?film foaf:name ?name .

        OPTIONAL {?film dbkwik:director ?direct}
        OPTIONAL {?film dbkwik:producer ?prod}
        OPTIONAL {?film dbkwik:starring ?actor}
        OPTIONAL {?film dbkwik:editing ?edit} 
        OPTIONAL {?film dbkwik:cinematography ?cg}
        OPTIONAL {?film dbkwik:distributor ?distributor}
        OPTIONAL {?film dbkwik:studio ?studio}    
        OPTIONAL {?film dbkwik:country ?country}
        OPTIONAL {?film dbkwik:language ?lang}
        OPTIONAL {?film dbkwik:budget ?budget}
        OPTIONAL {?film dbkwik:gross ?gross} 
        OPTIONAL {?film dbkwik:abstract ?abstract} 
        OPTIONAL {?film dbkwik:releaseDate ?date}
        OPTIONAL {?film dbkwik:runtime ?duration}
        OPTIONAL {?film dbkwik:creator ?create}
        OPTIONAL {?film dbkwik:developer ?create}
        OPTIONAL {?film dbkwik:composer ?compose}
        OPTIONAL {?film dbkwik:genre ?gn}

      
    
    } LIMIT 5


"""

construct_query1= """ 

    PREFIX ma: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>     
    PREFIX dbkwik: <http://dbkwik.webdatacommons.org>   
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

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
        ?tv rdf:type dbkwik:Episode .
        ?tv foaf:name ?name .

        OPTIONAL {?tv dbkwik:director ?direct}
        OPTIONAL {?tv dbkwik:producer ?prod}
        OPTIONAL {?tv dbkwik:starring ?actor}
        OPTIONAL {?tv dbkwik:editing ?edit} 
        OPTIONAL {?tv dbkwik:cinematography ?cg}
        OPTIONAL {?tv dbkwik:channel ?distributor}
        OPTIONAL {?tv dbkwik:distributor ?distributor}
        OPTIONAL {?tv dbkwik:company ?studio}    
        OPTIONAL {?tv dbkwik:country ?country}
        OPTIONAL {?tv dbkwik:language ?lang}
        OPTIONAL {?tv dbkwik:budget ?budget}
        OPTIONAL {?tv dbkwik:gross ?gross} 
        OPTIONAL {?tv dbkwik:abstract ?abstract} 
        OPTIONAL {?tv dbkwik:releaseDate ?date}
        OPTIONAL {?tv dbkwik:runtime ?duration}
        OPTIONAL {?tv dbkwik:executiveProducer ?exp}
        OPTIONAL {?tv dbkwik:numberOfEpisodes ?ne}
        OPTIONAL {?tv dbkwik:numberOfSeasons ?ns}
        OPTIONAL {?tv dbkwik:numEpisodes ?ne}
        OPTIONAL {?tv dbkwik:numSeasons ?ns}
        OPTIONAL {?tv dbkwik:genre ?gn}
        OPTIONAL {?tv dbkwik:creator ?create}
        OPTIONAL {?tv dbkwik:developer ?create}
        OPTIONAL {?tv dbkwik:composer ?compose}
        OPTIONAL {?tv dbkwik:audioFormat ?a_for}
        OPTIONAL {?tv dbkwik:pictureFormat ?p_for}
        OPTIONAL {?tv dbkwik:camera ?cam}
       

       
    } LIMIT 5

 """

sparql.setQuery(construct_query)
sparql.setReturnFormat(XML)

memory_store = Memory()
graph_id = URIRef('http://www.semanticweb.org/store/movie')
g = Graph(store = memory_store, identifier = graph_id)

print("  Working, please wait")

g = sparql.query().convert()
g.parse(" final report basic.owl")

g.serialize(" final report bonus.owl", "xml")

sparql.setQuery(construct_query1)
sparql.setReturnFormat(XML)

memory_store = Memory()
graph_id = URIRef('http://www.semanticweb.org/store/movie')
g = Graph(store = memory_store, identifier = graph_id)

print("  Working, please wait")

g = sparql.query().convert()
g.parse(" final report basic.owl")

g.serialize(" final report bonus.owl", "xml")

print("  Done file generated!!!!")

