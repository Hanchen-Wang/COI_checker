# COI_checker
An automatic COI checker to find the conflict of interest for conference submissions.

## Usage

```
python find_coi.py --file_name <file_name> --years <years> --pc_file <pc_file>
```
Example:
```
python find_coi.py --file_name ./data/ying_zhang.xml --years 2019,2020,2021 --pc_file ./data/pc_members.xlsx
```

<file_name> is the downloaded DBLP author file. Current, this checker only supports the xml format. I provide serveral downloaded pages of the professors in the data folder.

'<years>' is a string with the years you want to check. The years are separated by commas, e.g., 2019,2020,2021
 
<pc_file> is a xlsx file contains the information of PC members. You can build this by copying the coi name list from CMT and pasting in Excel. An example PC member file is provided in the data folder.

> Currently this checker is under alpha test. If you have any issue, please contact me.
