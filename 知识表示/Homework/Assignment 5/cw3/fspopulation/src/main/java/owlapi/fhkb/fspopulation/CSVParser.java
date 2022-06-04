/**
 * 
 */
package owlapi.fhkb.fspopulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;


/**
 * 
 * This class parses CSV files. Don't change it.
 *
 */
public class CSVParser {
	
	private static final char SEP = ',';

	/**
	 * Parses the CSV file
	 * 
	 * @param csvFile File to parse
	 * @return Collection of job beans holding the data
	 * @throws IOException if any problem occurs with reading the file
	 */
	public Collection<JobDataBean> parse(Reader reader) throws IOException {

		List<JobDataBean> results = new ArrayList<JobDataBean>();
		BufferedReader bReader = new BufferedReader(reader);
		String line = null;
		//We skip the first file
		bReader.readLine();
		
		while ((line = bReader.readLine()) != null) {
			
			JobDataBean bean = parse(line);
			//Fill some missing fields (if any)
			if (!results.isEmpty()) {
				
				JobDataBean previous = results.get(results.size() - 1);
				
				bean.copyMissingFields(previous);
			}
			//Add the list
			results.add(bean);
		}
		
		return results;
	}

	/*
	 * Parses a single line
	 */
	private JobDataBean parse(String line) {

		List<String> parts = new ArrayList<String>();
		int index = 0;
		JobDataBean bean = new JobDataBean();
		
		while ((index = line.indexOf(SEP)) >= 0) {
			
			parts.add(line.substring(0, index).trim());
			line = line.substring(index + 1);
		}
		
		parts.add(line.trim());
		bean.deserialize(parts.toArray(new String[]{}));
		
		return bean;
	}
}
