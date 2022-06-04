/**
 * 
 */
package owlapi.fhkb.fspopulation;

import java.util.Arrays;

/**
 * @author Yizheng
 * 
 * Simple Java Bean to hold job data
 *
 */
public class JobDataBean {

	private String surname = null;
	private String marriedSurname = null;
	private Integer birthYear = null;
	private String givenName = null;
	private Integer year = null;
	private String source = null;
	private String occupation = null;
	
	
	public String getSurname() {
		return surname;
	}
	public void setSurname(String surname) {
		this.surname = surname;
	}
	public String getMarriedSurname() {
		return marriedSurname;
	}
	public void setMarriedSurname(String marriedSurname) {
		this.marriedSurname = marriedSurname;
	}
	public Integer getBirthYear() {
		return birthYear;
	}
	public void setBirthYear(int birthYear) {
		this.birthYear = birthYear;
	}
	public String getGivenName() {
		return givenName;
	}
	public void setGivenName(String givenName) {
		this.givenName = givenName;
	}
	public Integer getYear() {
		return year;
	}
	public void setYear(int year) {
		this.year = year;
	}
	public String getSource() {
		return source;
	}
	public void setSource(String source) {
		this.source = source;
	}
	public String getOccupation() {
		return occupation;
	}
	public void setOccupation(String occupation) {
		this.occupation = occupation;
	}
	
	

	@Override
	public String toString() {

		return givenName + " " + surname + " (" + marriedSurname + ") " + birthYear + " " + year + " " + source + " " + occupation;
	}
	/*-----------------------------------------------------------------------------------------------------
	 * Don't change anything below this
	 *----------------------------------------------------------------------------------------------------- 
	 */
	public void deserialize(String[] parts) {

		if (parts.length < 7) throw new RuntimeException("Wrong CSV format, not enough fields: " + Arrays.toString(parts));
		
		surname = isEmpty(parts[0]) ? null : parts[0];
		marriedSurname = isEmpty(parts[1]) ? null : parts[1];
		birthYear = isEmpty(parts[2]) ? null : Integer.valueOf(parts[2]);
		givenName = isEmpty(parts[3]) ? null : parts[3];
		year = isEmpty(parts[4]) ? null : Integer.valueOf(parts[4]);
		source = isEmpty(parts[5]) ? null : parts[5];
		occupation = isEmpty(parts[6]) ? null : parts[6];
	}
	
	//TODO Reflection could be useful here but we don't bother...
	public void copyMissingFields(JobDataBean bean) {

		if (isEmpty(surname)) {
			
			surname = bean.getSurname();
			
			if (isEmpty(marriedSurname)) marriedSurname = bean.getMarriedSurname();
			if (isEmpty(givenName)) givenName = bean.getGivenName();
			if (birthYear == null) birthYear = bean.getBirthYear();			
		}
	}
	
	private boolean isEmpty(String val) {
		
		return val == null || val.length() == 0;
	}
}
