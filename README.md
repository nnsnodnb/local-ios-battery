# local-ios-battery

Monitor battery status of local iOS devices.

## Installation

### Python application

```console
$ git clone https://github.com/nnsnodnb/local-ios-battery.git
$ cd /path/to/local-ios-battery/server
$ pip install -r requirements.txt
$ gunicorn battery:app -b 0.0.0.0:8080
```

### iOS application

```console
$ brew update
$ brew install carthage
$ carthage bootstrap --platform ios
$ open /path/to/local-ios-battery/client/LocalBattery/LocalBattery.xcodeproj/
```

Edit hostname of URL written in `AppDelegate.swift`. (L.50 & L.67)

## LICENSE

Apache License 2.0

## Author

nnsnodnb

