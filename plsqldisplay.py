from IPython.display import display, HTML
def display_plsql(plsqlcode: str) -> str:
  html:str = """<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>PL/SQL Code Editor</title>
      <!-- Include a CSS file for syntax highlighting -->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/androidstudio.min.css">
      <!-- Include a JavaScript file for syntax highlighting -->
      <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/highlight.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/languages/pgsql.min.js"></script>
      <style>
              /* Style for the container */
              #code2 {
                  position: relative;
                  width: 90%;
                  height: 200px;
                  overflow: auto; /* Add scrollbars when content overflows */
                  white-space: pre-wrap; /* Preserve whitespace and wrap long lines */
                  border: 1px solid #ccc;
              }

              /* Style for the copy button */
              #copyButton {
                  position: absolute;
                  top: 10px;
                  right: 10px;
                  cursor: pointer;
                  background-color: #4CAF50;
                  color: white;
                  padding: 5px 10px;
                  border: none;
                  border-radius: 3px;
              }
          </style>
  </head>
  <body>
      <pre id="code2" rows="10" class="language-pgsql" >PLSQLCODE
      </pre>
      <button id="copyButton" onclick="copyToClipboard()">Copiar</button>

    <script>
        // Function to copy the content of the pre element to the clipboard
        function copyToClipboard() {
            // Get the text content of the pre element
            var codeContainer = document.getElementById('code2');
            var codeText = codeContainer.textContent || codeContainer.innerText;

            // Create a temporary textarea element to hold the text
            var tempTextarea = document.createElement('textarea');
            tempTextarea.value = codeText;

            // Append the textarea to the document
            document.body.appendChild(tempTextarea);

            // Select the text in the textarea
            tempTextarea.select();
            tempTextarea.setSelectionRange(0, 99999); // For mobile devices

            // Execute the copy command
            document.execCommand('copy');

            // Remove the temporary textarea
            document.body.removeChild(tempTextarea);

            // Provide visual feedback (optional)
            alert('Copiado!');
        }
    </script>
      <script>
          // Initialize the syntax highlighting
          hljs.highlightAll();
          hljs.highlightElement(document.getElementById('code2'));
      </script>
  </body>
  </html>"""
  display(HTML(html.replace("PLSQLCODE",plsqlcode)));