// alert.js - Real-Time Notification Logic

// Function to create a toast notification
function showNotification(message, type) {
    // Create the notification container
    const notification = document.createElement("div");
    notification.className = `safeguard-notification ${type}`;
    notification.textContent = message;

    // Append the notification to the body
    document.body.appendChild(notification);

    // Remove the notification after 5 seconds
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Example usage: Listening for messages from background scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.type === "FILE_ALERT") {
        showNotification(
            `⚠️ Unsafe File Detected: ${request.fileName}`,
            "alert-danger"
        );
    } else if (request.type === "URL_ALERT") {
        showNotification(
            `🚨 Malicious URL Blocked: ${request.url}`,
            "alert-warning"
        );
    }
    sendResponse({ status: "Notification displayed" });
});
