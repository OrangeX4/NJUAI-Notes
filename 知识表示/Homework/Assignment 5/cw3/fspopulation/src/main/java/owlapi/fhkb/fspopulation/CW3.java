package owlapi.fhkb.fspopulation;

import java.io.InputStream;
import java.util.Collection;

import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyManager;

import org.semanticweb.owlapi.model.*;
import org.semanticweb.owlapi.util.DefaultPrefixManager;
import org.semanticweb.owlapi.model.OWLIndividual;
import java.util.*;


/**
 * Nanjing University<br>
 * School of Artificial Intelligence<br>
 * KRistal Group<br>
 * 
 * Acknowledgement: with great thanks to Nico at Cambridge for the insightful discussions and his useful suggestions in making this project. 
 *
 * This class MUST HAVE A ZERO ARGUMENT CONSTRUCTOR!
 */

public class CW3 {

    private static String NAMESPACE = "http://ai.nju.edu.cn/krp/FamilyHistory#";


    protected CW3() {
        // Do not specify a different constructor to this empty constructor!
    }

    
    protected void populateOntology(OWLOntologyManager manager, OWLOntology ontology, Collection<JobDataBean> beans) {
    	// implement
    }
    
    
    protected OWLOntology loadOntology(OWLOntologyManager manager, InputStream inputStream) {
    	//implement
    	return null;
    }
    
    protected void saveOntology(OWLOntologyManager manager, OWLOntology ontology, IRI locationIRI) {
    	// implement
        
    }

}
