from api_app import create_app

application = create_app()

application.run(host="0.0.0.0", debug=True)
