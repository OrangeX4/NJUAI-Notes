package owlapi.msccourse.query;

import java.util.Set;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLClass;
import org.semanticweb.owlapi.model.OWLClassExpression;
import org.semanticweb.owlapi.model.OWLDataFactory;
import org.semanticweb.owlapi.model.OWLNamedIndividual;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTestFHKB extends TestCase {
	/**
	 * Create the test case
	 *
	 * @param testName
	 *            name of the test case
	 */
	OWLDataFactory df = OWLManager.getOWLDataFactory();
	CW5 queryApp;

	public AppTestFHKB(String testName) {
		super(testName);
		queryApp = Utils.prepareCW5("fhkb.owl");
	}

	/**
	 * @return the suite of tests being tested
	 */
	public static Test suite() {
		return new TestSuite(AppTestFHKB.class);
	}

	public void testEquivalentClassesWithFHKB() {
		OWLDataFactory df = OWLManager.getOWLDataFactory();
		OWLClass ve1 = df
				.getOWLClass(IRI.create("http://owl.cs.manchester.ac.uk/tutorials/fhkbtutorial/fhkb_chapter_6.owl#ParentOfRichard"));
		OWLClass ve2 = df
				.getOWLClass(IRI.create("http://owl.cs.manchester.ac.uk/tutorials/fhkbtutorial/fhkb_chapter_6.owl#ParentOfRobert"));
		OWLClass ve3 = df
				.getOWLClass(IRI.create("http://owl.cs.manchester.ac.uk/tutorials/fhkbtutorial/fhkb_chapter_6.owl#ParentOfRichardAndRobert"));

		OWLClassExpression exp = queryApp.parseClassExpression("Person and (isParentOf some {Richard_John_Bright_1962,Robert_David_Bright_1965})");
		Set<QueryResult> results = queryApp.performQuery(exp, QueryType.EQUIVALENTCLASSES);
		assertTrue(results.contains(new QueryResult(ve1, true, QueryType.EQUIVALENTCLASSES)));
		assertTrue(results.contains(new QueryResult(ve2, true, QueryType.EQUIVALENTCLASSES)));
		assertTrue(results.contains(new QueryResult(ve3, true, QueryType.EQUIVALENTCLASSES)));
	}

	public void testSubClassesFHKB() {
		OWLClass c1 = df.getOWLClass(IRI.create("http://owl.cs.manchester.ac.uk/tutorials/fhkbtutorial/fhkb_chapter_4.owl#FemaleAncestor"));
		OWLClassExpression exp = queryApp.parseClassExpression("FemaleDescendant");
		Set<QueryResult> results = queryApp.performQuery(exp, QueryType.SUBCLASSES);
		printResults(results);
		assertTrue(results.contains(new QueryResult(c1, true, QueryType.SUBCLASSES)));
		assertTrue(results.size() == 1);
	}

	private void printResults(Set<QueryResult> results) {
		for (QueryResult s : results) {
			System.out.println(s);
		}
	}

	public void testInstancesWithFHKB() {
		OWLNamedIndividual margarete = df
				.getOWLNamedIndividual(IRI.create("http://owl.cs.manchester.ac.uk/tutorials/fhkbtutorial/fhkb_chapter_2.owl#Margaret_Grace_Rever_1934"));
		OWLNamedIndividual david = df
				.getOWLNamedIndividual(IRI.create("http://owl.cs.manchester.ac.uk/tutorials/fhkbtutorial/fhkb_chapter_2.owl#David_Bright_1934"));

		OWLClassExpression exp = queryApp.parseClassExpression("Person and isParentOf value Robert_David_Bright_1965");
		Set<QueryResult> results = queryApp.performQuery(exp, QueryType.INSTANCES);
		printResults(results);
		assertTrue(results.contains(new QueryResult(margarete, false, QueryType.INSTANCES)));
		assertTrue(results.contains(new QueryResult(david, false, QueryType.INSTANCES)));
		assertTrue(results.size() == 2);
	}
}
