import React, { useContext } from 'react';
import { Button } from 'react-native-elements';
import { Text, StyleSheet, View } from 'react-native';
import { SafeAreaView } from 'react-navigation';
import Spacer from '../components/Spacer';
import { Context as AuthContext } from '../context/AuthContext';
import { FontAwesome } from '@expo/vector-icons'; 

const AccountScreen = () => {

    const { signout } = useContext(AuthContext);

    return (
        <SafeAreaView forceInset={{ top: 'always' }}>
            <View>
                <Text style={{ fontSize: 48 }}>AccountScreen</Text>
                <Spacer>
                    <Button title="Sign Out" onPress={signout}/>
                </Spacer>
            </View>
        </SafeAreaView>
    )
};

AccountScreen.navigationOptions = {
    title: 'Account',
    tabBarIcon: <FontAwesome name="gear" size={24} color="black" />
};

const styles = StyleSheet.create({});

export default AccountScreen;