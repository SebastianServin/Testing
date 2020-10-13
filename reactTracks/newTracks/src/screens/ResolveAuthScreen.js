import React, { useEffect, useContext } from 'react';
import { Text } from 'react-native';
import { Context as AuthContext } from '../context/AuthContext';

const ResolveAuthScreeen = () => {
    const { tryLocalSignin } = useContext(AuthContext);

    useEffect(() => {
        tryLocalSignin();
    }, []);
    return null;    
}

export default ResolveAuthScreeen;

