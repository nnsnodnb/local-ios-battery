<!DOCTYPE html>
<html>
    <head>
        <title>Battery Status Viewer</title>
        <meta charset="UTF-8">
        <link type="text/css" rel="stylesheet" href="/static/css/bootstrap.min.css">
        <link type="text/css" rel="stylesheet" href="/static/css/battery.css">

        <script src="/static/js/jquery.min.js"></script>
        <script src="/static/js/bootstrap.min.js"></script>
    </head>

    <body>
        <div class="container">
            <div class="row">
                % for battery in batteries:
                <div class="col-xs-4">
                    <p style="color: #fff;">{{ battery.name }}: {{ battery.battery }}%</p>
                % if battery.battery >= 6 and battery.battery <= 10:
                    <p class="battery empty"></p>
                % elif battery.battery >= 11 and battery.battery <= 20:
                    <p class="battery ten"></p>
                % elif battery.battery >= 21 and battery.battery <= 30:
                    <p class="battery twenty"></p>
                % elif battery.battery >= 31 and battery.battery <= 40:
                    <p class="battery thirty"></p>
                % elif battery.battery >= 41 and battery.battery <= 50:
                    <p class="battery forty"></p>
                % elif battery.battery >= 51 and battery.battery <= 60:
                    <p class="battery half"></p>
                % elif battery.battery >= 61 and battery.battery <= 70:
                    <p class="battery sixty"></p>
                % elif battery.battery >= 71 and battery.battery <= 80:
                    <p class="battery seventy"></p>
                % elif battery.battery >= 81 and battery.battery <= 90:
                    <p class="battery eighty"></p>
                % elif battery.battery >= 91 and battery.battery <= 99:
                    <p class="battery ninety"></p>
                % elif battery.battery == 100:
                    <p class="battery full"></p>
                % end
                </div>
                % end
            </div>
        </div>
    </body>
</html>
