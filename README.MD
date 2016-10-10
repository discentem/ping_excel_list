**Purpose:** Pings all of the servers in a specified column in a `.xlsx` file. 

I used it in a production scenario to check if `500+ servers` were online/responsive. 

**Warnings:** 
		*I haven't tested this on many datasets, so I might have missed certain error-checking cases for cell data (which could 		lead to crashes).
	      *This ideally should be using my `ExcelColumnHeaders` project as an import but is not currently. 
	      *`pingExcelList.py` currently assumes there is a `.xlsx` file exists in the directory. 
	    
**Requirements:** `openpyxl` module must be installed. The easiest method I have found is `pip install openpyxl`.
	    
**Usage**: Run `python pingExcelList.py`. Currently assumes there is a `.xlsx` file exists in the directory. 
