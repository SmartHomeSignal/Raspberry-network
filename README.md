# Raspberry-network

## Getting started

1) Install dependecies:

```
pip install websocket-client
```

2) Move `network.py` to folder with project

## Example
You can find a usage example in **example.py** file

## Usage
### Import Network class

```python
from network import Network
```

### Connect to socket
Create callback function:
```python
def callback(is_signal_on):
    # Do something (is_signal_on - Bool)
```

Initialize networking:
```python
network = Network()

network.connect(callback)
```

### Controlling signal
Enable:
```python
network.enable_signal()
```

Disable:
```python
network.disable_signal()
```

### Disconnect
```python
network.disconnect()
```
