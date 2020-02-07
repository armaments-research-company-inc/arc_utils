# arc_utils
Utilities methods for ARC python code

Modules in `arc_utils` :

- `KafkaLogProducer`
- `DateUtils`


## 1. KafkaLogProducer

`KafkaLogProducer` is a kafka producer that produces messages on `niobrara-70979.elastic-log` kafka topic.

The `log-engine` server consumes messages from `niobrara-70979.elastic-log` and pushes to elastic search.

The goal for this architecture is to remove elastic search dependency from each service.

### API

- #### produce_log

`produce_log` takes in three arguments: `index`, `doc`, and `doc_type`

1. the first argument is the elastic search index.
    
2. the second argument is the document that needs to be pushed.
    
3. the third argument is the document type which is usually `_doc`.
    

```python
from arc_utils.producer import KafkaLogProducer

broker_urls = ['kafka://host:port', 'kafka://host:port']
producer = KafkaLogProducer(broker_urls)
producer.produce_log("log-index", doc=doc, doc_type="_doc")

```


## 2. DateUtils

DateUtils is a python class that allows you to evaluate time in milliseconds with similar to the atak device.

### APIs

- #### elapsed_time()
gets time in milliseconds from 01-01-2016

Example:

```python        
from arc_utils.date import DateUtils

dt = DateUtils()
dt.elapsed_time()
````

- #### elapsed_from(time_in_milliseconds)

gets time difference from passed argument and 01-01-2016

Example:

```python

from arc_utils.date import DateUtils

dt = DateUtils()
dt.elapsed_from(dt.elapsed_time())
```

## 3. Logger

Logger is a python class that allows you to create formated logs and enables log rotation.

### APIs

- #### getLogger()
gets logger object for logging

Example:

```python        
from arc_utils.logger import Logger

logger = Logger("log-file-path.log").getLogger()
logger.info("msg")
logger.warn("msg")
logger.error("msg")
````
