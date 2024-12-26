// background.js - Trigger Notifications

// Simulate unsafe file detection
// unsafe file detected code-
chrome.downloads.onDeterminingFilename.addListener((downloadItem) => {
    const unsafe = Math.random() < 0.3; // Random simulation for testing
    if (unsafe) {
        chrome.runtime.sendMessage({
            type: "FILE_ALERT",
            fileName: downloadItem.filename,
        });
    }
});

// Simulate malicious URL detection
chrome.webRequest.onBeforeRequest.addListener(
    (details) => {
        const blockedURL = "http://example.com/malicious"; // Example malicious
        if (details.url.includes(blockedURL)) {
            chrome.runtime.sendMessage({
                type: "URL_ALERT",
                url: details.url,
            });
            return { cancel: true }; // Block the request
        }
    },
    { urls: ["<all_urls>"] },
    ["blocking"]
);
