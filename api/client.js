const BASE_URL = 'http://10.0.2.2:8000/api'; // Change to your backend URL

export async function loginWithEmail(email, password) {
  const res = await fetch(`${BASE_URL}/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  return res.json();
}

export async function sendOTP(mobile) {
  const res = await fetch(`${BASE_URL}/send-otp/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mobile })
  });
  return res.json();
}

export async function verifyOTP(mobile, otp_code) {
  const res = await fetch(`${BASE_URL}/verify-otp/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mobile, otp_code })
  });
  return res.json();
}

export async function loginWithOTP(mobile, otp_code) {
  // This can be the same as verifyOTP if backend returns user info
  return verifyOTP(mobile, otp_code);
}
