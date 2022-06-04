package owlapi.msccourse.query;

import junit.framework.Test;
import junit.framework.TestSuite;

public class AllTests {

	public static Test suite() {
		TestSuite suite = new TestSuite(AllTests.class.getName());
		//$JUnit-BEGIN$
		suite.addTest(AppTestFHKB.suite());
		suite.addTest(AppTestPizza.suite());
		//$JUnit-END$
		return suite;
	}

}
