document.addEventListener("DOMContentLoaded", () => {
    const locationInput = document.getElementById("location");
    const locationStatus = document.getElementById("location-status");
  
    // Check if Geolocation API is supported
    if (navigator.geolocation) {
      locationStatus.textContent = "Fetching your location...";
  
      // Prompt the user to allow location sharing
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          locationInput.value = `${latitude},${longitude}`;
          locationStatus.textContent = "Location successfully retrieved.";
        },
        (error) => {
          locationStatus.textContent =
            "Unable to fetch location. Please check your permissions.";
        }
      );
    } else {
      locationStatus.textContent =
        "Geolocation is not supported by your browser.";
    }
  });
  