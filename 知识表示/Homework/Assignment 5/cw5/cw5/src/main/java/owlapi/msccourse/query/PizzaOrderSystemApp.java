package owlapi.msccourse.query;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

import org.semanticweb.owlapi.io.OWLParserException;
import org.semanticweb.owlapi.model.OWLClass;
import org.semanticweb.owlapi.model.OWLClassExpression;
import org.semanticweb.owlapi.model.OWLEntity;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;

/**
 * Hello world!
 *
 */
public class PizzaOrderSystemApp {
	static boolean running = true;

	public static void main(String[] args) throws OWLOntologyCreationException {
		System.out.println("Welcome to the Pizza Ordering Tool!");
		CW5 queryApp = Utils.prepareCW5("pizza.owl");

		Scanner scanIn = new Scanner(System.in);

		while (running) {
			boolean performquery = true;
			System.out.println("");
			System.out.println("################");
			System.out.println("What do you want to do next?");
			String sQueryType;
			QueryType type = QueryType.SUBCLASSES;

			System.out.println("[1]: Order (another) a Pizza");
			System.out.println("[0]: Quit");
			sQueryType = scanIn.nextLine();

			switch (sQueryType) {
			case "1":
				break;
			case "0":
				System.out.println("Quitting...");
				running = false;
				performquery = false;
				break;
			default:
				System.out.println("Illegal entry: " + sQueryType + ". Has to be one of 0,1.");
				performquery = false;
			}
			if (performquery) {
				String sClassExpression;
				System.out.println("Enter your Pizza Order");
				sClassExpression = scanIn.nextLine();
				try {
					OWLClassExpression exp = queryApp.parseClassExpression(sClassExpression);
					if (queryApp.isValidPizza(exp)) {
						Set<QueryResult> res = queryApp.performQuery(exp, type);
						Set<QueryResult> results = queryApp.filterNamedPizzas(res);
						Map<Integer, QueryResult> mres = new HashMap<Integer, QueryResult>();
						int i = 1;
						for (QueryResult q : results) {
							mres.put(i, q);
							i++;
						}
						if (mres.isEmpty()) {
							System.out
									.println("Unfortunately, we have no offers matching your description. Try again!");

						} else {
							System.out.println("We have the following offers. Select an option: ");
							for (Integer in : mres.keySet()) {
								System.out.println("[" + in + "] " + mres.get(in));
							}

							String s_order = scanIn.nextLine();
							try {
								Integer order = Integer.valueOf(s_order);
								if (mres.containsKey(order)) {
									OWLEntity e = mres.get(order).getEntity();
									System.out.println(
											"Your order has been received. While you are waiting,"+"\n"+"here some facts about the Pizza you have ordered!");
									System.out.println("");
									System.out.println(
											"##########FactSheet for: " + Utils.render(e) + " ####################");

									Set<OWLClassExpression> superclassesOfOrder = queryApp
											.getAllSuperclassExpressions((OWLClass) (mres.get(order).getEntity()));
									for (OWLClassExpression ce : superclassesOfOrder) {
										System.out.println(Utils.render(ce));
										System.out.println("----------------------------------");
									}
									System.out.println("");
									System.out.println(
											"##################################################################");
								}
							} catch (NumberFormatException e) {
								System.out.println("Illegal number entered");
							}
						}
					} else {
						System.out.println("Your description does not correspond to a real Pizza! Try again!");
					}

				} catch (OWLParserException e) {
					System.out.println("Illegal syntax: " + sClassExpression);
				}
			}
		}
		scanIn.close();
	}
}
