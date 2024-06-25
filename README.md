# Addition of Integers in a list

## Clone Git Repository

```bash
git clone https://github.com/alokkumarsbg/assesment
```

## Create a Virtual Environment
```bash 
python -m venv <Virtual env name>
```
Enable the Virtual Environment

## Install packages from requirements.txt
```bash
pip install -r requirements.txt
```
 ## Steps to execute the Webserver
```bash
cd addition
python main.py
```
## To run Test Cases
```bash
pytest
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## API to run from Postman
### Post request http://127.0.0.1:8000/api/add
```bash
Body:
{"batchid":"test01","lists":[[1, 2], [3, 4]]}

Response:
{
    "batchid": "test01",
    "results": [
        3,
        7
    ],
    "status": "complete",
    "started_at": "2024-06-25T20:57:42.381890",
    "completed_at": "2024-06-25T20:57:45.946702"
}
```

