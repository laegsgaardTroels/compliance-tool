import requests
import json

URI = 'http://distribution.virk.dk/offentliggoerelser/_search'
HEADERS = {
    'Content-Type': 'application/json',
}


def es_quiery():
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "term": {
                            "dokumenter.dokumentMimeType": "application"
                        }
                    },
                    {
                        "term": {
                            "dokumenter.dokumentMimeType": "xml"
                        }
                    },
                    {
                        "range": {
                            "offentliggoerelsesTidspunkt": {
                                "gt": "2018-06-21T00:00:00.001Z",
                                "lt": "2018-06-21T23:59:59.505Z"
                            }
                        }
                    }
                ],
                "must_not": [],
                "should": []
            }
        },
       "size": 2999
    }
    return json.dumps(query) 


def main():
    print(es_quiery())
    response = (
        requests
        .get(
            URI,
            data=es_quiery(),
            headers=HEADERS,
        )
    )
    with open('sample', 'wb') as f:
        for chunk in response:
            f.write(chunk)


if __name__ == '__main__':
    main()
