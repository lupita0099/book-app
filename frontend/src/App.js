import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './screens/LoginScreen';
import SignUpScreen from './screens/SignUpScreen';
import HomeScreen from './screens/HomeScreen';
import UserInfoScreen from './screens/UserInfoScreen';
import ReadingHistoryScreen from './screens/ReadingHistoryScreen';
import { SavedBooksProvider } from './contexts/SavedBooksContext';

const Stack = createStackNavigator();

function App() {
  return (
    <SavedBooksProvider>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Login">
          <Stack.Screen 
            name="Login" 
            component={LoginScreen} 
            options={{ headerShown: false }} 
          />
          <Stack.Screen 
            name="SignUp" 
            component={SignUpScreen} 
            options={{ headerShown: false }} 
          />
          <Stack.Screen 
            name="UserInfo" 
            component={UserInfoScreen} 
            options={{ headerShown: false }} 
          />
          <Stack.Screen 
            name="ReadingHistory" 
            component={ReadingHistoryScreen} 
            options={{ headerShown: false }} 
          />
          <Stack.Screen 
            name="Home" 
            component={HomeScreen} 
            options={{ headerShown: false }} 
          />
        </Stack.Navigator>
      </NavigationContainer>
    </SavedBooksProvider>
  );
}

export default App;
