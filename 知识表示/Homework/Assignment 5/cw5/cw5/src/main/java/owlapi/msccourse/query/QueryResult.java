package owlapi.msccourse.query;

import org.semanticweb.owlapi.model.OWLEntity;

public class QueryResult {
	
	final boolean direct;
	final QueryType type;
	final OWLEntity e;
	
	QueryResult(OWLEntity e, boolean direct, QueryType t) {
		this.direct = direct;
		this.type=t;
		this.e=e;
	}
	
	@Override 
	public String toString() {
		String out = e.getIRI().getRemainder().or("UNKOWN");
		//out+=direct&&type!=QueryType.EQUIVALENTCLASSES ? " (direct)" : " (indirect)";
		//out+=type.toString()+")";
		return out;
	}
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + (direct ? 1231 : 1237);
		result = prime * result + ((e == null) ? 0 : e.hashCode());
		result = prime * result + ((type == null) ? 0 : type.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		QueryResult other = (QueryResult) obj;
		if (direct != other.direct)
			return false;
		if (e == null) {
			if (other.e != null)
				return false;
		} else if (!e.equals(other.e))
			return false;
		if (type != other.type)
			return false;
		return true;
	}

	public OWLEntity getEntity() {
		// TODO Auto-generated method stub
		return e;
	}

}
