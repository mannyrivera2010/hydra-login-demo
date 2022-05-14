

stra = """
	<http://mobi.com/data/uhtc/material/SiCaA{sa}> a <http://matonto.org/ontologies/uhtc#Material> ;
		<http://www.w3.org/2000/01/rdf-schema#label> "SiCaA{sa}" ;
		<http://www.w3.org/2000/01/rdf-schema#comment> "Silicon carbide, also known as carborundum, is a compound of silicon and carbon with chemical formula SiC. It occurs in nature as the extremely rare mineral moissanite." ;
		<http://matonto.org/ontologies/uhtc#chemicalFormula> "SiCaA{sa}" ;
		<http://matonto.org/ontologies/uhtc#crystalStructure> <http://mobi.com/data/uhtc/crystalstructure/Polymorphic> ;
		<http://matonto.org/ontologies/uhtc#density> 3.21E0 ;
		<http://matonto.org/ontologies/uhtc#element> <http://mobi.com/data/uhtc/element/Carbon> , <http://mobi.com/data/uhtc/element/Silicon> ;
		<http://matonto.org/ontologies/uhtc#meltingPoint> 2.82E3 .
"""

for i in range(10000,20000):
    print(stra.replace("{sa}", str(i)))