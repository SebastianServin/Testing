import React, { useContext } from 'react';
import { Input, Button } from 'react-native-elements';
import { Context as LocationContext } from '../context/LocationCotext';
import useSaveTrack from '../hooks/useSaveTracks';
import Spacer from './Spacer';

const TrackForm = () => {
    const { state: { name, recording, locations }, 
            startRecording, 
            stopRecording, 
            changeName } = useContext(LocationContext);

    const [saveTrack] = useSaveTrack();
            
    return (
        <>
            <Input value={name} onChangeText={changeName} placeholder="Enter Track Name"/>
            <Spacer>
                {recording 
                    ? <Button title="Stop" onPress={stopRecording} /> 
                    : <Button title="Start Recording" onPress={startRecording}/>
                }       
            </Spacer>
            <Spacer>
                { !recording && locations.length
                    ? <Button title="Save Recording" onPress={saveTrack}/> 
                    : null
                }     
            </Spacer>            
        </>
    );
};

export default TrackForm;