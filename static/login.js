document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const sessionMessage = document.getElementById('session-message');

    if (!loginForm || !sessionMessage) {
        console.error('Required elements not found');
        return;
    }

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        if (!username || !password) {
            showMessage('Please fill in all fields', 'error');
            return;
        }

        try {
            const response = await fetch('/login', {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({ username, password }),
                credentials: 'same-origin'
            });

            const data = await response.json();

            if (response.ok) {
                showMessage('Login successful! Redirecting...', 'success');
                // Use the redirect URL from the response
                if (data.redirect) {
                    window.location.href = data.redirect;
                } else {
                    window.location.href = '/chatbot';
                }
            } else {
                showMessage(data.error || 'Login failed', 'error');
            }
        } catch (error) {
            console.error('Login error:', error);
            showMessage('Connection error. Please try again.', 'error');
        }
    });

    function showMessage(text, type) {
        sessionMessage.textContent = text;
        sessionMessage.classList.remove('hidden');
        
        if (type === 'success') {
            sessionMessage.className = 'mt-4 text-center p-3 rounded-xl bg-green-100 text-green-700 border border-green-200';
        } else {
            sessionMessage.className = 'mt-4 text-center p-3 rounded-xl bg-red-100 text-red-700 border border-red-200';
        }
    }
});