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
Download and install latest [release package](https://github.com/wkobiela/jobScrapper/releases) using pip:
```
python3 -m venv new-venv
linux: source new-venv/bin/activate
windows: .\new-venv\Scripts\Activate.ps1

python3 -m pip install jobscrapper-current_version-py3-none-any.whl
```
```
> jobscrapper --help
usage: jobscrapper [-h] --config CONFIG

    jobScrapper -  Simplify your IT job search.
    How to use: https://github.com/wkobiela/jobScrapper/blob/master/README.md

options:
  -h, --help       show this help message and exit
  --config CONFIG  Path to the configuration file
```

Provide new, or use example `config.json` file with configuration for every scrapper. Example config is inside this repository.

```json
{
    "excel_settings": {
        "EXCEL_NAME": "jobs.xlsx",
        "NOFLUFFJOBS_SHEET": "NoFluffJobs",
        "BULLDOGJOB_SHEET": "BulldogJob",
        "JUSTJOINIT_SHEET": "JustJoinIt"
    },
        "search_params": {
            "nofluffjobs_settings": {
                "site": "NoFluffJobs",
                "role": "testing",
                "lvl": "junior,mid",
                "city": "Gdańsk"
            },
            "bulldogjob_settings": {
                "site": "BulldogJob",
                "role": "qa,tester",
                "lvl": "junior,medium",
                "city": "Remote,Gdańsk"
            },
            "justjoinit_settings": {
                "site": "JustjoinIt",
                "role": "testing",
                "lvl": "mid.senior",
                "city": "Gdańsk"
            }
    }
}
```

### Excel settings
- EXCEL_NAME - this is name of excel file, that will be generated
- SHEET - results from every scrapper will be stored in another tab/sheet in excel spreadsheet. You can leave it as it is.

### NoFluffJobs
To setup nofluffjobs scrapper, insert 3 MAIN parameters. 
- role (string, roles separated by a comma) from available: 
```
frontend,fullstack,mobile,testing,devops,embedded,architecture,security,gaming,artificial-intelligence,big-data,support,it-administrator,agile,product-management,project-manager,business-intelligence,business-analyst,ux,erp,electronics,telecommunication,electrical-eng,automation,robotics,mechanics,sales,marketing,backoffice,hr,finance,customer-service,other
```
- lvl (string, levels separated by a comma) from available: `junior,mid,senior,expert`
- city (string) - this scrapper always looks for `remote` + city, that you define here.

### BulldogJob
To setup bulldogjob scrapper, insert 3 MAIN parameters.

- role (string, roles separated by a comma) from available: 
```
devops,frontend,fullstack,backend,analyst,administrator,project_manager,qa,tester,mobile,architect,support,tech_lead,embedded,scrum_master,security,designer,gamedev,data,consultant
```
- lvl (string, levels separated by a comma) from available: `junior,medium,senior`
- city (string, separated by a comma) - include `Remote` if you want to.

### JustJoinIt

To setup justnoinit scrapper, insert 3 MAIN parameters.
- role (single string) from available: 
```
'testing', 'net', 'architecture', 'ruby', 'php', 'mobile', 'other', 'analytics', 'erp', 'go', 'admin', 'scala', 'pm', 'support', 'data', 'java', 'security', 'game', 'python', 'ux', 'c', 'javascript', 'devops', 'html'
```
- lvl (strings separated by comma) from avaliable: `'junior', 'mid', 'senior', 'c-level'`
- city (string) - always looking for remote + eventually in the city of your choosing


### After initial (one time) setup, just use:
```
jobscrapper --config config.json
```

## Development

### Building
To build wheel package locally, use:
```
python -m build
```

## Tests
There are some tests implemented, to check a few methods. Clone repository, install requirements and run tests with:
```
cd jobScrapper

python3 -m pip install -r requirements.txt

pytest 
or 
pytest tests/test_file_to_run.py
```

## License 
This project is under the GNU General Public License v3.0. See the LICENSE file for the full license text.