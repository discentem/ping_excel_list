**Purpose:** Pings all of the servers in a specified column in a `.xlsx` file. 

I used it in a production scenario to check if `500+ servers` were online/responsive. 

**Warnings:**
*I used this for one particular dataset, so I might be ignoring certain cell values for seemingly unknown reasons or not-error checking for seemingly obvious things. Feel free to submit a PR to make this more generally useful. 
*This ideally should be using my `ExcelColumnHeaders` project as an import but is not currently. 
*`pingExcelList.py` currently assumes there is a `.xlsx` file in the project directory. 
	    
**Requirements:** `openpyxl` module must be installed. The easiest method I have found is `pip install openpyxl`.
	    
**Usage**: Run `python pingExcelList.py`. Currently assumes there is a `.xlsx` file in the project directory. 
