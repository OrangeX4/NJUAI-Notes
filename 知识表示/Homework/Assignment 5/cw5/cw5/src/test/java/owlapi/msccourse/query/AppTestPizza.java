package owlapi.msccourse.query;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

import org.apache.commons.io.IOUtils;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLClass;
import org.semanticweb.owlapi.model.OWLClassExpression;
import org.semanticweb.owlapi.model.OWLDataFactory;
import org.semanticweb.owlapi.model.OWLNamedIndividual;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import owlapi.msccourse.query.CW5;
import owlapi.msccourse.query.QueryResult;
import owlapi.msccourse.query.QueryType;

/**
 * Unit test for simple App.
 */
public class AppTestPizza extends TestCase {
	/**
	 * Create the test case
	 *
	 * @param testName
	 *            name of the test case
	 */

	OWLDataFactory df = OWLManager.getOWLDataFactory();
	OWLClass domaine = df.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#DomainConcept"));
	OWLClass hot = df.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#Hot"));
	
	OWLClass nap = df.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#Napoletana"));
	OWLClass ven = df.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#Veneziana"));
	OWLClass real = df.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#RealItalianPizza"));
	OWLClass ve1 = df
			.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#VegetarianPizzaEquivalent1"));
	OWLClass ve2 = df
			.getOWLClass(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#VegetarianPizzaEquivalent2"));
	OWLNamedIndividual america = df
			.getOWLNamedIndividual(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#America"));
	OWLNamedIndividual germany = df
			.getOWLNamedIndividual(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#Germany"));
	OWLNamedIndividual france = df
			.getOWLNamedIndividual(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#France"));
	OWLNamedIndividual italy = df
			.getOWLNamedIndividual(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#Italy"));
	OWLNamedIndividual england = df
			.getOWLNamedIndividual(IRI.create("http://www.co-ode.org/ontologies/pizza/pizza.owl#England"));


	
	CW5 queryApp;

	public AppTestPizza(String testName) {
		super(testName);
		queryApp = Utils.prepareCW5("pizza.owl");
	}

	/**
	 * @return the suite of tests being tested
	 */
	public static Test suite() {
		return new TestSuite(AppTestPizza.class);
	}

	public void testEquivalentClassesWithPizza() {
		OWLClassExpression exp = queryApp.parseClassExpression("Pizza and (hasTopping only VegetarianTopping)");
		Set<QueryResult> results = queryApp.performQuery(exp, QueryType.EQUIVALENTCLASSES);
		assertTrue(results.contains(new QueryResult(ve1, true, QueryType.EQUIVALENTCLASSES)));
		assertTrue(results.contains(new QueryResult(ve2, true, QueryType.EQUIVALENTCLASSES)));
	}

	public void testSubClassesWithPizza() {
		OWLClassExpression exp = queryApp.parseClassExpression("ThinAndCrispyPizza");
		Set<QueryResult> results = queryApp.performQuery(exp, QueryType.SUBCLASSES);
		assertTrue(results.contains(new QueryResult(nap, false, QueryType.SUBCLASSES)));
		assertTrue(results.contains(new QueryResult(ven, false, QueryType.SUBCLASSES)));
		assertTrue(results.contains(new QueryResult(real, true, QueryType.SUBCLASSES)));
		assertTrue(results.size() == 3);
	}

	private void printResults(Set<QueryResult> results) {
		for (QueryResult s : results) {
			System.out.println(s);
		}
	}

	public void testInstancesWithPizza() {
		OWLClassExpression exp = queryApp.parseClassExpression("Country");
		Set<QueryResult> results = queryApp.performQuery(exp, QueryType.INSTANCES);
		printResults(results);
		assertTrue(results.contains(new QueryResult(america, true, QueryType.INSTANCES)));
		assertTrue(results.contains(new QueryResult(germany, true, QueryType.INSTANCES)));
		assertTrue(results.contains(new QueryResult(france, true, QueryType.INSTANCES)));
		assertTrue(results.contains(new QueryResult(italy, true, QueryType.INSTANCES)));
		assertTrue(results.contains(new QueryResult(england, true, QueryType.INSTANCES)));
		assertTrue(results.size() == 5);
	}

	public void testValidPizza() {
		assertTrue(queryApp.isValidPizza(ve1));
		assertFalse(queryApp.isValidPizza(domaine));
		assertTrue(queryApp.isValidPizza(nap));
		assertTrue(queryApp.isValidPizza(ven));
		assertFalse(queryApp.isValidPizza(hot));
		assertFalse(queryApp.isValidPizza(queryApp.parseClassExpression("hasTopping only Thing")));
	}
	
	public void testFilterNamedPizza() {
		Set<QueryResult> res = new HashSet<QueryResult>();
		res.add(new QueryResult(england, true, QueryType.INSTANCES));
		res.add(new QueryResult(nap, false, QueryType.SUBCLASSES));
		res.add(new QueryResult(ve1, true, QueryType.EQUIVALENTCLASSES));
		res.add(new QueryResult(ve2, false, QueryType.EQUIVALENTCLASSES));
		res.add(new QueryResult(ven, true, QueryType.EQUIVALENTCLASSES));
		Set<QueryResult> results = queryApp.filterNamedPizzas(res);
		assertFalse(results.contains(new QueryResult(england, true, QueryType.INSTANCES)));
		assertTrue(results.contains(new QueryResult(nap, false, QueryType.SUBCLASSES)));
		assertFalse(results.contains(new QueryResult(ve1, true, QueryType.EQUIVALENTCLASSES)));
		assertFalse(results.contains(new QueryResult(ve2, false, QueryType.EQUIVALENTCLASSES)));
		assertTrue(results.contains(new QueryResult(ven, true, QueryType.EQUIVALENTCLASSES)));
		
	}
	
	public void testGetSuperClassesPizza() {
		Set<OWLClassExpression> superc = queryApp.getAllSuperclassExpressions(nap);
		assertTrue(superc.contains(domaine));
		assertTrue(superc.contains(queryApp.parseClassExpression("Pizza and (hasBase only ThinAndCrispyBase)")));
		assertTrue(superc.contains(queryApp.parseClassExpression("Pizza and (hasCountryOfOrigin value Italy)")));
		assertTrue(superc.contains(queryApp.parseClassExpression("Pizza and (not (VegetarianPizza))")));
		assertTrue(superc.contains(queryApp.parseClassExpression("Pizza and (hasTopping min 3 Thing)")));
		assertTrue(superc.contains(queryApp.parseClassExpression("Pizza and (hasTopping some CheeseTopping)")));
		assertTrue(superc.contains(queryApp.parseClassExpression("ThinAndCrispyPizza")));
		assertTrue(superc.contains(queryApp.parseClassExpression("NonVegetarianPizza")));
		assertFalse(superc.contains(df.getOWLNothing()));
		//assertTrue(false);
	}
	
		

}
