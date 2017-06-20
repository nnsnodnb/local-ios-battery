# local-ios-battery

Monitor battery status of local iOS devices.

## Installation

### Python application

```console
$ git clone https://github.com/nnsnodnb/local-ios-battery.git
$ cd local-ios-battery/
$ pip install -r requirements.txt
$ gunicorn battery:app -b 0.0.0.0:8080
```

### iOS application

```console
$ brew update
$ brew install carthage
$ open /path/to/local-ios-battery/client/LocalBattery/LocalBattery.xcodeproj/
```

Edit hostname of URL written in `AppDelegate.swift`. (L.50 & L.67)

## Author

nnsnodnb

