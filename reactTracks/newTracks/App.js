import React from 'react';
import { createAppContainer, createSwitchNavigator } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import AccountScreen from './src/screens/AccountScreen';
import SigninScreen from './src/screens/SigninScreen';
import SignupScreen from './src/screens/SignupScreen';
import TrackCreateScreen from './src/screens/TrackCreateScreen';
import TrackDetailScreen from './src/screens/TrackDetailScreen';
import TrackListScreen from './src/screens/TrackListScreen';
import ResolveAuthScreen from './src/screens/ResolveAuthScreen';
import { Provider as AuthProvider } from './src/context/AuthContext';
import { setNavigator } from './src/navigationRef';
import { Provider as LocatioProvider } from './src/context/LocationCotext';
import { Provider as TrackProvider } from './src/context/TrackContext';
import { FontAwesome } from '@expo/vector-icons';

const trackListFlow = createStackNavigator({
  TrackList: TrackListScreen,
  TrackDetail: TrackDetailScreen
});

trackListFlow.navigationOptions = {
  title: "Tracks",
  tabBarIcon: <FontAwesome name="list-ul" size={24} color="black" />
}

const switchNavigator = createSwitchNavigator({
  RevolveAuth: ResolveAuthScreen,
  loginFlow: createStackNavigator({ 
    Signup: SignupScreen,
    Signin: SigninScreen
  }),

  mainFlow: createBottomTabNavigator({
    trackListFlow,
    TrackCreate: TrackCreateScreen,
    Account: AccountScreen,
  })
});

const App = createAppContainer(switchNavigator);

export default () => {
  return (
    <TrackProvider>
      <LocatioProvider>
        <AuthProvider>
          <App ref={(navigator) => { setNavigator(navigator) }}/>
        </AuthProvider>
      </LocatioProvider>
      </TrackProvider>
  )
}