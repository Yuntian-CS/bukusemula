importScripts('https://www.gstatic.com/firebasejs/11.9.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/11.9.1/firebase-messaging-compat.js');

firebase.initializeApp({
	apiKey: "AIzaSyANlKPVkQXyB3wObpInZdZjaiuuffvp_uc",

	authDomain: "bukusemula.firebaseapp.com",

	projectId: "bukusemula",

	storageBucket: "bukusemula.firebasestorage.app",

	messagingSenderId: "205622939353",

	appId: "1:205622939353:web:e8009b1d63b46f918778c8",

	measurementId: "G-49T5Y06WKN"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
	console.log('[firebase-messaging-sw.js] Received background message ', payload);
	const notificationTitle = payload.notification.title;
	const notificationOptions = {
		body: payload.notification.body,
		icon: '/firebase-logo.png' // Optional
	};

	self.registration.showNotification(notificationTitle, notificationOptions);
});
