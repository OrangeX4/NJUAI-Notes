package owlapi.fhkb.fspopulation;

import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.util.Collection;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.model.parameters.Imports;

import junit.framework.TestCase;
import owlapi.fhkb.fspopulation.CSVParser;
import owlapi.fhkb.fspopulation.CW3;
import owlapi.fhkb.fspopulation.JobDataBean;

public class CW3Test extends TestCase {

	public void testLoad() {
		CW3 main = new CW3();
		// Load data from CSV
		// Collection<JobDataBean> beans = new CSVParser().parse(new
		// InputStreamReader(URI.create(args[0]).toURL().openStream()));
		ClassLoader classloader = Thread.currentThread()
				.getContextClassLoader();
		OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
		// Your code should now load the ontology using the supplied manager

		OWLOntology ontology = main.loadOntology(manager,
				classloader.getResourceAsStream("ontology.owl"));
		assertTrue(ontology!=null);
		assertTrue(ontology.tboxAxioms(Imports.INCLUDED).count()==160);
		assertTrue(ontology.aboxAxioms(Imports.INCLUDED).count()==0);
	}

	public void testSave() {

		CW3 main = new CW3();
		// Load data from CSV
		// Collection<JobDataBean> beans = new CSVParser().parse(new
		// InputStreamReader(URI.create(args[0]).toURL().openStream()));
		ClassLoader classloader = Thread.currentThread()
				.getContextClassLoader();
		try {
			OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
			// Your code should now load the ontology using the supplied manager

			OWLOntology ontology = main.loadOntology(manager,
					classloader.getResourceAsStream("ontology.owl"));

			File out = new File("fhkb-ai.owl");
			Files.deleteIfExists(out.toPath());
			main.saveOntology(manager, ontology, IRI.create(out.toURI()));
			OWLOntology fhkb = OWLManager.createOWLOntologyManager()
					.loadOntologyFromOntologyDocument(out);
			assertTrue(fhkb.tboxAxioms(Imports.INCLUDED).count()==160);

		} catch (IOException e) {
			// TODO Auto-generated catch block
			assertTrue(false);
			e.printStackTrace();
		} catch (OWLOntologyCreationException e) {
			// TODO Auto-generated catch block
			assertTrue(false);
			e.printStackTrace();
		}
		

	}

	public void testPopulate() {
		try {
			CW3 main = new CW3();
			// Load data from CSV
			// Collection<JobDataBean> beans = new CSVParser().parse(new
			// InputStreamReader(URI.create(args[0]).toURL().openStream()));
			ClassLoader classloader = Thread.currentThread()
					.getContextClassLoader();
			Collection<JobDataBean> beans = new CSVParser()
					.parse(new InputStreamReader(classloader
							.getResourceAsStream("test.csv")));

			OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
			// Your code should now load the ontology using the supplied manager

			OWLOntology ontology = main.loadOntology(manager,
					classloader.getResourceAsStream("ontology.owl"));
			
			main.populateOntology(manager, ontology, beans);
			assertTrue(ontology!=null);
			assertTrue(ontology.aboxAxioms(Imports.INCLUDED).count()>=40);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
