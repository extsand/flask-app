import logging.handlers

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/tmp/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html>
<html>
	<link rel="stylesheet" href="style.css">
	<link rel="stylesheet" href="./css/style_add.css">
  <head>
    <title>Elastic Beanstalk Color.App </title>
   
  </head>
  <body>
	<style>

	body {
	color: #ffffff;
	font-family: Arial, sans-serif;
	font-size:14px;
	-moz-transition-property: text-shadow;
	-moz-transition-duration: 4s;
	-webkit-transition-property: text-shadow;
	-webkit-transition-duration: 4s;
	text-shadow: none;
}
body.blurry {
	-moz-transition-property: text-shadow;
	-moz-transition-duration: 4s;
	-webkit-transition-property: text-shadow;
	-webkit-transition-duration: 4s;
	text-shadow: #fff 0px 0px 25px;
}
a {
	color: #55aaff;
}
.textColumn, .linksColumn {
	padding: 2em;
}
.textColumn {
	position: absolute;
	top: 0px;
	right: 50%;
	bottom: 0px;
	left: 0px;
}

.linksColumn {
	position: absolute;
	top:0px;
	right: 0px;
	bottom: 0px;
	left: 50%;
	background-color: #33342D;
}

h1 {
	color: #33342D;
	font-size: 500%;
	font-weight: normal;
	margin-bottom: 0em;
}

ul {
	padding-left: 1em;
	margin: 0px;
}
li {
	margin: 1em 0em;
}

	h1 {
  color: #000501;
  font-size: 6rem;
  font-weight: 600; }

h2 {
  font-size: 3rem; }

.textColumn, .linksColumn {
  background-color: green;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center; }

p {
  font-size: 1.4rem;
  text-align: center; }

.linksColumn {
  background-color: #000501;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex; }

.controller {
  font-size: 1.5rem;
  cursor: pointer; }

ul li {
  list-style-type: none;
  text-align: center;
  color: #000;
  display: block;
  background-color: #73AB84;
  padding: 1rem 3rem;
  border-radius: 10px; }
  ul li:hover {
    -webkit-box-shadow: 0px 0px 10px #79C7C5;
            box-shadow: 0px 0px 10px #79C7C5;
    background-color: #79C7C5; }

.notification {
  margin-bottom: 1rem;
  position: relative;
  font-size: 1.3rem;
  opacity: 0;
  -webkit-transition: all 0.4s ease-in;
  -o-transition: all 0.4s ease-in;
  transition: all 0.4s ease-in; }
  .notification:before {
    content: '';
    background-color: red;
    display: block;
    position: absolute;
    right: -19px;
    top: -19px;
    width: 15px;
    height: 15px;
    border-radius: 50%; }

.colorCode {
  font-size: 3rem;
  font-weight: 600;
  letter-spacing: 2px; }
/*# sourceMappingURL=style_add.css.map */

 
	</style>




    <div class="textColumn">
      <h1>Color.app</h1>
      <p class="first_line">It's simple js app. You can change background-color with controllers in right panel. 
			<br> 
			This environment is launched with Elastic Beanstalk Node.js Platform</p>
			<p class="second_line"></p>

			<div class="notification">color copied</div>
			<div class="colorCode">#005800</div>
			
			
      
    </div>
    <div class="linksColumn">
      <h2>What color do you like?</h2>
      <ul>
				<li class="controller" data-colorChoice="green">Green</li>
				<li class="controller" data-colorChoice="yellow">Yelow</li>
				<li class="controller" data-colorChoice="red">Red</li>
				<li class="controller" data-colorChoice="blue">Blue</li>
				<li class="controller" data-colorChoice="purpure">Purpure</li>
				<li class="controller" data-colorChoice="orange">Orange</li>
				
      </ul>
    </div>
  </body>
	<script>
		//Color choice app
			const controllers = document.querySelectorAll('.controller')
			const leftPanel = document.querySelector('.textColumn')
			const colorCode = document.querySelector('.colorCode')
			const notification = document.querySelector('.notification')



			//  leftPanel.style.backgroundColor = "red";

			const colorsDB = { 
				yellow: '#EFA00B',
				blue: '#228cdb',
				purpure: '#170A1C',
				red: '#F71735',
				orange: '#FF9F1C',
				green: '#4CE670'

			}


			// console.log(controllers)
			controllers.forEach( item => {
				console.log(item.dataset.colorchoice)

				item.addEventListener('click', (e) => {
					
					const color = e.target.dataset.colorchoice
					const setColor = colorsDB[color]
					leftPanel.style.transition = "all 2s"
					leftPanel.style.backgroundColor = setColor	
					

					colorCode.textContent = setColor

				})
			})



			colorCode.addEventListener('click', (e) => {
				const selectedText = colorCode.textContent
				console.log(selectedText)


			const navi = 	navigator.clipboard.writeText(selectedText)
					.then( (data) => {
						console.log('text copied')
						addNotification('color copied')
						
					
					})
					.catch((err) => console.log(err))	

				
			})


			function addNotification(text, timeout=1000) {
				notification.textContent = text
				notification.style.opacity = 1
				setTimeout(() => {
					notification.style.opacity = 0
				}, timeout)
			}




	</script>
</html>






"""





def application(environ, start_response):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'],
                            environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
