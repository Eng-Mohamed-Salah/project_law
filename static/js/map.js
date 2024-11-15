var map = L.map("map").setView([30.0909712, 31.3234532], 13);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);
L.marker([30.0909712, 31.3234532]).addTo(map);
