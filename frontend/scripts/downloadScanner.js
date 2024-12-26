// downloadScanner.js - File and URL Scanning Logic

const SAFE_API_ENDPOINT = "http://localhost:5000/analyze"; // Backend server endpoint

// Function to scan a downloaded file using its hash
async function scanFileHash(fileName, fileHash) {
    try {
        const response = await fetch(SAFE_API_ENDPOINT, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ type: "file", hash: fileHash, name: fileName }),
        });

        const result = await response.json();
        return result.isSafe ? "safe" : "unsafe";
    } catch (error) {
        console.error("Error scanning file:", error);
        return "error";
    }
}

// Function to analyze URLs
async function analyzeURL(url) {
    try {
        const response = await fetch(SAFE_API_ENDPOINT, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ type: "url", url: url }),
        });

        const result = await response.json();
        return result.isSafe ? "safe" : "malicious";
    } catch (error) {
        console.error("Error analyzing URL:", error);
        return "error";
    }
}

// Export the functions for use in other scripts
export { scanFileHash, analyzeURL };
