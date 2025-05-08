from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Mock data for gym packages and trainers
PACKAGES = [
    {
        'name': 'Basic Membership',
        'price': '$29.99/month',
        'features': ['Access to gym floor', 'Basic equipment usage', 'Locker room access']
    },
    {
        'name': 'Premium Membership',
        'price': '$49.99/month',
        'features': ['All Basic features', 'Group classes', 'Personal trainer consultation', 'Spa access']
    },
    {
        'name': 'Elite Membership',
        'price': '$79.99/month',
        'features': ['All Premium features', 'Private training sessions', 'Nutrition consultation', 'Priority booking']
    }
]

TRAINERS = [
    {
        'name': 'John Smith',
        'specialty': 'Strength Training',
        'experience': '10 years'
    },
    {
        'name': 'Sarah Johnson',
        'specialty': 'Yoga & Pilates',
        'experience': '8 years'
    },
    {
        'name': 'Mike Wilson',
        'specialty': 'CrossFit',
        'experience': '12 years'
    }
]

@app.route('/')
def home():
    return render_template('index.html', packages=PACKAGES, trainers=TRAINERS)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Simulate registration
        flash('Registration successful! Welcome to our gym!')
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Simulate form submission
        flash('Thank you for your message! We will get back to you soon.')
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 