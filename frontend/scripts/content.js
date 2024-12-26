// content.js - In-Page Interactions for Scanning

// Function to notify background script when a download link is clicked
function monitorDownloadLinks() {
    document.addEventListener("click", (event) => {
        const target = event.target;
        if (target.tagName === "A" && target.href) {
            const fileUrl = target.href;
            chrome.runtime.sendMessage({
                type: "DOWNLOAD_INITIATED",
                fileUrl: fileUrl,
            });
        }
    });
}

// Function to scan visible links on the page
function scanVisibleLinks() {
    const links = document.querySelectorAll("a[href]");
    links.forEach((link) => {
        chrome.runtime.sendMessage({
            type: "URL_SCAN",
            url: link.href,
        });
    });
}

// Run the functions when the content script is loaded
monitorDownloadLinks();
scanVisibleLinks();

// Listen for messages from the background script to display alerts
chrome.runtime.onMessage.addListener((request) => {
    if (request.type === "SHOW_ALERT") {
        // Reuse alert.js for consistent notifications
        const script = document.createElement("script");
        script.src = chrome.runtime.getURL("notifications/alert.js");
        document.body.appendChild(script);

        // Trigger the alert
        script.onload = () => {
            showNotification(request.message, request.alertType);
            script.remove();
        };
    }
});
