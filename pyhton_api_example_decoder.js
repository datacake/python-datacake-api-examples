function Decoder(request) {

    // Parse JSON string in request body to real json
    var payload = JSON.parse(request.body);

    // Extract serial number in payload for device routing
    var serial = payload.s;
    
    // Return an array of dictionaries to Datacake
    // Each dictionary contains device serial, database identifier and value
    return [
        {
            device: serial, // Serial number of device
            field: "TEMPERATURE", // Identifier of database field
            value: payload.t // Actual data value for field
        },
        {
            device: serial,
            field: "HUMIDITY",
            value: payload.h
        },
        {
            device: serial,
            field: "PRESSURE",
            value: payload.p
        },
        {
            device: serial,
            field: "LIGHT",
            value: payload.l
        },
        {
            device: serial,
            field: "POWER_STATUS",
            value: payload.ps
        },
        {
            device: serial,
            field: "LOCATION",
            value: payload.loc
        },
    ];
}