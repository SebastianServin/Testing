import * as Location from 'expo-location';

const tenMetersWithDegrees = 0.0001;

const getLocation = increment => {
    return {
        timestamp: 10000000,
        coords: {
            speed: 5,
            heading: 0,
            accuracy: 5,
            altitudeAccuracy: 5,
            altitude: 5,
            longitude: -106.3853392424505 + increment * tenMetersWithDegrees,
            latitude: 31.710436923060012 + increment * tenMetersWithDegrees,
        }
    };
};

let counter = 1;
setInterval(() => {
    Location.EventEmitter.emit('Expo.locationChanged', {
        watchId: Location._getCurrentWatchId(),
        location: getLocation(counter)
    });
    counter++;
}, 1000);