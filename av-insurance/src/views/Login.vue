<template>
    <div class="login-container">
        <h2>Login</h2>
        <form @submit.prevent="handleLogin">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" placeholder="Enter your username" required />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" placeholder="Enter your password" required />
            </div>
            <button type="submit" :disabled="!isFormValid">Login</button>
        </form>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
</template>

<script>
import { ref } from 'vue'

export default {
    name: 'Login',
    setup() {
        const username = ref('')
        const password = ref('')
        const errorMessage = ref('')

        const isFormValid = computed(() => username.value && password.value)

        const handleLogin = () => {
            if (username.value === 'admin' && password.value === 'password') {
                alert('Login successful!')
                errorMessage.value = ''
                // Redirect or handle successful login here
            } else {
                errorMessage.value = 'Invalid username or password.'
            }
        }

        return {
            username,
            password,
            errorMessage,
            isFormValid,
            handleLogin
        }
    }
}
</script>

<style scoped>
.login-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
    text-align: left;
}

label {
    font-weight: bold;
}

input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

button:disabled {
    background-color: #ccc;
}

.error-message {
    color: red;
    margin-top: 10px;
}
</style>