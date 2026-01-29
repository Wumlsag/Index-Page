<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apache Server Status</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #002040; /* Dark blue background from image */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            color: #ffffff;
        }

        .container {
            background-color: #0d2847; /* Slightly lighter dark blue for container */
            border: 3px solid #e6b800; /* Yellow gold border */
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            max-width: 500px;
            width: 90%;
        }

        .status-badge {
            display: inline-block;
            background-color: #28a745; /* Green badge */
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-weight: bold;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        h1 {
            color: #e6b800; /* Yellow gold text */
            font-size: 3em;
            margin: 0;
            font-weight: bold;
            text-transform: uppercase;
        }

        h2 {
            font-size: 1.5em;
            margin: 10px 0 20px;
            font-weight: normal;
        }

        p {
            font-size: 1em;
            margin-bottom: 30px;
            line-height: 1.5;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            background-color: #e6b800; /* Yellow gold button */
            color: #002040;
            padding: 12px 24px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        
        .btn:hover {
            background-color: #cdaa00;
        }

        .btn span {
            margin-right: 10px;
        }

        .footer {
            margin-top: 40px;
            font-style: italic;
            font-size: 0.9em;
            color: #b0c4de; /* Lighter text for footer */
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="status-badge">Apache Server: Operational</div>
        <h1>GO NAVY!</h1>
        <h2>Beat Army!</h2>
        <p>If you are seeing this, the server is successfully standing the watch.</p>
        
        <a href="https://xkcd.com/" target="_blank" class="btn">
            <span>🚀</span> It works!
        </a>

        <div class="footer">
            Ex Scientia Tridens
        </div>
    </div>

</body>
</html>