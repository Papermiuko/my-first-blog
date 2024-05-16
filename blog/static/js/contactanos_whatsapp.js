function sendWhatsAppMessage() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    if (!name || !email || !message) {
        return;
    }

    var fullMessage = `Hola, mi nombre es ${name}, mi email es ${email}. ${message}`;
    var whatsappUrl = `https://wa.me/573046413008?text=${encodeURIComponent(fullMessage)}`; // Cambia 1234567890 por tu número de WhatsApp

    window.open(whatsappUrl, '_blank');
}
