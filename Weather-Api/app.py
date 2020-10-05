from weatherApi import create_app


create_app().run(
    host='0.0.0.0',
    debug=True,
    port=8080
)
