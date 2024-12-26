document.getElementById("scanDownloads").addEventListener("click", () => {
    chrome.runtime.sendMessage({ action: "scanDownloads" }, (response) => {
      const resultDiv = document.getElementById("result");
      resultDiv.textContent = response.message || "No unsafe downloads found.";
    });
  });
  