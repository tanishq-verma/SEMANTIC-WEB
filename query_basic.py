import rdflib


query = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX fo: <http://purl.org/ontology/fo/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cw: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#>



SELECT ?name  ?budget ?box_office ?p ?a
WHERE { 
  		?show rdf:type cw:TV_series .
  		?show cw:names ?name .
  		?show cw:Budget ?budget . 
  		?show cw:Box_office ?box_office .
		?show cw:summary ?sum . 
  		?show cw:produced_by ?p .
		?show cw:starring_in ?a 
  		}
"""

query1 = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX fo: <http://purl.org/ontology/fo/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cw: <http://www.semanticweb.org/tanishq/ontologies/2022/3/cw#>

SELECT ?n  ?bud ?box ?p ?a
WHERE { 
  		?mov rdf:type cw:Movies .
  		?mov cw:names ?n .
  		?mov cw:Budget ?bud . 
  		?mov cw:Box_office ?box .
		?mov cw:summary ?sum . 
		?mov cw:produced_by ?p .
  		?mov cw:starring_in ?a 
  		}
	  
	  """	  


g = rdflib.Graph()
g.parse(" final report basic.owl", "xml")

print("graph has %s statements.\n" % len(g))

print(" THIS QUERY IS FOR TV_series") 
print(" ----------------------------------------------------------------------------------------------------------") 


print ('{0:25s} {1:25s} {2:25s} {3:50s} {4:50s} '.format("name", "budget", "box_office","director", "actor"))
for x,y,z,a,b in g.query(query):
    print ('{0:25s} {1:25s} {2:25s} {3:50s} {4:50s}'.format(x,y,z,a,b))


print(" THIS QUERY IS FOR Movies")
print(" ----------------------------------------------------------------------------------------------------------") 


print ('{0:25s} {1:25s} {2:25s} {3:50s} {4:50s}'.format("name", "budget", "box_office","director","actor"))
for x,y,z,a,b in g.query(query1):
    print ('{0:25s} {1:25s} {2:25s} {3:50s} {4:50s}'.format(x,y,z,a,b))


