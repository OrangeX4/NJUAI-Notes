package owlapi.msccourse.query;

import java.io.File;
import java.util.Scanner;
import java.util.Set;

import org.semanticweb.owlapi.io.OWLParserException;
import org.semanticweb.owlapi.model.OWLClassExpression;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;

/**
 * Hello world!
 *
 */
public class App {
	static boolean running = true;

	public static void main(String[] args) throws OWLOntologyCreationException {
		System.out.println("Welcome to Reasoner Query Tool!");
		CW5 queryApp = Utils.prepareCW5("fhkb.owl");
		Scanner scanIn = new Scanner(System.in);

		while (running) {
			boolean performquery = true;
			System.out.println("");
			System.out.println("################");
			System.out.println("Enter a valid query in Protege syntax!");
			String sQueryType;
			QueryType type = QueryType.SUBCLASSES;

			System.out.println("Select the query type");
			System.out.println("[1]: Subclasses");
			System.out.println("[2]: Equivalent classes");
			System.out.println("[3]: Instances");
			System.out.println("[0]: Quit");
			sQueryType = scanIn.nextLine();

			switch (sQueryType) {
			case "1":
				type = QueryType.SUBCLASSES;
				break;
			case "2":
				type = QueryType.EQUIVALENTCLASSES;
				break;
			case "3":
				type = QueryType.INSTANCES;
				break;
			case "0":
				System.out.println("Quitting...");
				running = false;
				performquery = false;
				break;
			default:
				System.out.println("Illegal entry: " + sQueryType + ". Has to be one of 0,1,2,3.");
				performquery = false;
			}
			if (performquery) {
				String sClassExpression;
				System.out.println("Enter a valid query in protege syntax");
				sClassExpression = scanIn.nextLine();
				System.out.println(sClassExpression);
				try {
					OWLClassExpression exp = queryApp.parseClassExpression(sClassExpression);
					Set<QueryResult> results = queryApp.performQuery(exp, type);
					for (QueryResult r : results) {
						System.out.println(r);
					}
				} catch (OWLParserException e) {
					System.out.println("Illegal syntax: "+sClassExpression);
				}
			}
		}
		scanIn.close();
	}
}
