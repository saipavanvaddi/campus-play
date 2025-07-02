import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert, ActivityIndicator } from 'react-native';
import { loginWithEmail, sendOTP } from '../api/client';

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [mobile, setMobile] = useState('');
  const [loading, setLoading] = useState(false);

  const handleEmailLogin = async () => {
    setLoading(true);
    try {
      const res = await loginWithEmail(email, password);
      if (res && res.user_id && res.role) {
        if (res.role === 'faculty') {
          navigation.replace('FacultyDashboard');
        } else {
          navigation.replace('StudentDashboard');
        }
      } else {
        Alert.alert('Login Failed', res.error || 'Invalid credentials');
      }
    } catch (e) {
      Alert.alert('Error', 'Network error');
    } finally {
      setLoading(false);
    }
  };

  const handleOTPRequest = async () => {
    if (!mobile) {
      Alert.alert('Error', 'Enter mobile number');
      return;
    }
    setLoading(true);
    try {
      const res = await sendOTP(mobile);
      if (res && res.otp) {
        navigation.navigate('OTP', { mobile });
      } else {
        Alert.alert('Error', res.error || 'Failed to send OTP');
      }
    } catch (e) {
      Alert.alert('Error', 'Network error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>CampusPlay Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        autoCapitalize="none"
        keyboardType="email-address"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button title="Login with Email/Password" onPress={handleEmailLogin} />
      <Text style={{ marginVertical: 16 }}>OR</Text>
      <TextInput
        style={styles.input}
        placeholder="Mobile Number"
        value={mobile}
        onChangeText={setMobile}
        keyboardType="phone-pad"
      />
      <Button title="Login with OTP" onPress={handleOTPRequest} />
      {loading && <ActivityIndicator style={{ marginTop: 16 }} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 24,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 24,
    textAlign: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 8,
    padding: 12,
    marginBottom: 12,
  },
});
