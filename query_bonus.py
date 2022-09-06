import rdflib

if True:
    g = rdflib.Graph()
    g.parse(" final report bonus.owl", "xml")
    print("graph has %s statements.\n" % len(g))


    
    query="""
    PREFIX ma: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    SELECT DISTINCT ?name ?budget ?release
    WHERE { ?film rdf:type ma:TV_series .
  			?film ma:names ?name .
            ?film ma:Budget ?budget . 
            ?film ma:Release_date ?release .
  			 FILTER regex(?name, "r", "i"). 
            } ORDER BY DESC(?budget)
            """

    print ('{0:45s} {1:30s} {2:30s}'.format("Title","Budget","Release_Date"))
    for x,y,z in g.query(query):
        print ('{0:45s} {1:30s} {2:30s}'.format(x,y,z))


    query1="""
    PREFIX ma: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    SELECT DISTINCT ?name ?budget ?release
    WHERE { ?film rdf:type ma:Movies .
  			?film ma:names ?name .
            ?film ma:Budget ?budget . 
            ?film ma:Release_date ?release .
  			 FILTER regex(?name, "r", "i"). 
            } ORDER BY DESC(?budget)
            """

    print ('{0:45s} {1:30s} {2:30s}'.format("Title","Budget","Release_Date"))
    for x,y,z in g.query(query1):
        print ('{0:45s} {1:30s} {2:13s}'.format(x,y,z))