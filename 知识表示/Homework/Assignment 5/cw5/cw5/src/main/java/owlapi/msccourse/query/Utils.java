package owlapi.msccourse.query;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

import org.semanticweb.owlapi.dlsyntax.renderer.DLSyntaxObjectRenderer;
import org.semanticweb.owlapi.io.OWLObjectRenderer;
import org.semanticweb.owlapi.manchestersyntax.renderer.ManchesterOWLSyntaxOWLObjectRendererImpl;
import org.semanticweb.owlapi.manchestersyntax.renderer.ManchesterOWLSyntaxObjectRenderer;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLClass;
import org.semanticweb.owlapi.model.OWLClassExpression;
import org.semanticweb.owlapi.model.OWLObject;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;

public class Utils {
	
	private static OWLObjectRenderer ren = new ManchesterOWLSyntaxOWLObjectRendererImpl();
	
	public static CW5 prepareCW5(String name) {
		ClassLoader classloader = Thread.currentThread().getContextClassLoader();
		InputStream is = classloader.getResourceAsStream(name);
		try {
			Files.copy(is, new File(new File("").getAbsolutePath(), "cw5_ontology.owl").toPath(),
					StandardCopyOption.REPLACE_EXISTING);
			return new CW5(new File("cw5_ontology.owl"));
		} catch (IOException e) {
			e.printStackTrace();
		} catch (OWLOntologyCreationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

	public static String render(OWLObject ce) {
		return ren.render(ce);
	}

}
