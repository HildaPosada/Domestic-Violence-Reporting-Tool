<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Emergency Report</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      line-height: 1.6;
      color: #333;
    }
    header {
      background: #d32f2f;
      color: #fff;
      text-align: center;
      padding: 20px 10px;
    }
    header .hotline {
      font-size: 1.2em;
      margin-top: 10px;
    }
    .main-container {
      padding: 20px;
      text-align: center;
    }
    .main-container h1 {
      color: #d32f2f;
      font-size: 1.8em;
    }
    .main-container p {
      font-size: 1.1em;
      margin-bottom: 20px;
    }
    .report-form {
      max-width: 400px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
    .report-form label {
      display: block;
      text-align: left;
      margin-bottom: 8px;
    }
    .report-form input,
    .report-form textarea,
    .report-form select {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .report-form button {
      width: 100%;
      background: #d32f2f;
      color: #fff;
      border: none;
      padding: 12px;
      font-size: 1.1em;
      cursor: pointer;
      border-radius: 5px;
    }
    .report-form button:hover {
      background: #c62828;
    }
    .emergency-button {
      display: inline-block;
      margin-top: 20px;
      padding: 15px 20px;
      font-size: 1.2em;
      font-weight: bold;
      color: #fff;
      background: #d32f2f;
      border: none;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.3s ease;
    }
    .emergency-button:hover {
      background: #c62828;
    }
    footer {
      background: #d32f2f;
      color: #fff;
      text-align: center;
      padding: 10px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <header>
    <h1>Emergency Violence Report</h1>
    <p class="hotline">Hotline: <a href="tel:+18007997233" style="color: #ffeb3b;">1-800-799-7233</a></p>
  </header>

  <div class="main-container">
    <h1>Report Now</h1>
    <p>If you are in danger, report the incident below quickly. Stay safe!</p>
    <form action="#" method="POST" class="report-form">
      <label for="location">Location:</label>
      <input type="text" id="location" name="location" placeholder="Enter city or address" required>

      <label for="description">What happened?</label>
      <textarea id="description" name="description" rows="5" placeholder="Describe the incident" required></textarea>

      <label for="category">Type of Violence:</label>
      <select id="category" name="category" required>
        <option value="domestic">Domestic Violence</option>
        <option value="workplace">Workplace Violence</option>
        <option value="school">School Violence</option>
        <option value="public">Public Violence</option>
      </select>

      <button type="submit">Submit Report</button>
    </form>
    <a href="tel:+911" class="emergency-button">Call 911</a>
  </div>

  <footer>
    <p>&copy; 2024 Emergency Report. All rights reserved.</p>
  </footer>
</body>
</html>