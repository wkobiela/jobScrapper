# jobScrapper

## Description
Simple python project, that should make it easier to be up to date with jobs offers. Websites like BulldogJob, Nofluffjobs or JustJoinIt have this nasty fature - job offers that are "refreshed" are bumped to the top of the page, so it is easy to get lost of track and even apply to the same job twice. 

This combined scrapper uses excel sheet to write down all jobs offers, that match search patterns. On subsequent starts it will check found offers against excel, exclude ones that are already scrapped and write new ones on the top as inserted rows. 

You can edit this excel, mark with color offers that are intresting (or not), even hide rows. Just do not delete them, as this is reference info for scrapper.

Best way to run this project, would be to use cron and run this regularly on schedule. This way you can yeasily organise your IT work searching process - and most important - stop waisting your time on looking through hundreds of offers every day. 

5min is enough to browse the latest.

Currently there are 3 websites supported:
- nofluffjobs
- bulldogjob
- justjoinit

That would be nice, to include more.

## How to run
Install requirements using pip:
```
python3 -m pip install -r requirements.txt
```
To setup script, edit `runner.py` and insert role, level and city you are looking for. This parameters are a little bit different for every website, but not that much.
```
EXCEL_NAME = 'jobs.xlsx'
NOFLUFFJOBS_SHEET = 'NoFluffJobs'
BULLDOGJOB_SHEET = 'BulldogJob'
JUSTJOINIT_SHEET = 'JustJoinIt'
```
`setup` will create excel named `jobs.xlsx` with 3 sheets. Do not bother with this as this point, consider it static.

### NoFluffJobs
To setup nofluffjobs scrapper, insert 3 MAIN parameters. 
- role (string, roles separated by a comma) from available: `frontend,fullstack,mobile,testing,devops,embedded,architecture,security,gaming,artificial-intelligence,big-data,support,it-administrator,agile,product-management,project-manager,business-intelligence,business-analyst,ux,erp,electronics,telecommunication,electrical-eng,automation,robotics,mechanics,sales,marketing,backoffice,hr,finance,customer-service,other`
- lvl (string, levels separated by a comma) from available: `junior,mid,senior,expert`
- city (string) - this scrapper always looks for `remote` + city, that you define here.
```
NOFLUFFJOBS_URL = common.createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk")
```

### BulldogJob
To setup bulldogjob scrapper, insert 3 MAIN parameters.

- role (string, roles separated by a comma) from available: `devops,frontend,fullstack,backend,analyst,administrator,project_manager,qa,tester,mobile,architect,support,tech_lead,embedded,scrum_master,security,designer,gamedev,data,consultant`
- lvl (string, levels separated by a comma) from available: `junior,medium,senior`
- city (string, separated by a comma) - include `Remote` if you want to.
```
BULLDOGJOB_URL = common.createLinks(site='BulldogJob', role="qa,tester", lvl="junior,mid", city="Remote,Gdańsk")
```

### JustJoinIt

To setup justnoinit scrapper, insert 3 MAIN parameters.
- role (list of strings) from available: `'testing', 'net', 'architecture', 'ruby', 'php', 'mobile', 'other', 'analytics', 'erp', 'go', 'admin', 'scala', 'pm', 'support', 'data', 'java', 'security', 'game', 'python', 'ux', 'c', 'javascript', 'devops', 'html'`
- lvl (list of strings) from avaliable: `'junior', 'mid', 'senior'`
- city (string) - always looking for remote + eventually in the city of your choosing
```
justjoinit.run(role=['testing'], lvl=["mid", "junior"], city='Gdańsk')
```

### After initial (one time) setup, just use:
```
python3 runner.py
```

## Tests
There are some tests implemented, to check a few methods. You can run them using
```
pytest 
or 
pytest tests/test_file_to_run.py
```

## License 
This project is under the GNU General Public License v3.0. See the LICENSE file for the full license text.