# uuid_tools.py
Web-API for [uuidtools.com](https://www.uuidtools.com) website that provides a free tool and API for generating UUIDs on-the-fly

## Example
```python
from uuid_tools import UuidTools

uuidt = UUIDTools()
decoded_uuid = uuidt.decode_uuid(uuid="")
print(decoded_uuid)
```
