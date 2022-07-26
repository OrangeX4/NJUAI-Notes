package owlapi.msccourse.query;

import java.io.File;
import java.util.HashSet;
import java.util.Set;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.expression.OWLEntityChecker;
import org.semanticweb.owlapi.expression.ShortFormEntityChecker;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLClass;
import org.semanticweb.owlapi.model.OWLClassExpression;
import org.semanticweb.owlapi.model.OWLDataFactory;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.reasoner.InferenceType;
import org.semanticweb.owlapi.reasoner.OWLReasoner;
import org.semanticweb.owlapi.util.BidirectionalShortFormProviderAdapter;
import org.semanticweb.owlapi.util.SimpleShortFormProvider;
import org.semanticweb.owlapi.util.mansyntax.ManchesterOWLSyntaxParser;

import com.clarkparsia.pellet.owlapiv3.PelletReasonerFactory;


/**
 * Nanjing University<br>
 * School of Artificial Intelligence<br>
 * KRistal Group<br>
 * 
 * Acknowledgement: with great thanks to Nico at Cambridge for the insightful discussions and his useful suggestions in making this project. 
 *
 */

public class CW5 {

	final OWLOntologyManager man;
	final OWLDataFactory df = OWLManager.getOWLDataFactory();
	final OWLOntology o;
	OWLReasoner r;

	CW5(File file) throws OWLOntologyCreationException {
		// DO NOT CHANGE
		this.man = OWLManager.createOWLOntologyManager();
		this.o = man.loadOntologyFromOntologyDocument(file);
		this.r = new PelletReasonerFactory().createReasoner(o);
		this.r.precomputeInferences(InferenceType.CLASS_HIERARCHY);
	}

	public Set<QueryResult> performQuery(OWLClassExpression exp, QueryType type) {
		/*
		 * Change this method to perform the task
		 */
		System.out.println("Performing Query");
		Set<QueryResult> results = new HashSet<QueryResult>();
		switch (type) {
		case EQUIVALENTCLASSES:
			/// Use the reasoner to query for equivalent classes and add the appropriate query results
			break;
		case INSTANCES:
			/// Use the reasoner to query for direct and indirect instances (separately) and add the appropriate query results
			break;
		case SUBCLASSES:
			/// Use the reasoner to query for direct and indirect sub-classes (separately) and add the appropriate query results
			break;
		default:
			break;
		}

		return results;
	}
	
	public boolean isValidPizza(OWLClassExpression exp) {
		OWLClass pizza = df.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#Pizza"));
		boolean b = false;
		/// IMPLEMENT: Use the reasoner to check whether exp is a valid Pizza expression! Return TRUE if it is.
		return b;
	}

	public Set<QueryResult> filterNamedPizzas(Set<QueryResult> results) {
		OWLClass np = df.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#NamedPizza"));
		Set<QueryResult> results_filtered = new HashSet<QueryResult>();
		// Add to results filtered only those QueryResults that correspond to NamedPizzas
		return results_filtered;
	}

	public Set<OWLClassExpression> getAllSuperclassExpressions(OWLClass ce) {
		Set<OWLClassExpression> restrictions = new HashSet<OWLClassExpression>();
		// try to think of a way to infer as many restrictions on ce as possible. Tip: You will need to use both the ontology and the reasoner for this task!
		return restrictions;
	}

	public OWLClassExpression parseClassExpression(String sClassExpression) {
		OWLEntityChecker entityChecker = new ShortFormEntityChecker(
				new BidirectionalShortFormProviderAdapter(man, o.getImportsClosure(), new SimpleShortFormProvider()));
		ManchesterOWLSyntaxParser parser = OWLManager.createManchesterParser();
		parser.setOWLEntityChecker(entityChecker);
		parser.setStringToParse(sClassExpression);
		// j
		OWLClassExpression exp = parser.parseClassExpression();
		return exp;
	}

}
